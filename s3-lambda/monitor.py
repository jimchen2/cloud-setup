import boto3
import urllib3
import json
from datetime import datetime, timedelta
import csv
import io
import os

def lambda_handler(event, context):
    s3 = boto3.client('s3')
    bucket_name = os.environ.get('S3_BUCKET_NAME')
    
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
        {"name": "Metabase", "url": "https://metabase.jimchen.me"}
    ]

    
    http = urllib3.PoolManager()
    current_time = datetime.utcnow()
    
    results = []
    for endpoint in endpoints:
        try:
            response = http.request('GET', endpoint['url'], timeout=15.0)
            status = response.status
            up_down = 'up' if 200 <= status < 400 else 'down'
        except urllib3.exceptions.RequestError:
            status = 'Error'
            up_down = 'down'
        
        result = {
            'name': endpoint['name'],
            'url': endpoint['url'],
            'status': status,
            'up_down': up_down,
            'timestamp': current_time.isoformat()
        }
        results.append(result)
    
    # Create a folder structure and file for this run
    timestamp = current_time.strftime("%Y/%m/%d/%H%M%S")
    key = f'{timestamp}_status.json'
    
    # Write results to S3
    s3.put_object(
        Bucket=bucket_name,
        Key=key,
        Body=json.dumps(results)
    )
    
    # Update the latest status CSV
    update_latest_csv(s3, bucket_name, results)
    
    # Update the daily uptime CSV
    update_daily_uptime_csv(s3, bucket_name, current_time)
    
    return {
        'statusCode': 200,
        'body': json.dumps(results)
    }

def update_latest_csv(s3, bucket_name, results):
    csv_key = 'latest_status.csv'
    
    output = io.StringIO()
    writer = csv.DictWriter(output, fieldnames=['name', 'url', 'status', 'up_down', 'timestamp'])
    writer.writeheader()
    writer.writerows(results)
    
    csv_content = output.getvalue()
    
    s3.put_object(
        Bucket=bucket_name,
        Key=csv_key,
        Body=csv_content
    )

def update_daily_uptime_csv(s3, bucket_name, current_time):
    csv_key = 'last_seven_days_status.csv'
    
    # Get all JSON files from the last 7 days
    all_results = []
    end_date = current_time.date()
    start_date = end_date - timedelta(days=6)  # 7 days including today

    current_date = start_date
    while current_date <= end_date:
        prefix = current_date.strftime("%Y/%m/%d/")
        response = s3.list_objects_v2(
            Bucket=bucket_name,
            Prefix=prefix,
            MaxKeys=10000
        )
        
        for obj in response.get('Contents', []):
            if obj['Key'].endswith('status.json'):
                file_content = s3.get_object(Bucket=bucket_name, Key=obj['Key'])['Body'].read().decode('utf-8')
                all_results.extend(json.loads(file_content))
        
        current_date += timedelta(days=1)
    
    # Calculate daily uptime for each service
    daily_uptime = {}
    for result in all_results:
        date = datetime.fromisoformat(result['timestamp']).date()
        name = result['name']
        up_down = result['up_down']
        
        if date not in daily_uptime:
            daily_uptime[date] = {}
        if name not in daily_uptime[date]:
            daily_uptime[date][name] = {'up': 0, 'down': 0}
        
        daily_uptime[date][name][up_down] += 1
    
    # Calculate uptime percentage
    uptime_results = []
    for date, services in daily_uptime.items():
        for name, counts in services.items():
            total = counts['up'] + counts['down']
            uptime_percentage = (counts['up'] / total) * 100 if total > 0 else 0
            uptime_results.append({
                'date': date.isoformat(),
                'name': name,
                'uptime_percentage': round(uptime_percentage, 2)
            })
    
    # Sort results by date and name
    uptime_results.sort(key=lambda x: (x['date'], x['name']))
    
    # Write updated results to CSV
    output = io.StringIO()
    writer = csv.DictWriter(output, fieldnames=['date', 'name', 'uptime_percentage'])
    writer.writeheader()
    writer.writerows(uptime_results)
    
    csv_content = output.getvalue()
    
    # Upload CSV to S3
    s3.put_object(
        Bucket=bucket_name,
        Key=csv_key,
        Body=csv_content
    )
