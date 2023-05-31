sudo apt install python3-flask

## Running the app
export FLASK_APP=_pushups_tracker
flask run

Thi  is an environment variable given by flask which handles the behign scenes for your app & WSGI,.
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