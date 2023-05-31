from flask import Blueprint, render_template, redirect, url_for
from flask_login import login_required, current_user

main = Blueprint('main',__name__)

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/profile')
@login_required #we need a logged in user to view his 'My Account' page, else it will be hidden from Guests
def profile():
    return render_template('profile.html', name=current_user.name)

