from flask import Blueprint, render_template, redirect, url_for, request, flash, abort
from flask_login import login_required, current_user
from . import db
from .models import User
from .models import Workout


main = Blueprint('main',__name__)

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/profile')
@login_required #we need a logged in user to view his 'My Account' page, else it will be hidden from Guests
def profile():
    return render_template('profile.html', name=current_user.name)

@main.route('/new')
@login_required
def new_workout():
    return render_template('create_workout.html')

@main.route('/new',methods=['POST'])
@login_required
def new_workout_post():
    pushups = request.form.get('pushups')
    comment = request.form.get('comment')

    #Flask will understand that the workout is linked to the current logged in user
    # We create a Workout DB object & pass in the data which we got from POST
    workout = Workout(pushups=pushups, comment=comment, author=current_user)
    db.session.add(workout)
    db.session.commit()

    flash('Your workut has been added')

    return redirect(url_for('main.user_workouts'))

@main.route('/all')
@login_required
def user_workouts():
    user = User.query.filter_by(email=current_user.email).first_or_404()
    workouts = user.workouts
    return render_template('all_workouts.html', workouts=workouts, user=user)

#We need to generate the workout URL with the ID so that we cna update/delete it
@main.route("/workout/<int:workout_id>/update",methods=['GET','POST'])
@login_required
def update_workout(workout_id):
    workout = Workout.query.get_or_404(workout_id)

    #take the new updated value, update the workout DB object & send back to All workouts
    if request.method == 'POST':
        workout.pushups = request.form['pushups']
        workout.comment = request.form['comment']
        db.session.commit()
        
        flash('Your workout has been updated')
        
        return redirect(url_for('main.user_workouts'))

    return render_template('update_workout.html', workout=workout)

@main.route("/workout/<int:workout_id>/delete", methods=['GET', 'POST'])
@login_required
def delete_workout(workout_id):
    workout = Workout.query.get_or_404(workout_id)
    db.session.delete(workout)
    db.session.commit()
    flash('Your post has been deleted!')
    return redirect(url_for('main.user_workouts'))