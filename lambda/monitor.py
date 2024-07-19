import boto3
import urllib3
import json
from datetime import datetime, timedelta
import csv
import io

def lambda_handler(event, context):
    s3 = boto3.client('s3')
    bucket_name = 'jimchen4214-status'
    
    endpoints = [
        {"name": "Lobe Chat", "url": "https://lobe.jimchen.me"},
        {"name": "ChatGPT Next Web", "url": "https://chat.jimchen.me"},
        {"name": "Vaultwarden", "url": "https://vault.jimchen.me"},
        {"name": "Uptime Kuma", "url": "https://status.jimchen.me"},
        {"name": "Immich", "url": "https://immich.jimchen.me"},
        {"name": "Portainer", "url": "https://portainer.jimchen.me"},
        {"name": "Alist", "url": "https://bucket.jimchen.me"},
        {"name": "Personal Website", "url": "https://jimchen.me"},
        {"name": "Task Manager", "url": "https://task.jimchen.me"},
        {"name": "Markdown Parser", "url": "https://markdown.jimchen.me"},
        {"name": "NocoDB", "url": "https://nocodb.jimchen.me"},
        {"name": "Actual", "url": "https://actual.jimchen.me"},
        {"name": "Nezha", "url": "https://nezha.jimchen.me"},
        {"name": "Stirling PDF", "url": "https://pdf.jimchen.me"},
        {"name": "RSSHub", "url": "https://rss.jimchen.me"},
        {"name": "FreshRSS", "url": "https://feed.jimchen.me"},
        {"name": "Linktree", "url": "https://link.jimchen.me"},
        {"name": "Gitea", "url": "https://git.jimchen.me"},
        {"name": "Grafana", "url": "https://grafana.jimchen.me"}
    ]
    
    http = urllib3.PoolManager()
    current_time = datetime.utcnow()
    
    results = []
    for endpoint in endpoints:
        try:
            response = http.request('GET', endpoint['url'], timeout=15.0)
            status = response.status
        except urllib3.exceptions.RequestError:
            status = 'Error'
        
        result = {
            'name': endpoint['name'],
            'url': endpoint['url'],
            'status': status,
            'timestamp': current_time.isoformat()
        }
        results.append(result)
    
    # Create a single file for this run
    key = f'{current_time.strftime("%Y%m%d%H%M%S")}_status.json'
    
    # Write results to S3
    s3.put_object(
        Bucket=bucket_name,
        Key=key,
        Body=json.dumps(results)
    )
    
    # Update the CSV file
    update_csv(s3, bucket_name, current_time)
    
    return {
        'statusCode': 200,
        'body': json.dumps('URL checks completed successfully')
    }

def update_csv(s3, bucket_name, current_time):
    csv_key = 'last_seven_days_status.csv'
    seven_days_ago = current_time - timedelta(days=7)
    
    # Get all JSON files from the last 7 days
    response = s3.list_objects_v2(
        Bucket=bucket_name,
        Prefix=seven_days_ago.strftime("%Y%m%d"),
        MaxKeys=10000
    )
    
    all_results = []
    for obj in response.get('Contents', []):
        if obj['Key'].endswith('_status.json'):
            file_content = s3.get_object(Bucket=bucket_name, Key=obj['Key'])['Body'].read().decode('utf-8')
            all_results.extend(json.loads(file_content))
    
    # Sort results by timestamp (newest first)
    all_results.sort(key=lambda x: x['timestamp'], reverse=True)
    
    # Write updated results to CSV
    output = io.StringIO()
    writer = csv.DictWriter(output, fieldnames=['name', 'url', 'status', 'timestamp'])
    writer.writeheader()
    writer.writerows(all_results)
    
    # Upload CSV to S3
    s3.put_object(
        Bucket=bucket_name,
        Key=csv_key,
        Body=output.getvalue()
    )