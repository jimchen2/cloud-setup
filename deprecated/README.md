
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
