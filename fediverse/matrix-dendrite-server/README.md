## Generate config

```sh
docker run --rm --entrypoint="/usr/bin/generate-keys"   -v $(pwd)/config:/mnt   matrixdotorg/dendrite-monolith:latest   -private-key /mnt/matrix_key.pem
docker run --rm --entrypoint="/bin/sh"   -v $(pwd)/config:/mnt   matrixdotorg/dendrite-monolith:latest   -c "/usr/bin/generate-config \
    -dir /var/dendrite/ \
    -db postgres://dendrite:itsasecret@postgres/dendrite?sslmode=disable \
    -server matrix.jimchen.me > /mnt/dendrite.yaml"
```

Then edit the docker-compose



Folder might be like this

```sh
root@ip-172-31-25-211:~/dendrite# ls
config  docker-compose.yml  media  postgres
root@ip-172-31-25-211:~/dendrite# ls config/
dendrite.yaml  matrix_key.pem
```

## Also change dendrite config to use Postgres

## Also edit the config to change this registration_shared_secret 

## Then go to test

https://federationtester.matrix.org/#matrix.jimchen.me


## Creating Admin


```
docker exec -it 8c5317fe8a00 /usr/bin/create-account -config /etc/dendrite/dendrite.yaml -username ADMINUSERNAME -admin url https://localhost:8009
```

