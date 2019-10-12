# Name : Django Data Project

## Description :

### Generates the following plots ...

#### 1. Plot the number of matches played per year of all the years in IPL.
#### 2. Plot a stacked bar chart of matches won of all teams over all the years of IPL.
#### 3. For the year 2016 plot the extra runs conceded per team.
#### 4. For the year 2015 plot the top economical bowlers.
#### 5. Performance graphs of batsmen on basis of strike rate.

### Work done in this project

#### 1 Used Django Custom Command to import data from csv into Postgresql database
#### 2 Used Django ORM for making queries
#### 3 Used 5 api routes for creating data 
#### 4 used Redis for caching
#### 5 Used 5 template routes for using Highcharts to plot data on the frontend
#### 6 Created api route for all matches - GET, POST, PUT, DELETE
#### 7 Created api route for all deliveries - GET, POST, PUT, DELETE
#### 8 Created an explorer for any one case bowling average

## Installation for api

### install [redis](https://redis.io/)
### start redis service
```bash
sudo service redis-server start
```
### install [postgresql](https://www.postgresql.org/)
### start postgresql service

```bash
sudo service postgresql start
```
### create a database named djangoipl and update the password in settings.py
### install requirements.txt
```bash
pip install -r requirements.txt
```
### Run the server

```bash
cd djangoipl
python manage.py runserver
```

## Tools used

### asn1crypto==0.24.0
### astroid==1.6.0
### backports.functools-lru-cache==1.5
### configparser==3.5.0
### cryptography==2.1.4
### cycler==0.10.0
### enum34==1.1.6
### futures==3.2.0
### idna==2.6
### ipaddress==1.0.17
### isort==4.3.4
### keyring==10.6.0
### keyrings.alt==3.0
### kiwisolver==1.1.0
### lazy-object-proxy==1.3.1
### logilab-common==1.4.1
### matplotlib==2.2.4
### mccabe==0.6.1
### numpy==1.16.5
### pycrypto==2.6.1
### pygobject==3.26.1
### pylint==1.8.3
### pyparsing==2.4.2
### python-dateutil==2.8.0
### pytz==2019.2
### pyxdg==0.25
### SecretStorage==2.3.1
### singledispatch==3.4.0.3
### six==1.11.0
### subprocess32==3.5.4
### virtualenv==16.7.4
### wrapt==1.9.0

## Contributors

### None



