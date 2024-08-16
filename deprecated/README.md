
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