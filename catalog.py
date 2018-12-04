#!/usr/bin/env python2

from flask import Flask, render_template, request, redirect, url_for, flash, jsonify

from sqlalchemy import create_engine, desc, asc
from sqlalchemy.orm import sessionmaker
from setup_database import Base, Member, Machine, Project, Tag

app = Flask(__name__)

#DataBase
engine = create_engine('sqlite:///lepetitfablabdeparis.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)

@app.route('/')
@app.route('/catalog/')
def show_home():
    return render_template('catalog.html')

@app.route('/catalog/login')
def show_connection():
    return "Ici on se connecte sois avec Oauth sois on s'inscrit"

# Show all members, their avatars and their names
@app.route('/catalog/members')
def show_members():
    session = DBSession()
    members = session.query(Member).all()
    session.close()
    return render_template('members.html', members=members)

# Show member with information and projects realized
@app.route('/catalog/member/<member_id>')
def show_member(member_id):
    session = DBSession()
    member = session.query(Member).filter_by(id=member_id).one()
    return render_template('member.html', member = member)

# Show main machines present inside the fablab
@app.route('/catalog/machines')
def show_machines():
    session = DBSession()
    machines = session.query(Machine).all()
    session.close()
    return render_template('machines.html', machines=machines)

# Show the latest 5 projects
@app.route('/catalog/projects')
def show_projects():
    session = DBSession()
    projects = session.query(Project).order_by(desc(Project.id)).limit(5)
    session.close()
    return render_template('projects.html', projects=projects)

# Show all project using a certain catagory of tool
@app.route('/catalog/projects/<tag_name>/')
def show_projects_tag(tag_name):
    session = DBSession()
    projects = session.query(Project).join(Tag).filter(Tag.tag_name == tag_name.replace('_',' ')).all()
    session.close()
    return render_template('projects_tag.html', projects=projects)

# Show all information concerning one project
@app.route('/catalog/projects/<tag_name>/<int:project_id>')
def show_project(tag_name):
    session = DBSession()
    projects = session.query(Project).join(Tag).filter(Tag.tag_name == tag_name.replace('_',' ')).all()
    session.close()
    return render_template('projects_tag.html', projects=projects)

if __name__ == '__main__':
    app.secret_key = "super_secret_key"
    app.debug = True
    app.run(host='0.0.0.0', port=5000, threaded = False)

