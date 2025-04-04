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

## [roundcube](https://roundcube.net/)

url: [m.jimchen.me](https://m.jimchen.me)

Enter the IMAP username and password to login

Use ssl

```
docker run -d \
  --restart always\
  -e ROUNDCUBEMAIL_DEFAULT_HOST=ssl://imap.mail.us-east-1.awsapps.com \
  -e ROUNDCUBEMAIL_DEFAULT_PORT=993 \
  -e ROUNDCUBEMAIL_SMTP_SERVER=ssl://smtp.mail.us-east-1.awsapps.com \
  -e ROUNDCUBEMAIL_SMTP_PORT=465 \
  -p 2948:80 \
  --name roundcube \
  roundcube/roundcubemail
```

## [alist](https://github.com/alist-org/alist)

url: [bucket.jimchen.me](https://bucket.jimchen.me)

```sh
docker run -d --restart=always -v /etc/alist:/opt/alist/data -p 5244:5244 -e PUID=0 -e PGID=0 -e UMASK=022 --name="alist" xhofe/alist:latest
docker exec -it alist ./alist admin set password
```

## [markdown-parser](https://github.com/jimchen2/markdown-parser)

url: [markdown.jimchen.me](https://markdown.jimchen.me)

## [linktree](https://github.com/jimchen2/linktree)

url: [link.jimchen.me](https://link.jimchen.me)

## [stirling-pdf](https://github.com/Stirling-Tools/Stirling-PDF)

url: [pdf.jimchen.me](https://pdf.jimchen.me)

```bash
docker run -d --restart always \
  -p 8033:8080 \
  -v ./logs:/logs \
  -e DOCKER_ENABLE_SECURITY=false \
  -e LANGS=en_GB \
  --name stirling-pdf \
  frooodle/s-pdf:latest
sudo certbot certonly --standalone -d pdf.jimchen.me --email jimchen4214@gmail.com --non-interactive --agree-tos
sudo ln -sf /etc/nginx/sites-available/pdf.jimchen.me.conf /etc/nginx/sites-enabled/
```

## [metabase](https://github.com/metabase/metabase/)

Metabase uses too much ram

url: [metabase.jimchen.me](https://metabase.jimchen.me)

```bash
# configure docker-compose
# limit its memory usage
docker-compose up -d
sudo certbot certonly --standalone -d metabase.jimchen.me --email jimchen4214@gmail.com --non-interactive --agree-tos
sudo ln -sf /etc/nginx/sites-available/metabase.jimchen.me.conf /etc/nginx/sites-enabled/
```

## [task-manager-nextjs](https://github.com/jimchen2/task-manager-nextjs)

url: [task.jimchen.me](https://task.jimchen.me)

```bash
# configure .env
docker run -d --restart always --env-file .env -p 3025:3000 jimchen2/task-manager-nextjs:latest
sudo certbot certonly --standalone -d task.jimchen.me --email jimchen4214@gmail.com --non-interactive --agree-tos
sudo ln -sf /etc/nginx/sites-available/task.jimchen.me.conf /etc/nginx/sites-enabled/
```

## [vaultwarden](https://github.com/dani-garcia/vaultwarden)

```
sudo docker run -d --name vaultwarden -v /vw-data/:/data/ --restart always -p 3001:80 vaultwarden/server:latest
sudo certbot certonly --standalone -d vault.jimchen.me --email jimchen4214@gmail.com --non-interactive --agree-tos
sudo ln -sf /etc/nginx/sites-available/vault.jimchen.me.conf /etc/nginx/sites-enabled/
```

## [uptime-kuma](https://github.com/louislam/uptime-kuma)

```
sudo docker run -d --restart=always -p 3002:3001 -v uptime-kuma:/app/data --name uptime-kuma louislam/uptime-kuma:1
sudo certbot certonly --standalone -d status.jimchen.me --email jimchen4214@gmail.com --non-interactive --agree-tos
sudo ln -sf /etc/nginx/sites-available/status.jimchen.me.conf /etc/nginx/sites-enabled/
```

## [immich](https://github.com/immich-app/immich)

```sh
mkdir ./immich-app
cd ./immich-app

# wget -O docker-compose.yml https://github.com/immich-app/immich/releases/latest/download/docker-compose.yml
#wget -O .env https://github.com/immich-app/immich/releases/latest/download/example.env

sudo docker-compose up -d
sudo certbot certonly --standalone -d immich.jimchen.me --email jimchen4214@gmail.com --non-interactive --agree-tos
sudo ln -sf /etc/nginx/sites-available/immich.jimchen.me.conf /etc/nginx/sites-enabled/
```

## [rsshub](https://github.com/DIYgod/RSSHub)

```bash
docker run -d --name rsshub -p 1200:1200 --restart always diygod/rsshub:chromium-bundled
sudo certbot certonly --standalone -d rss.jimchen.me --email jimchen4214@gmail.com --non-interactive --agree-tos
sudo ln -sf /etc/nginx/sites-available/rss.jimchen.me.conf /etc/nginx/sites-enabled/
```

## [nocodb](https://github.com/nocodb/nocodb)

```bash
# configure docker-compose.yml
docker-compose up -d
sudo certbot certonly --standalone -d nocodb.jimchen.me --email jimchen4214@gmail.com --non-interactive --agree-tos
sudo ln -sf /etc/nginx/sites-available/nocodb.jimchen.me.conf /etc/nginx/sites-enabled/
```

## [actual](https://github.com/actualbudget/actual)

```

docker run --pull=always --restart=unless-stopped -d -p 3037:5006 -v /data:/data --name actual-server actualbudget/actual-server:latest
sudo certbot certonly --standalone -d actual.jimchen.me --email jimchen4214@gmail.com --non-interactive --agree-tos
sudo ln -sf /etc/nginx/sites-available/actual.jimchen.me.conf /etc/nginx/sites-enabled/
```

## [lobe-chat](https://github.com/lobehub/lobe-chat)

url: [lobe.jimchen.me](https://lobe.jimchen.me)

```
sudo docker run -d -p 3210:3210 --env-file .env --restart always --name lobe-chat lobehub/lobe-chat
sudo certbot certonly --standalone -d lobe.jimchen.me --email jimchen4214@gmail.com --non-interactive --agree-tos
sudo ln -sf /etc/nginx/sites-available/chat.jimchen.me.conf /etc/nginx/sites-enabled/
```

## [nezha](https://github.com/naiba/nezha)

url: [nezha.jimchen.me](https://nezha.jimchen.me)

```bash
curl -L https://raw.githubusercontent.com/naiba/nezha/master/script/install.sh -o nezha.sh && chmod +x nezha.sh && sudo ./nezha.sh
# expose port 8008 and 5555
```

## [miniflux](https://github.com/miniflux/v2)

url: [feed.jimchen.me](https://feed.jimchen.me)

```
docker run -d \
  --restart always \
  -p 8092:8080 \
  --name miniflux \
  -e DATABASE_URL="postgresql://miniflux:@:5432/miniflux?sslmode=disable" \
  -e RUN_MIGRATIONS=1 \
  -e CREATE_ADMIN=1 \
  -e ADMIN_USERNAME=admin \
  -e ADMIN_PASSWORD= \
  docker.io/miniflux/miniflux:latest
```

## [grafana](https://github.com/grafana/grafana/)

url: [grafana.jimchen.me](https://grafana.jimchen.me)

```
docker run -d \
  --name=grafana \
  --restart=always \
  -p 3088:3000 \
  -v grafana-storage:/var/lib/grafana \
  -e "GF_AWS_PROFILES=default" \
  -e "GF_AWS_default_ACCESS_KEY_ID=" \
  -e "GF_AWS_default_SECRET_ACCESS_KEY=" \
  -e "GF_AWS_default_REGION=us-east-1" \
  grafana/grafana-enterprise
```

## [chatgpt-next-web](https://github.com/ChatGPTNextWeb/ChatGPT-Next-Web)

url: [chat.jimchen.me](https://chat.jimchen.me)

env:

```
OPENAI_API_KEY=
GOOGLE_API_KEY=

CODE=
```

Then

```
sudo docker run -d -p 3000:3000 --env-file .env --restart always yidadaa/chatgpt-next-web
```

## [portainer](https://github.com/portainer/portainer)

url: [portainer.jimchen.me](https://portainer.jimchen.me)

```sh
sudo docker volume create portainer_data
sudo docker run -d -p 3003:9000 --name portainer --restart=always -v /var/run/docker.sock:/var/run/docker.sock -v portainer_data:/data portainer/portainer-ce:latest
```
