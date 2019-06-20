from flask import Flask, render_template, flash, redirect, url_for, request,abort

import click
from forms import *
from models import *
import datetime
import requests 
app = Flask(__name__)


app.secret_key = 'Microlly' #Don't use it .. !

@app.route('/')
def showdata(posts=None):
    return render_template('listallpost.html',posts=Publication.select())

@app.route('/list_all_post/<users>/')
def showuserdata(users=None):
    return render_template('listuserpost.html',users=Publication.select().join(User).where(Publication.user.username==users))

@app.route('/newpost/', methods=['GET', 'POST'])
def createnewpost():
    publi = Publication()
    form = NewPublicationForm()
    if request.method == 'POST':
        form = NewPublicationForm(request.form)
        if form.validate():
            form.populate_obj(publi)
            print(publi.title)
            publi.created_at = datetime.datetime.now()
            publi.modified_at = datetime.datetime.now()
            publi.user = User.get(id=1)
            publi.save()
            flash('Votre poste a été publié')
            return redirect(url_for('showdata'))
    return render_template('newpost.html', form=form)

@app.route('/editpost/<int:publi_id>/', methods=['GET', 'POST'])
def editnewpost(publi_id):
    try:
        publi = Publication.get(id=publi_id)
    except DoesNotExist:
        abort(404)
    if request.method == 'POST':
        form = NewEditPublicationForm(request.form, obj=publi)
        if form.validate():
            form.populate_obj(publi)
            publi.modified_at = datetime.datetime.now()
            publi.save()
            flash('Votre changement a été pris en compte.')
            return redirect(url_for('showdata'))
    else:
        form = NewEditPublicationForm(obj=publi)
    return render_template('editpost.html', form=form, publi=publi)
@app.route('/deletepost/<int:publi_id>/', methods=['GET', 'POST'])
def deletepost(publi_id):
    try:
        publi = Publication.get(id=publi_id)
    except DoesNotExist:
        abort(404)
    dq = Publication.delete().where(Publication.id==publi.id)
    dq.execute()
    return redirect(url_for('showdata'))
    return render_template('editpost.html', publi=publi)


@app.route('/newuser/', methods=['GET', 'POST'])
def createnewuser():
    usr = User()
    form = NewUserForm()
    if request.method == 'POST':
        form = NewUserForm(request.form)
        if form.validate():
            form.populate_obj(usr)
            usr.save()
            flash('Votre utilisateur a été crée.')
            return redirect(url_for('showdata'))
    return render_template('newuser.html', form=form)

@app.route('/login/', methods=['GET', 'POST'])
def login():
    usr = User()
    form = NewLoginForm()
    if request.method == 'POST':
        form = NewUserForm(request.form)
        if form.validate():
            form.populate_obj(usr)
            flash('Vous êtes identifié.')
            return redirect(url_for('showdata'))
    return render_template('login.html', form=form)


@app.cli.command()
def initdb():
    
    create_tables()
    click.echo('Initialized the database')

@app.cli.command()
def dropdb():
    
    drop_tables()
    click.echo('Dropped tables from database')

@app.cli.command()
def fakedata():
    from faker import Faker
    fake = Faker()

    for pk in range(0, 5):
        User.create(username=fake.user_name(),
                    first_name=fake.first_name(),
                    last_name=fake.last_name(),
                    email=fake.email(),
                    birthday=fake.date_of_birth(),
                    password=fake.password())
    for user in User.select():
        for pk in range(0, 4):
            created_at = fake.date_time(end_datetime="now")
            Publication.create(title=fake.word(), 
                            body=fake.text(),
                            created_at=created_at,
                            modified_at=fake.date_time_between_dates(datetime_start=created_at),
                            user=user)
