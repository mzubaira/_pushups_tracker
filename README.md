sudo apt install python3-flask

## Running the app
Linux:
export FLASK_APP=_pushups_tracker
flask run

Windows:
$env:FLASK_APP="_pushups_tracker"

This is an environment variable given by flask which handles the behign scenes for your app & WSGI,.
Flask looks for an __init__.py file & setup tha app

## Blueprint
It helps in organizing our projects by splitting it into different modules & each module will handle a specific functionality rather than pushing everything under app.py

Blueprint is not an pplications & it needs to be registered to an app before you run it. You basically extend the applicaiton with the contents of the blueprint.

We can access any funton inside the project using the blueprint main.func()

We need a decorator for each function we make - it overrides/modifies the functionality.

## render_template
Used to render the html pages

## static folder
It has the images, CSS files, pdf, etc.

## templates fodler
it holds the html files to be rendered

## __init__.py
Servers as entry point for the flask app
It will deal with everything which has to be set up only once at the beginning - instance, database, login features, etc.

## main.py
Main functions - CRUD
Showing Home Page, Profile page

## Auth.py
Handles the authentication - login, logout, signup


## Template inheritence
We can setup a base template in flask for HTML & use it in other files. e.g. we have a <navbar> which will be common on all the pages. So we can ceate it once & inherit it elsewhere.

## url_for
The url_for() function is very useful for dynamically building a URL for a specific function. There is no need to specify static URLs & gard code them everywhere.

flask.url_for(endpoint, **values)

Example:
from flask import Flask, redirect, url_for
app = Flask(__name__)

@app.route('/admin')
def hello_admin():
   return 'Hello Admin'

@app.route('/guest/<guest>')
def hello_guest(guest):
   return 'Hello %s as Guest' % guest

@app.route('/user/<name>')
def hello_user(name):
   if name =='admin':
      return redirect(url_for('hello_admin'))
   else:
      return redirect(url_for('hello_guest',guest = name))

if __name__ == '__main__':
   app.run(debug = True)

O/P: http://localhost:5000/user/admin
Hello Admin

http://localhost:5000/user/mvl
Hello mvl as Guest

## Jinjer Template
It helps us to use python code inside our HTML pages

REF: https://svn.python.org/projects/external/Jinja-1.1/docs/build/inheritance.html

EXAMPLE: 
<!-- Copies the entire BASE.html template -->
{% extends 'base.html' %} 

{% block head %} {{ super() }}

<!-- We can add our own CSS files inside the HEAD section-->
<link rel="stylesheet" href="{{ url_for('static',filename='extended_beauty.css') }}">

{% endblock %} 

<!-- We are adding content in the BODY section -->
{% block content %}

<div class="showcase">
    <img src="{{ url_for('static',filename='images/pushups.png') }}" alt="Pushup Guy" height="200px">
</div>
<div class="container">
    <h3>Hello!</h3>
    <p>
        Welcome to the push-ups logger! <br>
        This website implements basic CRUD functionality & user authentication.
    </p>
</div>

{% endblock %}


## HTTP Requests (CRUD)
GET -> fetching data from Web Server
POST -> sends info to Web Server
PUT -> modify data in web server
DELETE -> delete data in web server

## Request & Redirect
name = request.form.get('name') => collect the "name" data from the formreturn redirect(url_for('auth.login')) => once the sign up is done, we redirect tp the login page

## Database 
SQLITE: https://sqlitebrowser.org/dl/
from flask_sqlalchemy import SQLAlchemy

All tables should go into models.py

## Create database from CMD
python3
>>>from _pushups_tracker import db,create_app
>>> app=create_app()
>>> app.app_context().push()
>>> db.create_all()
>>> exit()