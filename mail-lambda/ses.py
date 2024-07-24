import boto3
import email
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
import logging
from datetime import datetime
import os

logger = logging.getLogger()
logger.setLevel(logging.INFO)

s3 = boto3.client('s3')
ses = boto3.client('ses')

def lambda_handler(event, context):
    bucket = "jimchen4214-mail"
    key = event['Records'][0]['s3']['object']['key']
    logger.info(f"Processing email from bucket: {bucket}, key: {key}")

    try:
        email_content = s3.get_object(Bucket=bucket, Key=key)['Body'].read().decode('utf-8')
        msg = email.message_from_string(email_content)
        logger.info(f"Parsed email. Subject: {msg['subject']}")

        # Save the original message with new prefix
        save_email_to_s3_again(bucket, msg)

        if filter_email(msg):
            forward_email(msg)
        else:
            logger.info("Email did not pass filter, bouncing back.")
            bounce_email(msg)
    except Exception as e:
        logger.error(f"Error processing email: {str(e)}")
        raise

def save_email_to_s3_again(bucket, msg):
    now = datetime.now()
    prefix = now.strftime("%Y/%m/%d/%H%M%S")
    key = f"{prefix}_message"

    # Save the main message
    s3.put_object(Bucket=bucket, Key=key, Body=msg.as_string())

    # Save attachments
    if msg.is_multipart():
        for part in msg.walk():
            if part.get_filename():
                attachment_key = f"{prefix}_attachment_{part.get_filename()}"
                s3.put_object(Bucket=bucket, Key=attachment_key, Body=part.get_payload(decode=True))

def filter_email(msg):
    headers = ' '.join([f"{k}: {v}" for k, v in msg.items()]).lower()
    body = get_email_body(msg).lower()
    full_content = headers + ' ' + body
    
    logger.info(f"Filtering email. Headers: {headers[:100]}... Body: {body[:100]}...")

    filter_keywords = ['lottery', 'win', 'prize', 'jackpot']

    for keyword in filter_keywords:
        if keyword in full_content:
            logger.info(f"Filtered out email containing keyword: {keyword}")
            return False
    
    logger.info("Email passed filter")
    return True

def get_email_body(msg):
    if msg.is_multipart():
        for part in msg.walk():
            if part.get_content_type() == 'text/plain' and 'attachment' not in str(part.get('Content-Disposition')):
                return part.get_payload(decode=True).decode('utf-8')
    return msg.get_payload(decode=True).decode('utf-8')

def forward_email(msg):
    new_msg = MIMEMultipart()
    new_recipient = 'jimchen@mail.jimchen.me'

    for header in ['From', 'Subject', 'Date']:
        if header in msg:
            new_msg[header] = msg[header]

    new_msg['To'] = new_recipient

    if msg.is_multipart():
        for part in msg.walk():
            if part.get_content_type() in ['text/plain', 'text/html']:
                new_msg.attach(MIMEText(part.get_payload(decode=True).decode('utf-8'), part.get_content_type().split('/')[1]))
            elif part.get_filename():
                attachment = MIMEApplication(part.get_payload(decode=True), Name=part.get_filename())
                attachment['Content-Disposition'] = f'attachment; filename="{part.get_filename()}"'
                new_msg.attach(attachment)
    else:
        new_msg.attach(MIMEText(msg.get_payload(decode=True).decode('utf-8'), 'plain'))

    send_email(new_msg)

def bounce_email(msg):
    bounce_msg = MIMEMultipart('alternative')
    bounce_msg['From'] = 'no-reply@jimchen.me'
    bounce_msg['To'] = msg['From']
    bounce_msg['Subject'] = 'Your email was caught in our junk filter'

    bounce_text = """
    Dear Sender,

    Your email was caught in my junk filter and could not be delivered.
    This is an automated response. Please do not reply to this email.
    If you believe this is a mistake please open an issue at https://github.com/jimchen2/docker-self-host/issues

    Best regards,
    Jim Chen
    """

    bounce_html = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <script src="https://cdn.tailwindcss.com"></script>
    </head>
    <body class="bg-gray-100 font-sans">
        <div class="max-w-2xl mx-auto my-8 p-6 bg-white rounded-lg shadow-md">
            <h1 class="text-2xl font-bold text-gray-800 mb-4">Email Blocked</h1>
            <p class="text-gray-600 mb-4">Dear Sender,</p>
            <p class="text-gray-600 mb-4">Your email was caught in my junk filter and could not be delivered.</p>
            <p class="text-gray-600 mb-4">This is an automated response. Please do not reply to this email.</p>
            <p class="text-gray-600 mb-4">If you believe this is a mistake, please open an issue at:</p>
            <a href="https://github.com/jimchen2/docker-self-host/issues" class="text-blue-500 hover:underline">https://github.com/jimchen2/docker-self-host/issues</a>
            <p class="text-gray-600 mt-6">Best regards,<br>Jim Chen</p>
        </div>
    </body>
    </html>
    """

    bounce_msg.attach(MIMEText(bounce_text, 'plain'))
    bounce_msg.attach(MIMEText(bounce_html, 'html'))

    send_email(bounce_msg)

def send_email(msg):
    try:
        response = ses.send_raw_email(
            Source=msg['From'],
            Destinations=[msg['To']],
            RawMessage={'Data': msg.as_string()}
        )
        logger.info(f"Email sent successfully. MessageId: {response['MessageId']}")
    except Exception as e:
        logger.error(f"Error sending email: {str(e)}")
        raise