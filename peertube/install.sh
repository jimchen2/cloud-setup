# Part 1 PeerTube user
sudo useradd -m -d /var/www/peertube -s /bin/bash -p peertube peertube
sudo passwd peertube
ls -ld /var/www/peertube # Should be drwxr-xr-x
chmod 755 /var/www/peertube



# Part 2 Postgres
cd /var/www/peertube
sudo -u postgres createuser -P peertube
sudo -u postgres createdb -O peertube -E UTF8 -T template0 peertube_prod
sudo -u postgres psql -c "CREATE EXTENSION pg_trgm;" peertube_prod
sudo -u postgres psql -c "CREATE EXTENSION unaccent;" peertube_prod



# Part 3 Download
VERSION=$(curl -s https://api.github.com/repos/chocobozzz/peertube/releases/latest | grep tag_name | cut -d '"' -f 4) && echo "Latest Peertube version is $VERSION"
cd /var/www/peertube
sudo -u peertube mkdir config storage versions
sudo -u peertube chmod 750 config/
cd /var/www/peertube/versions
sudo -u peertube wget -q "https://github.com/Chocobozzz/PeerTube/releases/download/${VERSION}/peertube-${VERSION}.zip"
sudo -u peertube unzip -q peertube-${VERSION}.zip && sudo -u peertube rm peertube-${VERSION}.zip


# Part 4 Compile
cd /var/www/peertube
sudo -u peertube ln -s versions/peertube-${VERSION} ./peertube-latest
cd ./peertube-latest && sudo -H -u peertube yarn install --production --pure-lockfile

# Part 5 Config
cd /var/www/peertube
sudo -u peertube cp peertube-latest/config/default.yaml config/default.yaml
cd /var/www/peertube
sudo -u peertube cp peertube-latest/config/production.yaml.example config/production.yaml
# Then edit the config/production.yaml file according to your webserver and database configuration.
# configure
# webserver: Reverse proxy public information
# secrets: Secret strings you must generate manually (PeerTube version >= 5.0)
# database: PostgreSQL settings
# redis: Redis settings
# smtp: AWS SES
# admin.email: To correctly fill root user email
# object storage buckets
# Whisper engine


# Part 6 Nginx
sudo cp /var/www/peertube/peertube-latest/support/nginx/peertube /etc/nginx/sites-available/peertube
sudo sed -i 's/${WEBSERVER_HOST}/peertube.jimchen.me/g' /etc/nginx/sites-available/peertube
sudo sed -i 's/${PEERTUBE_HOST}/127.0.0.1:9000/g' /etc/nginx/sites-available/peertube
# Then modify the webserver configuration file. 
sudo vim /etc/nginx/sites-available/peertube
sudo ln -s /etc/nginx/sites-available/peertube /etc/nginx/sites-enabled/peertube


# Part 7 Certbot
sudo systemctl stop nginx
sudo certbot certonly --standalone --post-hook "systemctl restart nginx"
sudo systemctl restart nginx

# Part 8 Systemd
sudo cp /var/www/peertube/peertube-latest/support/systemd/peertube.service /etc/systemd/system/
sudo vim /etc/systemd/system/peertube.service
sudo systemctl daemon-reload
sudo systemctl enable peertube
sudo systemctl restart peertube

# Part 9 Admin Password
cd /var/www/peertube/peertube-latest && NODE_CONFIG_DIR=/var/www/peertube/config NODE_ENV=production npm run reset-password -- -u root

# Troubleshooting
sudo journalctl -feu peertube