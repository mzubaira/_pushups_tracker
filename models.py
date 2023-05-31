from . import db

class User(db.model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))

#Create database from CMD
# python3
# import db,create_app
# db.create_all(app=create_app())ssss