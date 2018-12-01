#!/usr/bin/env python2

from flask import Flask, render_template, request, redirect, url_for, flash, jsonify

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from setup_database import Base, Member, Machine, Project, Tag, Book

app = Flask(__name__)

#DataBase
engine = create_engine('sqlite:///catalog.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)



@app.route('/')
@app.route('/catalog/')
def show_catalog():
    return render_template('catalog.html')

@app.route('/catalog/login')
def show_connection():
    return "Ici on se connecte sois avec Oauth sois on s'inscrit"

@app.route('/catalog/machines')
def show_machines():
    return "Voici les machines"

@app.route('/catalog/tools')
def show_outils():
    return "Voici les outils du lpfp"

@app.route('/catalog/books')
def show_books():
    return "Voici les livres present au sein du lpfp"


@app.route('/catalog/members')
def show_members():
    return "Voici les membres du lpfp"

if __name__ == '__main__':
    app.secret_key = "super_secret_key"
    app.debug = True
    app.run(host='0.0.0.0', port=5000, threaded = False)

