import json
import boto3
import email
from datetime import datetime
import os
from botocore.exceptions import ClientError

def lambda_handler(event, context):
    # Main handler function
    return receive_email(event)

def receive_email(event):
    # Extract the message from the event
    message = event['Records'][0]['ses']['mail']
    
    # Filter the email
    if filter_email(message):
        return bounce(message)
    else:
        save_to_s3(message)
        forward(message)
    
    return {
        'statusCode': 200,
        'body': json.dumps('Email processed successfully')
    }

def filter_email(message):
    # Implement your spam filtering logic here
    # For example, you could check for specific keywords in the subject or body
    subject = message.get('commonHeaders', {}).get('subject', '').lower()
    spam_keywords = ['viagra', 'lottery', 'winner', 'inheritance']
    
    return any(keyword in subject for keyword in spam_keywords)

def bounce(message):
    bounce_message = "Your email has been classified as junk and cannot be delivered."
    sender = message['source']
    
    ses_client = boto3.client('ses')
    
    try:
        response = ses_client.send_email(
            Source=os.environ['FORWARD_EMAIL'],
            Destination={
                'ToAddresses': [sender]
            },
            Message={
                'Subject': {
                    'Data': 'Mail Delivery Failed'
                },
                'Body': {
                    'Text': {
                        'Data': bounce_message
                    }
                }
            }
        )
    except ClientError as e:
        print(e.response['Error']['Message'])
    else:
        print(f"Bounce message sent to {sender}")
    
    return {
        'statusCode': 200,
        'body': json.dumps('Email bounced')
    }

def save_to_s3(message):
    s3_client = boto3.client('s3')
    bucket_name = os.environ['S3_BUCKET_NAME']
    
    # Generate a unique key based on timestamp
    timestamp = datetime.now().strftime("%Y/%m/%d/%H%M%S")
    message_id = message['messageId']
    key = f"{timestamp}_{message_id}.json"
    
    # Save the message to S3
    try:
        s3_client.put_object(
            Bucket=bucket_name,
            Key=key,
            Body=json.dumps(message)
        )
        print(f"Email saved to S3: {key}")
    except ClientError as e:
        print(f"Error saving to S3: {e}")

def forward(message):
    ses_client = boto3.client('ses')
    forward_email = os.environ['FORWARD_EMAIL']
    
    # Construct the forwarded message
    original_subject = message['commonHeaders']['subject']
    original_sender = message['source']
    
    try:
        response = ses_client.send_email(
            Source=os.environ['FORWARD_EMAIL'],
            Destination={
                'ToAddresses': [forward_email]
            },
            Message={
                'Subject': {
                    'Data': f"Fwd: {original_subject}"
                },
                'Body': {
                    'Text': {
                        'Data': f"Forwarded message from {original_sender}\n\n{json.dumps(message, indent=2)}"
                    }
                }
            }
        )
    except ClientError as e:
        print(e.response['Error']['Message'])
    else:
        print(f"Email forwarded to {forward_email}")

def aws_ses_smtp():
    # Get environment variables for SMTP configuration
    smtp_username = os.environ['SMTP_USERNAME']
    smtp_password = os.environ['SMTP_PASSWORD']
    smtp_host = os.environ['SMTP_HOST']
    smtp_port = int(os.environ['SMTP_PORT'])
    
    return {
        'username': smtp_username,
        'password': smtp_password,
        'host': smtp_host,
        'port': smtp_port
    }