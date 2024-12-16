## All Services

- AWS: Bedrock, EC2
- Cloudflare (Free): R2, DNS

## PLEASE USE INTERNAL PRIVATE IP FOR DATABASE TO AVOID PUBLIC IP FEES

Ports: 443(https), 80(http), 22(ssh), 27017(mongo)

## Nginx

`nginx` files are in `/etc/nginx/sites-available/`

```
sudo ln -sf /etc/nginx/sites-available/jimchen.me.conf /etc/nginx/sites-enabled/
sudo ln -sf /etc/nginx/sites-available/llm.jimchen.me.conf /etc/nginx/sites-enabled/
```

## Cert and Private Key

I use Cloudflare certs and place them in

```
ssl_certificate /etc/cloudflare/jimchen.me/cert.pem;
ssl_certificate_key /etc/cloudflare/jimchen.me/privatekey.pem;
```

## [vercel-bedrock](https://github.com/jimchen2/vercel-bedrock)

url: [llm.jimchen.me](https://llm.jimchen.me)

Using us-east-1 Anthropic

## [jimchen.me](https://github.com/jimchen2/My-Website-New)

url: [jimchen.me](https://jimchen.me)