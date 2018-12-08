#!/usr/bin/env python2

from flask import Flask, render_template, request, redirect, url_for, flash, jsonify

from flask_dance.contrib.github import make_github_blueprint, github

from sqlalchemy import create_engine, desc, asc
from sqlalchemy.orm import sessionmaker
from setup_database import Base, Member, Machine, Project, Tag
import os

app = Flask(__name__)

github_blueprint = make_github_blueprint(
    client_id='968903ce2aaebd6dd332',
    client_secret='4b98a975586df65eb8ae16df9bd3954e169644be')

# We use flask-dance to facilitate token management
app.register_blueprint(github_blueprint, url_prefix='/login')

os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'

# DataBase Creation
engine = create_engine('sqlite:///lepetitfablabdeparis.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)


@app.route('/catalog/projects/JSON')
def projects_JSON():
    session = DBSession()
    projects = session.query(Project).all()
    session.close()
    return jsonify(Project=[project.serialize for project in projects])


@app.route('/catalog/project/<int:project_id>/JSON')
def project_JSON(project_id):
    session = DBSession()
    project = session.query(Project).filter_by(id=project_id).one()
    session.close()
    return jsonify(Project=[project.serialize])


@app.route('/catalog/projects/<tag_name>/JSON')
def projects_tag_JSON(tag_name):
    session = DBSession()
    projects = session.query(Project).join(Tag).filter(Tag.tag_name == tag_name.replace('_', ' ')).order_by(desc(Project.id)).all()
    session.close()
    return jsonify(Project=[project.serialize for project in projects])


@app.route('/catalog/machines/JSON/')
def machines_JSON():
    session = DBSession()
    machines = session.query(Machine).all()
    session.close()
    return jsonify(Machine=[machine.serialize for machine in machines])


@app.route('/catalog/machine/<int:machine_id>/JSON/')
def machine_JSON(machine_id):
    session = DBSession()
    machine = session.query(Machine).filter_by(id=machine_id).one()
    session.close()
    return jsonify(Machine=[machine.serialize])


@app.route('/catalog/members/JSON')
def members_JSON():
    session = DBSession()
    members = session.query(Member).all()
    session.close()
    return jsonify(Member=[member.serialize for member in members])


@app.route('/catalog/member/<int:member_id>/JSON')
def member_JSON(member_id):
    session = DBSession()
    member = session.query(Member).filter_by(id=member_id).one()
    session.close()
    return jsonify(Member=[member.serialize])


@app.route('/')
@app.route('/catalog/')
def show_home():
    return render_template('catalog.html')


@app.route('/catalog/login')
def show_login():
    if not github.authorized:
        return redirect(url_for('github.login'))
    account_info = github.get('/user')

    if account_info.ok:
        account_info_json = account_info.json()
        message = account_info_json['login']
        return render_template('account.html', account=account_info_json)
    return '<h1>Request failed</h1>'


'''
TODO :
Avoir une session [],
enfermer dans la session les informations d'utilisateurs,
si l'utilisateur est ou non dans la base sinon l'inscrire,
vider la session lors du logout.
'''


# Show all members, their avatars and their names
@app.route('/catalog/members')
def show_members():
    session = DBSession()
    members = session.query(Member).all()
    session.close()
    return render_template('members.html', members=members)


# Show member with information and projects realized
@app.route('/catalog/member/<int:member_id>')
def show_member(member_id):
    session = DBSession()
    member = session.query(Member).filter_by(id=member_id).one()
    projects = session.query(Project).filter(Project.member_id == member_id).all()
    session.close()
    return render_template('member.html', member=member, projects=projects)


# Show main machines present inside the fablab
@app.route('/catalog/machines')
def show_machines():
    session = DBSession()
    machines = session.query(Machine).all()
    session.close()
    return render_template('machines.html', machines=machines)


# Show the latest 5 projects
@app.route('/catalog/projects/')
def show_projects():
    session = DBSession()
    projects = session.query(Project).order_by(desc(Project.id)).limit(5)
    session.close()
    return render_template('projects.html', projects=projects)


# Show specific project information
@app.route('/catalog/projects/<int:project_id>/')
def show_project(project_id):
    session = DBSession()
    project = session.query(Project).filter_by(id=project_id).one()
    member = session.query(Member).filter_by(id=project.member_id).one()
    session.close()
    return render_template('project.html', project=project, member=member)


@app.route('/catalog/machiness/<int:machine_id>/')
def show_machine(machine_id):
    session = DBSession()
    machine = session.query(Machine).filter_by(id=machine_id).one()
    session.close()
    return render_template('machine.html', machine=machine)


# Edit the selected project
@app.route('/catalog/projects/<int:project_id>/edit', methods=['GET', 'POST'])
def edit_project(project_id):
    session = DBSession()
    project = session.query(Project).filter_by(id=project_id).one()
    members = session.query(Member).all()

    # aThis is to automatically checked tag in the view
    tags = session.query(Tag).filter(Tag.project_id == project_id).all()
    tag_names = []

    for tag in tags:
        tag_names.append(tag.tag_name)

    all_tags = ['Arduino', '3D Printer', 'Laser Cutter', 'Portable Electric']

    if request.method == 'POST':
        project.name = request.form['name']
        project.description = request.form['description']
        member_id = request.form.get('member')
        member = session.query(Member).filter_by(id=member_id).one()
        project.member = member
        session.add(project)
        session.commit()

    # You need to delete all tags previously put
        for tag in tags:
            session.delete(tag)
            session.commit()

        counter = False
        for update_tag in all_tags:
            if request.form.get(update_tag):
                new_tag = Tag(tag_name=update_tag, project=project)
                session.add(new_tag)
                session.commit()
                counter = True

        # When no tools have been used for the project
        if counter is False:
                no_tools = Tag(tag_name="No Tools", project=project)
                session.add(no_tools)
                session.commit()

        flash(project.name + " has been updated!")
        return redirect(url_for('show_projects'))

    else:
        return render_template(
            'editProject.html',
            project=project,
            members=members,
            tag_names=tag_names,
            all_tags=all_tags)


# Delete the selected project
@app.route('/catalog/projects/<int:project_id>/delete', methods=['GET', 'POST'])
def delete_project(project_id):
    session = DBSession()
    project = session.query(Project).filter_by(id=project_id).one()

    # clean the Tag table associated
    tags = session.query(Tag).filter(Tag.project_id == project_id).all()

    if request.method == 'POST':
        session.delete(project)
        session.commit()

        for tag in tags:
            session.delete(tag)
            session.commit()

        session.close()
        flash("Project has been deleted!")
        return redirect(url_for('show_projects'))
    else:
        session.close()
        return render_template(
            'deleteProject.html',
            project=project,
            tags=tags)


# Create a new project
@app.route('/catalog/projects/new', methods=['GET', 'POST'])
def new_project():
    if request.method == 'POST':
        session = DBSession()
        member_id = request.form.get('member')
        member = session.query(Member).filter_by(id=member_id).one()
        new_project = Project(
            name=request.form['name'],
            description=request.form['description'],
            member=member)
        session.add(new_project)
        session.commit()

        # Project table and tag table are in relationship
        tags = ['Arduino', '3D Printer', 'Laser Cutter', 'Portable Electric']
        counter = 0
        for tag in tags:
            if request.form.get(tag):
                new_tag = Tag(tag_name=tag, project=new_project)
                session.add(new_tag)
                session.commit()
                counter = 1

        # When no tools have been used for the project
        if counter == 0:
                no_tools = Tag(tag_name="No Tools", project=new_project)
                session.add(no_tools)
                session.commit()

        flash("Project has been created!")
        return redirect(url_for('show_projects'))
    else:
        session = DBSession()
        members = session.query(Member).all()
        session.close()
        return render_template('newProject.html', members=members)
        
        
# Show all project using a certain catagory of tool
@app.route('/catalog/projects/<tag_name>/')
def show_projects_tag(tag_name):
    session = DBSession()
    projects = session.query(Project).join(Tag).filter(Tag.tag_name == tag_name.replace('_', ' ')).order_by(desc(Project.id)).all()
    session.close()
    return render_template(
        'projectsTag.html',
        projects=projects,
        tag_name=tag_name)

# Here we create helper function
def createUser(login_session):
    session = DBSession()
    newUser = Member(name=login_session['username'],
                   email=login_session['email'],
                   picture=login_session['picture'])
    session.add(newUser)
    session.commit()
    session.close()
    member = session.query(Member).filter_by(email=login_session['email']).one()
    return member.id


# To get user Information
def getUserInfo(member_id):
    session = DBSession()
    member = session.query(Member).filter_by(id=member_id).one()
    session.close()
    return user


# To get users information
def getUserID(email):
    try:
        member = session.query(Member).filter_by(email=email).one()
        return meber.id
    except:
        return None


if __name__ == '__main__':
    app.secret_key = "super_secret_key"
    app.debug = True
    app.run(host='0.0.0.0', port=5000, threaded=False)
