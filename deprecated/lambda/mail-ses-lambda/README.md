# Email Setup

## Domain Configuration

- IMAP: mail.jimchen.me
- General: jimchen.me

## Process Flow (Asynchronous)

This is done in order

1. Save message to S3
2. Process the message
3. Deliver the message

## Event Rules

1. Save in S3 raw(Configure only `info@jimchen.me` to receive emails please)
2. Workmail integration(this is workmail IMAP, not for SES)

## Lambda Configuration

- Don't trigger Lambda in Mail receiving, only Trigger it with S3
- Set S3 notifications to trigger Lambda function(Please use prefix otherwise it will cause a bad loop)
- Remove WorkMail from suppression list
- Preprocess Emails and filter using python scripts
- Forward to IMAP server
- Save message in S3 with prefix: yyyy/mm/dd/hhmmss + attachment and message

## Thunderbird Configuration

### Inbound (IMAP)

- Server: imap.mail.us-east-1.awsapps.com
- Port: 993
- Security: SSL
- Username: Full email (IMAP email, not SES)
- Password: WorkMail password

### Outbound (SMTP)

- Server: email-smtp.us-east-1.amazonaws.com
- Port: 465
- Security: TLS
- Username: IMAP user access key
- Password: IMAP user secret key
