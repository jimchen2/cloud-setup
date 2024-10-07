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

