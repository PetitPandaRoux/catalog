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

@app.route('/catalog/members')
def show_members():
    session = DBSession()
    members = session.query(Member).all()
    session.close()
    return render_template('members.html', members=members)

@app.route('/catalog/machines')
def show_machines():
    session = DBSession()
    machines = session.query(Machine).all()
    session.close()
    return render_template('machines.html', machines=machines)

@app.route('/catalog/projects')
def show_projects():
    session = DBSession()
    projects = session.query(Project).order_by(desc(Project.id)).limit(5)
    session.close()
    return render_template('projects.html', projects=projects)

@app.route('/catalog/projects/arduino')
def show_projects_arduino():
    session = DBSession()
    projects = session.query(Project).join(Tag).filter(Tag.tag_name == 'Arduino').all()
    session.close()
    return render_template('projects_arduino.html', projects=projects)

@app.route('/catalog/projects/3D_printer')
def show_projects_3D_printer():
    session = DBSession()
    projects = session.query(Project).join(Tag).filter(Tag.tag_name == '3D printer').all()
    session.close()
    return render_template('projects_3D_printer.html', projects=projects)

@app.route('/catalog/projects/laser_cutter')
def show_projects_laser_cutter():
    session = DBSession()
    projects = session.query(Project).join(Tag).filter(Tag.tag_name == 'Laser cutter').all()
    session.close()
    return render_template('projects_laser_cutter.html', projects=projects)

@app.route('/catalog/projects/portable_electric')
def show_projects_portable_electric():
    session = DBSession()
    projects = session.query(Project).join(Tag).filter(Tag.tag_name == 'Portable electric').all()
    session.close()
    return render_template('projects_portable_electric.html', projects=projects)

if __name__ == '__main__':
    app.secret_key = "super_secret_key"
    app.debug = True
    app.run(host='0.0.0.0', port=5000, threaded = False)

