# Constellation server

This W.I.P API (and backend admin) works with `constellation` app (available in my github)

## Demo app !
This app use:
- Django 5
- Django REST framework
- Postgresql 14

## How to run it

/!\ At present, only work in local

```
pg_ctl -D /usr/local/var/postgres -l /usr/local/var/postgres/server.log start
./manage.py runserver
```

## How to install it

### Prerequisites
Postgresql 14 & python 3.12

### In local (i used virtualenv)
```
mkvirtualenv -p python3.12 constellation
pip install -r requirement.txt

# db
createuser constellation
createdb constellation
```
and configure password for constellation db user

#### Create my_pgpass.conf file:
```
localhost:5432:constellation:constellation:DB_USER_PASSWORD
```