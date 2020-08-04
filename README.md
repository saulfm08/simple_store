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
## Defaults
You can also change default values on .env (env_template)
```
username: admin
password: admin
database: store
```
