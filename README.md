# SBrain
It is an open source project that consists of being an extension of your mind with several useful tools.

## QuickStart
Install Docker Engine from the tutorial <https://docs.docker.com/engine/installation/>.</br>
Get the latest project clone to your computer:

```bash
$ git clone git@github.com:sbrainproject/sbrain.git
```

Run docker-compose commands to start containers:
```bash
$ docker-compose up
```

Now you can access the application at <http://localhost>.</br>
## Django Admin
If you want to access django admin site, please apply the django default migrations to database:
```bash
$ docker-compose run --rm web bash
$ python manage.py migrate
```

### Testing
If you want to access django admin site, please apply the django default migrations to database:
```bash
$ docker-compose run --rm web bash
$ python manage.py test -v 3
```

### Super user
Then you need to create a superuser account:
```bash
$ docker-compose run --rm web bash
$ python manage.py createsuperuser
```

## Docker Images Reference

| Name     | Image                                  |
| -------- | -------------------------------------- |
| Postgres | <https://hub.docker.com/_/postgres/>   |
| Python   | <https://hub.docker.com/_/python/>     |

