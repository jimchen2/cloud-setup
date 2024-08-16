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

Then create a user inside the psql shell

```sql
CREATE USER mastodon WITH PASSWORD '';
```

Then change owner 

```sql
ALTER DATABASE mastodon OWNER TO mastodon;

\c mastodon
-- Make mastodon the owner of the public schema
ALTER SCHEMA public OWNER TO mastodon;

-- Grant all privileges on the schema
GRANT ALL PRIVILEGES ON SCHEMA public TO mastodon;

-- Grant privileges on all existing objects
GRANT ALL PRIVILEGES ON ALL TABLES IN SCHEMA public TO mastodon;
GRANT ALL PRIVILEGES ON ALL SEQUENCES IN SCHEMA public TO mastodon;
GRANT ALL PRIVILEGES ON ALL FUNCTIONS IN SCHEMA public TO mastodon;

-- Set default privileges for future objects
ALTER DEFAULT PRIVILEGES IN SCHEMA public GRANT ALL PRIVILEGES ON TABLES TO mastodon;
ALTER DEFAULT PRIVILEGES IN SCHEMA public GRANT ALL PRIVILEGES ON SEQUENCES TO mastodon;
ALTER DEFAULT PRIVILEGES IN SCHEMA public GRANT ALL PRIVILEGES ON FUNCTIONS TO mastodon;

-- Revoke public schema usage from PUBLIC role
REVOKE ALL ON SCHEMA public FROM PUBLIC;

-- Grant schema usage to mastodon
GRANT USAGE ON SCHEMA public TO mastodon;
```

## Utils

`\l`, `\du`

