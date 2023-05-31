from flask import Blueprint, render_template, url_for, request, redirect
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import login_user, logout_user, login_required
from .models import User
from. import db

auth = Blueprint('auth',__name__)

@auth.route('/signup')
def signup():
    return render_template('signup.html')

@auth.route('/signup',methods=['POST'])
def signup_post():
    name = request.form.get('name')
    email = request.form.get('email')
    password = request.form.get('password')

    #print(name, email, password)

    #Check if user is already signed up or not by querying the "User" table
    user = User.query.filter_by(email=email).first()

    if user:
        return redirect(url_for('auth.signup')) #redirect to sign uppage if user already exists
    
    #create a new user object, add it to the DB & Commit
    new_user = User(email=email,name=name,password=generate_password_hash(password,method='sha256'))
    db.session.add(new_user)
    db.session.commit()

    return redirect(url_for('auth.login'))

@auth.route('/login')
def login():
    return render_template('login.html')

@auth.route('/login',methods=['POST'])
def login_post(): 
    email = request.form.get('email')
    password = request.form.get('password')
    remember = True if request.form.get('remember') else False

    #print(email, password)
    
    #Get the user object from DB by 'email' filter
    user = User.query.filter_by(email=email).first()

    #un-successfull login, redirect to login page
    if not user or not check_password_hash(user.password, password):
        return redirect(url_for('auth.login'))
    
    login_user(user, remember=remember)

    #if login is successful, redirect to profile page
    return redirect(url_for('main.profile')) 

@auth.route('/logout')
@login_required #you need to be logged in to access the "logout" page
def logout():
    #return "logging out"
    logout_user()
    return redirect('main.index')



