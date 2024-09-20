The previous setup was too confusing, too complex, and caused frequent errors, so like right now I am using a simpler setup

SMTP server is the same. Basically update all the records in Route 53.

In the "email receiving"

Then add the "backup to s3" in the rule.

### Outbound (SMTP)

- Server: email-smtp.us-east-1.amazonaws.com
- Port: 465
- Security: SSL/TLS

SES damn doesn't allow email forwarding, so we use workmail

We integrate workmail with SES

It integrates automatically.

After we integrate with workmail basically what we do is set up email forwarding. Thank you! Then we can use Gmail webmail and Gmail mobile client.