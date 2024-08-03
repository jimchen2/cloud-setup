sudo apt update && sudo apt upgrade -y
apt-get install curl sudo unzip vim
curl -fsSL https://deb.nodesource.com/setup_18.x -o nodesource_setup.sh && sudo -E bash nodesource_setup.sh
sudo apt-get install -y nodejs
sudo npm -g install yarn
sudo apt install python3-dev python3-pip python-is-python3
sudo apt install certbot nginx ffmpeg postgresql postgresql-contrib openssl g++ make redis-server git cron wget
sudo systemctl enable --now redis-server postgresql





ffmpeg -version # Should be >= 4.1
g++ -v # Should be >= 5.x
redis-server --version # Should be >= 6.x