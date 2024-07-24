Use mail.jimchen.me as IMAP, and jimchen.me as a 

asynchronously(do it in order, first save to s3 then process the message then deliver)

set s3 notifications to the lambda

Also please remove the workmail from suppression

save it teh message all again in s3 please with prefix yyyy/mm/dd/hhmmss + attachment and message

Thunderbird configuration

Inbound
IMAP


Port

993


imap.mail.us-east-1.awsapps.com


SSL
username; full email


Outbound

SMTP

465
TLS

email-smtp.us-east-1.amazonaws.com

username: IMAP user access key