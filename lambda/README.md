## First create a layer with Python Libraries, zip it to s3, then add it to RunTime
## Make Sure the python local and Lambda versions match
## Change Function Policies to Write to S3
## Add Git Layer `arn:aws:lambda:us-east-1:553035198032:layer:git-lambda2:8`
## Configure Env Vars and Increase Time to Run
## Then Configure the CloudEvent to Run it Periodically

## Extracted Lambda is like this(after extraction)

```
user@ubuntu ~/D/python> ls
bin
bson
certifi
certifi-2024.7.4.dist-info
cffi
cffi-1.16.0.dist-info
_cffi_backend.cpython-311-x86_64-linux-gnu.so
charset_normalizer
charset_normalizer-3.3.2.dist-info
cryptography
cryptography-42.0.8.dist-info
deprecated
Deprecated-1.2.14.dist-info
dns
dnspython-2.6.1.dist-info
github
gridfs
idna
idna-3.7.dist-info
jwt
nacl
__pycache__
pycparser
```



- GithubToS3Weekly
- Monitor: Every 30 minutes check website status
- MongoToS3: Every 30 minutes backup MongoDB



## S3 Lambda Functions

1. Monitor, ping websites to see if its up
2. Backup MongoDB to S3 every 30 minutes
3. Backup Github to S3 every week
