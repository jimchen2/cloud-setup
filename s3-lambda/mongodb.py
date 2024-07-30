import os
import boto3
from pymongo import MongoClient
from bson.json_util import dumps
from datetime import datetime, timedelta
from pymongo.errors import OperationFailure

def lambda_handler(event, context):
    mongo_uri = os.environ.get('MONGODB_URI')
    s3_bucket = os.environ.get('S3_BUCKET_NAME')

    backup_file = "/tmp/mongodb_backup.json"
    
    # MongoDB backup
    client = MongoClient(mongo_uri)
    with open(backup_file, 'w') as f:
        for db in client.list_database_names():
            if db not in ['admin', 'local', 'config']:  # Skip system databases
                for collection in client[db].list_collection_names():
                    try:
                        f.write(f"Database: {db}, Collection: {collection}\n")
                        f.write(dumps(client[db][collection].find()) + "\n")
                    except OperationFailure as e:
                        f.write(f"Error accessing {db}.{collection}: {str(e)}\n")
    
    # Upload to S3
    s3 = boto3.client('s3')
    current_time = datetime.now()
    timestamp = current_time.strftime("%Y/%m/%d/%H%M%S")
    
    # Check if time is between 00:00 and 01:00
    if current_time.hour == 0:
        s3_key = f"full/{timestamp}/backup.json"
    else:
        s3_key = f"{timestamp}/backup.json"
    
    s3.upload_file(
        backup_file, 
        s3_bucket, 
        s3_key,
        ExtraArgs={'StorageClass': 'STANDARD_IA'}
    )
    
    # Remove old shallow backups
    remove_old_backups(s3, s3_bucket)
    
    return {
        'statusCode': 200,
        'body': f"Backup uploaded to s3://{s3_bucket}/{s3_key}"
    }

def remove_old_backups(s3, bucket_name):
    # Get current date
    current_date = datetime.now()
    one_week_ago = current_date - timedelta(days=7)

    # List objects in the bucket
    paginator = s3.get_paginator('list_objects_v2')
    pages = paginator.paginate(Bucket=bucket_name)

    for page in pages:
        for obj in page.get('Contents', []):
            key = obj['Key']
            # Skip full backups
            if key.startswith('full/'):
                continue
            
            # Extract date from the key
            try:
                backup_date = datetime.strptime(key[:10], "%Y/%m/%d")
                if backup_date < one_week_ago:
                    s3.delete_object(Bucket=bucket_name, Key=key)
                    print(f"Deleted old backup: {key}")
            except ValueError:
                continue
