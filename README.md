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


## [nextjs-tube](https://github.com/jimchen2/nextjs-tube)

url: [tube.jimchen.me](https://tube.jimchen.me)

```
mkdir nextjs-tube && cd nextjs-tube 
curl -o docker-compose.yml https://raw.githubusercontent.com/jimchen2/nextjs-tube/main/docker-compose.yml
curl -o .env https://raw.githubusercontent.com/jimchen2/nextjs-tube/main/.env.example
# configure .env, add amazon s3 access keys
docker-compose up -d
sudo certbot certonly --standalone -d tube.jimchen.me --email jimchen4214@gmail.com --non-interactive --agree-tos
sudo ln -sf /etc/nginx/sites-available/tube.jimchen.me.conf /etc/nginx/sites-enabled/
```

## [s3-public-index](https://github.com/jimchen2/s3-public-index)

url: [bucket.jimchen.me](https://bucket.jimchen.me)

```
mkdir s3-public-index && cd s3-public-index
# configure .env
docker run -d --restart always --env-file .env -p 1241:3000 jimchen2/s3-public-index:latest 
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

