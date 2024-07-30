import os
import boto3
from pymongo import MongoClient
from bson.json_util import dumps
from datetime import datetime
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
    
    return {
        'statusCode': 200,
        'body': f"Backup uploaded to s3://{s3_bucket}/{s3_key}"
    }
