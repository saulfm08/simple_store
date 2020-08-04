# simple_store
Simple store is a very simple project which contains a CRUD for Products.

## Requirements
- [Docker](https://docs.docker.com/install/linux/docker-ce/ubuntu/)
- [Docker Compose](https://docs.docker.com/compose/install/)

## Instructions
Copy the `env_template` to `.env`
```
cp env_template .env
```
Run with docker-compose
```
docker-compose up -d
```
Run `docker ps -a`to see if all 3 docker containers are running.
You should see something like this:
```
IMAGE                 COMMAND                  CREATED           STATUS           PORTS                NAMES
sample_store_django   "/entrypoint.sh"         hours ago         Up hours         8000/tcp             django
postgres              "docker-entrypoint.s…"   hours ago         Up hours         5432/tcp             db
sample_store_nginx    "nginx -g 'daemon of…"   hours ago         Up hours         0.0.0.0:80->80/tcp   nginx
```


## Defaults
You can also change default values on .env (env_template)

Django:
```
username: admin
password: admin
```
Postgres
```
database name: store
database user: postgres
database pass: postgres
database host: db       # points to db docker container
```
