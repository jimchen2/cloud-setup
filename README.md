## All Services

AWS

- Bedrock
- EC2

Cloudflare

- R2
- DNS

## PLEASE USE INTERNAL PRIVATE IP FOR DATABASE TO AVOID PUBLIC IP FEES

Ports: 443(https), 80(http), 22(ssh), 5432(psql), 27017(mongo), 5555(nezha monitoring)

### Cleaning Up

```
docker system prune -af --volumes
```

## Nginx

`nginx` files are in `/etc/nginx/sites-available/`

```
sudo ln -sf /etc/nginx/sites-available/jimchen.me.conf /etc/nginx/sites-enabled/
```

## Cert and Private Key

I use Cloudflare certs and place them in

```
ssl_certificate /etc/cloudflare/jimchen.me/cert.pem;
ssl_certificate_key /etc/cloudflare/jimchen.me/privatekey.pem;
```

## [vercel-bedrock](https://github.com/jimchen2/vercel-bedrock)

url: [llm.jimchen.me](https://llm.jimchen.me)

## [jimchen.me](https://github.com/jimchen2/My-Website-New)

url: [jimchen.me](https://jimchen.me)

## [markdown-parser](https://github.com/jimchen2/markdown-parser)

url: [markdown.jimchen.me](https://markdown.jimchen.me)

## [linktree](https://github.com/jimchen2/linktree)

url: [link.jimchen.me](https://link.jimchen.me)

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

## [alist](https://github.com/alist-org/alist)

url: [bucket.jimchen.me](https://bucket.jimchen.me)

```sh
docker run -d --restart=always -v /etc/alist:/opt/alist/data -p 5244:5244 -e PUID=0 -e PGID=0 -e UMASK=022 --name="alist" xhofe/alist:latest
docker exec -it alist ./alist admin set password
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
