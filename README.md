## Install latest docker and docker compose

### Arm on AWS

```
sudo curl -L "https://github.com/docker/compose/releases/download/v2.27.1/docker-compose-linux-armv7" -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose
```

### x86

```
sudo curl -L "https://github.com/docker/compose/releases/download/v2.27.1/docker-compose-linux-x86_64" -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose
```

```
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg
echo \
"deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu \
$(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null

sudo apt-get update
sudo apt-get install docker-ce
sudo systemctl enable --now docker
```

## `nginx` files are in `/etc/nginx/sites-available/`

## [lobe-chat](https://github.com/lobehub/lobe-chat)

url: [lobe.jimchen.me](lobe.jimchen.me)

```
sudo docker run -d -p 3210:3210 --env-file .env --restart always --name lobe-chat lobehub/lobe-chat
sudo certbot certonly --standalone -d lobe.jimchen.me --email jimchen4214@gmail.com --non-interactive --agree-tos
sudo ln -sf /etc/nginx/sites-available/chat.jimchen.me.conf /etc/nginx/sites-enabled/
```

## [chatgpt-next-web](https://github.com/ChatGPTNextWeb/ChatGPT-Next-Web)

url: [chat.jimchen.me](https://chat.jimchen.me)

```
sudo docker run -d -p 3000:3000 --env-file .env.next --restart always yidadaa/chatgpt-next-web
sudo certbot certonly --standalone -d chat.jimchen.me --email jimchen4214@gmail.com --non-interactive --agree-tos
sudo ln -sf /etc/nginx/sites-available/chat.jimchen.me.conf /etc/nginx/sites-enabled/
```

## [vaultwarden](https://github.com/dani-garcia/vaultwarden)

url: [vault.jimchen.me](https://vault.jimchen.me)

```
sudo docker run -d --name vaultwarden -v /vw-data/:/data/ --restart always -p 3001:80 vaultwarden/server:latest
sudo certbot certonly --standalone -d vault.jimchen.me --email jimchen4214@gmail.com --non-interactive --agree-tos
sudo ln -sf /etc/nginx/sites-available/vault.jimchen.me.conf /etc/nginx/sites-enabled/
```

## [uptime-kuma](https://github.com/louislam/uptime-kuma)

url: [status.jimchen.me](https://status.jimchen.me)

```
sudo docker run -d --restart=always -p 3002:3001 -v uptime-kuma:/app/data --name uptime-kuma louislam/uptime-kuma:1
sudo certbot certonly --standalone -d status.jimchen.me --email jimchen4214@gmail.com --non-interactive --agree-tos
sudo ln -sf /etc/nginx/sites-available/status.jimchen.me.conf /etc/nginx/sites-enabled/
```

## [immich](https://github.com/immich-app/immich)

url: [immich.jimchen.me](https://immich.jimchen.me)

```sh
mkdir ./immich-app
cd ./immich-app

# wget -O docker-compose.yml https://github.com/immich-app/immich/releases/latest/download/docker-compose.yml
#wget -O .env https://github.com/immich-app/immich/releases/latest/download/example.env

sudo docker-compose up -d
sudo certbot certonly --standalone -d immich.jimchen.me --email jimchen4214@gmail.com --non-interactive --agree-tos
sudo ln -sf /etc/nginx/sites-available/immich.jimchen.me.conf /etc/nginx/sites-enabled/
```

## [portainer](https://github.com/portainer/portainer)

url: [portainer.jimchen.me](https://portainer.jimchen.me)

```
sudo docker volume create portainer_data
sudo docker run -d -p 3003:9000 --name portainer --restart=always -v /var/run/docker.sock:/var/run/docker.sock -v portainer_data:/data portainer/portainer-ce:latest
sudo certbot certonly --standalone -d portainer.jimchen.me --email jimchen4214@gmail.com --non-interactive --agree-tos
sudo ln -sf /etc/nginx/sites-available/portainer.jimchen.me.conf /etc/nginx/sites-enabled/
```

## [grafana](https://github.com/grafana/grafana)

url: [grafana.jimchen.me](https://grafana.jimchen.me)

```
docker run -d -p 3004:3000 --restart always --name=grafana grafana/grafana-enterprise
sudo certbot certonly --standalone -d grafana.jimchen.me --email jimchen4214@gmail.com --non-interactive --agree-tos
sudo ln -sf /etc/nginx/sites-available/grafana.jimchen.me.conf /etc/nginx/sites-enabled/
```

## [prometheus](https://github.com/prometheus/prometheus)

url: [prometheus.jimchen.me](https://prometheus.jimchen.me)

```
sudo docker run --name prometheus --restart always -d -p 9090:9090 prom/prometheus
sudo certbot certonly --standalone -d prometheus.jimchen.me --email jimchen4214@gmail.com --non-interactive --agree-tos
sudo ln -sf /etc/nginx/sites-available/prometheus.jimchen.me.conf /etc/nginx/sites-enabled/
```

## [stash](https://github.com/stashapp/stash)

url: [stash.jimchen.me](https://stash.jimchen.me)

```
sudo mkdir stashapp && cd stashapp
curl -o docker-compose.yml https://raw.githubusercontent.com/stashapp/stash/develop/docker/production/docker-compose.yml
sudo docker-compose up -d
sudo certbot certonly --standalone -d stash.jimchen.me --email jimchen4214@gmail.com --non-interactive --agree-tos
sudo ln -sf /etc/nginx/sites-available/stash.jimchen.me.conf /etc/nginx/sites-enabled/
```

## [mongodb]

url: [mongo.jimchen.me](https://mongo.jimchen.me)

```bash
# add mongod.conf, dockercompose
docker-compose up -d
# expose port 27017
# mongosh "mongodb://admin:[]@3.228.73.172:27017/" --authenticationDatabase admin
# connecting admin only works when specifying admin ?authSource=admin
```

## [alist](https://github.com/alist-org/alist)

url: [bucket.jimchen.me](https://bucket.jimchen.me)

```
docker run -d --restart=always -v /etc/alist:/opt/alist/data -p 5244:5244 -e PUID=0 -e PGID=0 -e UMASK=022 --name="alist" xhofe/alist:latest
docker exec -it alist ./alist admin set password
sudo certbot certonly --standalone -d bucket.jimchen.me --email jimchen4214@gmail.com --non-interactive --agree-tos
sudo ln -sf /etc/nginx/sites-available/bucket.jimchen.me.conf /etc/nginx/sites-enabled/
```

## [jimchen.me](https://github.com/jimchen2/My-Website-New)

url: [jimchen.me](https://jimchen.me)

```bash
# configure .env
# double quote leads to errors
docker run -d --restart always --env-file .env -p 3010:3000 jimchen2/my-website:latest
# docker run -d --restart always --env-file .env -p 3011:3000 jimchen2/my-website-zh:latest
sudo certbot certonly --standalone -d jimchen.me --email jimchen4214@gmail.com --non-interactive --agree-tos
sudo ln -sf /etc/nginx/sites-available/jimchen.me.conf /etc/nginx/sites-enabled/
```

## [task-manager-nextjs](https://github.com/jimchen2/task-manager-nextjs)

url: [task.jimchen.me](https://task.jimchen.me)

```bash
# configure .env
docker run -d --restart always --env-file .env -p 3025:3000 jimchen2/task-manager-nextjs:latest
sudo certbot certonly --standalone -d task.jimchen.me --email jimchen4214@gmail.com --non-interactive --agree-tos
sudo ln -sf /etc/nginx/sites-available/task.jimchen.me.conf /etc/nginx/sites-enabled/
```

## [markdown-parser](https://github.com/jimchen2/markdown-parser)

url: [markdown.jimchen.me](https://markdown.jimchen.me)

```bash
# configure .env
docker run -d --restart always --env-file .env -p 3025:3000 jimchen2/markdown-parser:latest
sudo certbot certonly --standalone -d markdown.jimchen.me --email jimchen4214@gmail.com --non-interactive --agree-tos
sudo ln -sf /etc/nginx/sites-available/markdown.jimchen.me.conf /etc/nginx/sites-enabled/
```

## [nocodb](https://github.com/nocodb/nocodb)

url: [nocodb.jimchen.me](https://nocodb.jimchen.me)

```bash
# configure docker-compose.yml
docker-compose up -d
sudo certbot certonly --standalone -d nocodb.jimchen.me --email jimchen4214@gmail.com --non-interactive --agree-tos
sudo ln -sf /etc/nginx/sites-available/nocodb.jimchen.me.conf /etc/nginx/sites-enabled/
```

## [actual](https://github.com/actualbudget/actual)

url: [actual.jimchen.me](https://actual.jimchen.me)

```

docker run --pull=always --restart=unless-stopped -d -p 3037:5006 -v /data:/data --name actual-server actualbudget/actual-server:latest
sudo certbot certonly --standalone -d actual.jimchen.me --email jimchen4214@gmail.com --non-interactive --agree-tos
sudo ln -sf /etc/nginx/sites-available/actual.jimchen.me.conf /etc/nginx/sites-enabled/
```

## [monica](https://github.com/monicahq/monica)

url: [monica.jimchen.me](http://monica.jimchen.me)

```
docker-compose up -d
sudo certbot certonly --standalone -d monica.jimchen.me --email jimchen4214@gmail.com --non-interactive --agree-tos
sudo ln -sf /etc/nginx/sites-available/monica.jimchen.me.conf /etc/nginx/sites-enabled/
```




