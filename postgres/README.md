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

## Migration (Mastodon Example)
```sh
docker exec mastodon-db-1 pg_dump -U postgres YOUR_DATABASE_NAME > mastodon_backup.sql
```

Then on another remote:

```sh
psql "postgresql://postgres@..." -c "CREATE DATABASE mastodon;"
 psql "postgresql://postgres@.../mastodon" < mastodon_backup.sql
```