# CATALOG

This project is a training project from udacity full-stack nanodegree program. 
The project emulate the need of a fablab, an organisation with members, machines and differents projects using differents tools (3D printing, laser cutting etc.)

## GETTING STARTED

### Installation

To install the project you'll need :
* [sqlite](https://sqlite.org/download.html)
* [python2.7](https://www.python.org/downloads/) 
* [virtualenv](https://virtualenv.pypa.io/en/latest/)

### Setting up environement

To start the project, first :
`git clone https://github.com/PetitPandaRoux/catalog.git`

Set up your virtualenv using python 2.7 in the same directory :
`virtualenv ENV --python=python2.7`
Start the virtual environment :
`source ENV/bin/activate`
Install all dependencies :
`pip install -r requirements.txt`

### Setting up database
You need to initiate the database :
`python setup_database.py`

Then you need to fill the database :
`python fill_database.py`

You should have lepetitfablabdeparis.db with some projects, members and machines.

#### Running
To start the project :
`python catalog.py`
You can then check with the browser: http://127.0.0.1:8800/
You shoul have something that look like :

![image](https://drive.google.com/uc?export=view&id=1iZ685bnapzS5nbkpilUY0FzsnPQqNNau
)

## WEB APP :

For each project you can add a tag concerning the tool used to make the object
For now you can edit, delete and add new projects only if you are login.
To log in there are two options : 
- use github Oauth, it will create a new user if not already in database
- simply enter the name of a member (password management underconstruction)

## API ENDPOINTS

To access API endpoints to have a JSON list of members, projects and machines :
http://127.0.0.1:8800/catalog/projects/JSON
http://127.0.0.1:8800/catalog/members/JSON
http://127.0.0.1:8800/catalog/machines/JSON

For a specific member, machine or project :
http://127.0.0.1:8800/catalog/machine/<id>/JSON


## FURTHER DEVELOPMENT
- Generate date of today when register using Oauth
- Create a way to upload picture file to server and database
- Create a password management for each user
