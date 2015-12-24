Postgres
--------

`sudo apt-get update
sudo apt-get install python-pip python-dev libpq-dev postgresql postgresql-contrib
`
postGIS
`sudo apt-get install -y postgis postgresql-9.3-postgis-2.1`

`sudo su - postgres`
`psql`

`CREATE DATABASE towers;`
`CREATE USER toweruser WITH PASSWORD 'towerpass';`

`ALTER ROLE toweruser SET client_encoding TO 'utf8';`

`GRANT ALL PRIVILEGES ON DATABASE Towers TO toweruser;`

`\connect towers;`
`CREATE EXTENSION postgis;`
`CREATE EXTENSION postgis_topology;`

`\q`
`exit`

`sudo pip install virtualenv`
`virtualenv motionlogic`
`source motionlogic/bin/activate`

`pip install requirements.txt`


cd ~/Towers
python manage.py makemigrations
python manage.py migrate

python manage.py createsuperuser

python poulate.py

python manage.py runserver

