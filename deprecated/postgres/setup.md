## Postgres is the Database for many Apps

```sh
docker run -d \
  --name postgres-container \
  -p 5432:5432 \
  -v postgres-data:/var/lib/postgresql/data \
  --restart always \
  postgres:latest
```

## Expose it to all ip(not a good idea, but since I am exposing MongoDB also, let's go with it)

```sh
docker exec -it postgres-container bash
sed -i "s/#listen_addresses = 'localhost'/listen_addresses = '*'/" /var/lib/postgresql/data/postgresql.conf
echo "host all all 0.0.0.0/0 md5" >> /var/lib/postgresql/data/pg_hba.conf

su - postgres
psql
ALTER USER postgres WITH PASSWORD 'your_new_password';

exit

docker restart postgres-container
```

## Migration

```
IP_ADDRESS=""

docker exec mastodon-db-1 pg_dump -U postgres -O postgres > output_file.sql



psql "postgresql://postgres@$IP_ADDRESS:5432/postgres" -c "CREATE USER mastodon"
psql "postgresql://postgres@$IP_ADDRESS:5432/postgres"
ALTER USER mastodon CREATEDB;
exit
psql "postgresql://mastodon@$IP_ADDRESS:5432/postgres" -U mastodon -c "CREATE DATABASE mastodon_production"
psql "postgresql://postgres@$IP_ADDRESS:5432/postgres"
ALTER USER mastodon NOCREATEDB;
exit
psql "postgresql://mastodon@$IP_ADDRESS:5432/mastodon_production" < output_file.sql
```

## Create and Grant

```sh
postgres=# CREATE USER miniflux WITH PASSWORD '';
CREATE ROLE
postgres=# CREATE DATABASE miniflux;
CREATE DATABASE
postgres=# ALTER DATABASE miniflux OWNER TO miniflux;
ALTER DATABASE
postgres=# GRANT ALL PRIVILEGES ON DATABASE miniflux TO miniflux;
GRANT
postgres=# \c miniflux
psql (16.3, server 16.4 (Debian 16.4-1.pgdg120+1))
You are now connected to database "miniflux" as user "postgres".
miniflux=# GRANT ALL PRIVILEGES ON ALL TABLES IN SCHEMA public TO miniflux;
GRANT ALL PRIVILEGES ON ALL SEQUENCES IN SCHEMA public TO miniflux;
GRANT ALL PRIVILEGES ON ALL FUNCTIONS IN SCHEMA public TO miniflux;
GRANT
GRANT
GRANT
miniflux=# 
```