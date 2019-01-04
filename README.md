# CATALOG - AWS - DEPLOY

This project is a training project from udacity full-stack nanodegree program. 
The project emulate the need of a fablab, an organisation with members, machines and differents projects using differents tools (3D printing, laser cutting etc.). It is hosted on amazon web service as a ubuntu16 server on this IP address: 
http://35.180.62.188/

## Installation on server step by step

On the server I installed :
`sudo apt-get python`
`sudo apt-get apache2`
`sudo apt-get python-pip`
`sudo apt-get install libapache2-mod-wsgi`

I created 2 users, added them to the suddoers and created an encrypt key for each user
- zak for me
- grader for the reviewer

Then I cloned the repo : `git clone https://github.com/PetitPandaRoux/catalog.git`
Switched to the `git checkout prod` branch
To install all the dependencies I did a :
`sudo -H pip install -r requirements.txt`, the -H is important if you are logged as a user created, otherwise when launching apache, he doesn't find python dependencies like flask. 

## Securities, Port and firewall
Amazon by default only allow ssh-key connection and forbid password connection
I forbid root user `sudo nano /etc/ssh/sshd_config` 
I changed the port for ssh to `2200` using `sudo nano /etc/ssh/sshd_config` 
I needed to set port on the dashboard because Amazon put a firewall on top of hour configuration
I blocked by default all incomming connection except for ssh, www and port 123/tcp


## Setting up WSGI and Apache2 and sqlite database 
After installing Apache2 and libapache2-mod-wsgi I created a :
- catalog.wsgi wich is the gate to my webapp
- `/etc/apache2/sites-available nano catalog.conf` to configure apache2

I deleted the default behavior of apache2 to set WSGI :
- `sudo a2dissite 000-default.conf` 
Use my own conf and reload service
- `sudo a2ensite catalog.conf`
- `sudo service apache2 reload`

Then to run, a changed in owner of catalog folder and path to database were necessary.
I changed every :
```python
engine = create_engine('sqlite:///lepetitfablabdeparis.db')
```
Inside the setup_database and inside catalog.py to
```python
engine = create_engine('sqlite:////var/www/catalog/lepetitfablabdeparis.db')
```
I changed the ownership of my var/www/catalog/ and of my database from root to www-data for apache2 to access, read and write in it.

Then... IT WORKED !!!!!!!!!!

Internet ressources useful :
https://umar-yusuf.blogspot.com/2018/02/deploying-python-flask-web-app-on.html
http://flask.pocoo.org/docs/0.12/deploying/mod_wsgi/
