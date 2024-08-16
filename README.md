## Install latest docker and docker compose

## Server Dashboard

[https://grafana.jimchen.me/public-dashboards/b6c9b0826c0b4af6b7bd4324618c5b95](https://grafana.jimchen.me/public-dashboards/b6c9b0826c0b4af6b7bd4324618c5b95)

### Cleaning Up

```
docker system prune -af --volumes
```

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

url: [lobe.jimchen.me](https://lobe.jimchen.me)

```
sudo docker run -d -p 3210:3210 --env-file .env --restart always --name lobe-chat lobehub/lobe-chat
sudo certbot certonly --standalone -d lobe.jimchen.me --email jimchen4214@gmail.com --non-interactive --agree-tos
sudo ln -sf /etc/nginx/sites-available/chat.jimchen.me.conf /etc/nginx/sites-enabled/
```

## [chatgpt-next-web](https://github.com/ChatGPTNextWeb/ChatGPT-Next-Web)

url: [chat.jimchen.me](https://chat.jimchen.me)

```
sudo docker run -d -p 3000:3000 --env-file .env --restart always yidadaa/chatgpt-next-web
sudo certbot certonly --standalone -d chat.jimchen.me --email jimchen4214@gmail.com --non-interactive --agree-tos
sudo ln -sf /etc/nginx/sites-available/chat.jimchen.me.conf /etc/nginx/sites-enabled/
```

## [portainer](https://github.com/portainer/portainer)

url: [portainer.jimchen.me](https://portainer.jimchen.me)

```sh
sudo docker volume create portainer_data
sudo docker run -d -p 3003:9000 --name portainer --restart=always -v /var/run/docker.sock:/var/run/docker.sock -v portainer_data:/data portainer/portainer-ce:latest
sudo certbot certonly --standalone -d portainer.jimchen.me --email jimchen4214@gmail.com --non-interactive --agree-tos
sudo ln -sf /etc/nginx/sites-available/portainer.jimchen.me.conf /etc/nginx/sites-enabled/
```

## [alist](https://github.com/alist-org/alist)

url: [bucket.jimchen.me](https://bucket.jimchen.me)

```sh
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
sudo certbot certonly --standalone -d jimchen.me --email jimchen4214@gmail.com --non-interactive --agree-tos
sudo ln -sf /etc/nginx/sites-available/jimchen.me.conf /etc/nginx/sites-enabled/
```

## [markdown-parser](https://github.com/jimchen2/markdown-parser)

url: [markdown.jimchen.me](https://markdown.jimchen.me)

```bash
# configure .env
docker run -d --restart always --env-file .env -p 3048:3000 jimchen2/markdown-parser:latest
sudo certbot certonly --standalone -d markdown.jimchen.me --email jimchen4214@gmail.com --non-interactive --agree-tos
sudo ln -sf /etc/nginx/sites-available/markdown.jimchen.me.conf /etc/nginx/sites-enabled/
```

## [task-manager-nextjs](https://github.com/jimchen2/task-manager-nextjs)

url: [task.jimchen.me](https://task.jimchen.me)

```bash
# configure .env
docker run -d --restart always --env-file .env -p 3025:3000 jimchen2/task-manager-nextjs:latest
sudo certbot certonly --standalone -d task.jimchen.me --email jimchen4214@gmail.com --non-interactive --agree-tos
sudo ln -sf /etc/nginx/sites-available/task.jimchen.me.conf /etc/nginx/sites-enabled/
```

## [nezha](https://github.com/naiba/nezha)

url: [nezha.jimchen.me](https://nezha.jimchen.me)

```bash
curl -L https://raw.githubusercontent.com/naiba/nezha/master/script/install.sh -o nezha.sh && chmod +x nezha.sh && sudo ./nezha.sh
# expose port 8008 and 5555
sudo certbot certonly --standalone -d nezha.jimchen.me --email jimchen4214@gmail.com --non-interactive --agree-tos
sudo ln -sf /etc/nginx/sites-available/nezha.jimchen.me.conf /etc/nginx/sites-enabled/
```

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

## [freshrss](https://github.com/FreshRSS/FreshRSS)

url: [feed.jimchen.me](https://feed.jimchen.me)

```
docker run -d --restart always --log-opt max-size=10m \
  -p 8092:80 \
  -e TZ=Europe/Paris \
  -e 'CRON_MIN=1,31' \
  -v freshrss_data:/var/www/FreshRSS/data \
  -v freshrss_extensions:/var/www/FreshRSS/extensions \
  --name freshrss \
  freshrss/freshrss
sudo certbot certonly --standalone -d feed.jimchen.me --email jimchen4214@gmail.com --non-interactive --agree-tos
sudo ln -sf /etc/nginx/sites-available/feed.jimchen.me.conf /etc/nginx/sites-enabled/
```

## [linktree](https://github.com/jimchen2/linktree)

url: [link.jimchen.me](https://link.jimchen.me)

```bash
docker run -d --restart always -p 3069:3000 jimchen2/linktree:latest
sudo certbot certonly --standalone -d link.jimchen.me --email jimchen4214@gmail.com --non-interactive --agree-tos
sudo ln -sf /etc/nginx/sites-available/link.jimchen.me.conf /etc/nginx/sites-enabled/
```

## [gitea](https://github.com/go-gitea/gitea)

url: [git.jimchen.me](https://git.jimchen.me)

```bash
sudo docker-compose up -d
sudo certbot certonly --standalone -d git.jimchen.me --email jimchen4214@gmail.com --non-interactive --agree-tos
sudo ln -sf /etc/nginx/sites-available/git.jimchen.me.conf /etc/nginx/sites-enabled/
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
sudo certbot certonly --standalone -d grafana.jimchen.me --email jimchen4214@gmail.com --non-interactive --agree-tos
sudo ln -sf /etc/nginx/sites-available/grafana.jimchen.me.conf /etc/nginx/sites-enabled/
```

## [metabase](https://github.com/metabase/metabase/)

url: [metabase.jimchen.me](https://metabase.jimchen.me)

```bash
# configure docker-compose
docker-compose up -d
sudo certbot certonly --standalone -d metabase.jimchen.me --email jimchen4214@gmail.com --non-interactive --agree-tos
sudo ln -sf /etc/nginx/sites-available/metabase.jimchen.me.conf /etc/nginx/sites-enabled/
```

## [mastodon](https://github.com/mastodon/mastodon/)

url: [mastodon.jimchen.me](https://mastodon.jimchen.me)

See folder for more

## [peertube](https://github.com/Chocobozzz/PeerTube/)

url: [peertube.jimchen.me](https://peertube.jimchen.me)

See folder for more

## Database

### [mongodb](https://github.com/mongodb/mongo)

See mongo folder

## S3 Lambda Functions

1. Monitor, ping websites to see if its up
2. Backup MongoDB to S3 every 30 minutes
3. Backup Github to S3 every week

## Restore Glacier Objects

1. Get objects and classes in json from a bucket
2. Start restoring job for each Glacier Object
3. Restore like normal objects

## Email Server

See mail-lambda for setting up
