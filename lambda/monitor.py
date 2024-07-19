import boto3
import urllib3
import json
from datetime import datetime

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
    
    for endpoint in endpoints:
        try:
            response = http.request('GET', endpoint['url'], timeout=5.0)
            status = response.status
        except urllib3.exceptions.RequestError:
            status = 'Error'
        
        result = {
            'name': endpoint['name'],
            'url': endpoint['url'],
            'status': status,
            'timestamp': current_time.isoformat()
        }
        
        # Create a unique key for each service
        service_name = endpoint['name'].lower().replace(' ', '_')
        key = f'logs/{service_name}/{current_time.strftime("%Y/%m/%d/%H/%M")}.json'
        
        # Write result to S3
        s3.put_object(
            Bucket=bucket_name,
            Key=key,
            Body=json.dumps(result)
        )
    
    return {
        'statusCode': 200,
        'body': json.dumps('URL checks completed successfully')
    }