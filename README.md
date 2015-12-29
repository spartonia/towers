# Intro

Towers is a python/django based project for visualizing GSM towers database from [OpenCellId.org](http://opencellid.org). It requires python 2.7.x and Django 1.7.

# Installation Guide

### Postgres

```
$ sudo apt-get update
$ sudo apt-get install python-pip python-dev libpq-dev postgresql postgresql-contrib
```

### PostGIS

```
$ sudo apt-get install -y postgis postgresql-9.3-postgis-2.1
```
### Create database and enable PostGIS

```
$ sudo su - postgres
> psql

> CREATE DATABASE towers;
> CREATE USER toweruser WITH PASSWORD 'towerpass';
> ALTER ROLE toweruser SET client_encoding TO 'utf8';
> GRANT ALL PRIVILEGES ON DATABASE towers TO toweruser;

> \connect towers;
> CREATE EXTENSION postgis;
> CREATE EXTENSION postgis_topology;

> \q
> exit
```
Note: A complete guide on enabling geospatial database for Django could be found on django's official documentation [here](https://docs.djangoproject.com/en/1.7/ref/contrib/gis/install/) and [here](https://docs.djangoproject.com/en/1.7/ref/contrib/gis/install/geolibs/).

### Install and create a Virtualenv
```
$ sudo pip install virtualenv
$ virtualenv env
$ source env/bin/activate
```
### Install Requirements
```
$ pip install -r requirements.txt
```
### Prepare project 
Unzip the project file and `cd` to the project folder 
```
$ tar -zxvf motionlogic.tar.gz
$ cd motionlogic/Towers
$ python manage.py makemigrations
$ python manage.py migrate
```
Create a user
```
$ python manage.py createsuperuser
```
Download the data from opencellid.org, unzip it and place it in `motionlogic/data` folder as 'cell_towers.csv'. 
Populate the database (Help yourself with a coffee) 
```
$ python populate.py
```
Run following (only once per project) 
```
$ python manage.py collectstatic
```
Start server 
```
$ python manage.py runserver`
```
Open the browser and enter:
[http://127.0.0.1:8000/](http://127.0.0.1:8000/)

Wait until the page loads. On the left upper corner you can search for lat/lon of a desired coordinate to find out if it is covered by the network. 

##### Note: 
* All countries in the OpecCellId dayabase is supported by the application. Currently the database is populated only with "Egypt" data. To enable world data or a specific country edit populate.py file and run populate_Opencellid() function again. 
* We stick with the 4326 standard i.e (lat/lon) - which is inverse of google map coords- for creating geometries.

