Postgres
--------

`sudo apt-get update
sudo apt-get install python-pip python-dev libpq-dev postgresql postgresql-contrib
`
`sudo su - postgres`
`psql`

`CREATE DATABASE towers;`
`CREATE USER toweruser WITH PASSWORD 'towerpass';`

`ALTER ROLE toweruser SET client_encoding TO 'utf8';`

`GRANT ALL PRIVILEGES ON DATABASE Towers TO toweruser;`
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

python manage.py runserver

