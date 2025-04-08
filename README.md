- `jimchen.me` is hosted on vercel, and uses MongoDB atlas, Vercel Redis
- `feed.jimchen.me` is a FreshRSS instance hosted on Digital Ocean

## `nginx`

```sh
# copy the nginx config to sites-available
rm /etc/nginx/sites-enabled/default
sudo ln -sf /etc/nginx/sites-available/feed.jimchen.me.conf /etc/nginx/sites-enabled/
```

## Certbot

```
sudo mkdir -p /var/www/html
sudo chown -R www-data:www-data /var/www/html
sudo certbot certonly --webroot -w /var/www/html -d feed.jimchen.me
```

## RSS

```
docker run -d --restart always --log-opt max-size=10m -p 3001:80 -e TZ=Europe/Paris -e 'CRON_MIN=1,31' -v freshrss_data:/var/www/FreshRSS/data -v freshrss_extensions:/var/www/FreshRSS/extensions --name freshrss freshrss/freshrss
```
