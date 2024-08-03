## First create a layer with Python Libraries, zip it to s3, then add it to RunTime
## Make Sure the python local and Lambda versions match
## Change Function Policies to Write to S3
## Add Git Layer `arn:aws:lambda:us-east-1:553035198032:layer:git-lambda2:8`
## Configure Env Vars and Increase Time to Run
## Then Configure the CloudEvent to Run it Periodically