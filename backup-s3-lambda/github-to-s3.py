### DEFINE ENV VARS
### GITHUB_USERNAME
### GITHUB_TOKEN
### S3_BUCKET_NAME

import os
import shutil
import subprocess
from datetime import datetime, timedelta
import boto3
import requests

def lambda_handler(event, context):
    # Environment variables
    USERNAME = os.environ.get('GITHUB_USERNAME')
    TOKEN = os.environ.get('GITHUB_TOKEN')
    S3_BUCKET = os.environ.get('S3_BUCKET_NAME')
    TEMP_DIR = "/tmp/github_repos"

    if os.path.exists(TEMP_DIR):
        shutil.rmtree(TEMP_DIR)
    os.makedirs(TEMP_DIR)
    os.chdir(TEMP_DIR)

    s3 = boto3.client('s3')

    last_week = datetime.utcnow() - timedelta(days=7)

    # Get user's repositories
    headers = {'Authorization': f'token {TOKEN}'}
    repos_url = f'https://api.github.com/users/{USERNAME}/repos'
    response = requests.get(repos_url, headers=headers)
    repos = response.json()

    for repo in repos:
        if repo['size'] < 300000 and datetime.strptime(repo['pushed_at'], '%Y-%m-%dT%H:%M:%SZ') > last_week:
            clone_url = repo['clone_url'].replace('https://', f'https://{TOKEN}@')
            subprocess.run(['git', 'clone', '--depth', '1', clone_url, repo['name']], check=True)

    timestamp = datetime.now().strftime("%Y/%m/%d/%H%M%S")
    for root, dirs, files in os.walk(TEMP_DIR):
        for file in files:
            local_path = os.path.join(root, file)
            relative_path = os.path.relpath(local_path, TEMP_DIR)
            s3_key = f"{timestamp}/{relative_path}"
            s3.upload_file(local_path, S3_BUCKET, s3_key)

    shutil.rmtree(TEMP_DIR)

    return {
        'statusCode': 200,
        'body': f"GitHub repositories backed up to s3://{S3_BUCKET}/{timestamp}/"
    }