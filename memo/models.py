from flask_login import UserMixin
from memo import db

class User(UserMixin, db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    username = db.Column(db.String(length=30), unique=True, nullable=False)
    password = db.Column(db.String(length=60), nullable=False)

class Movie(db.Model):
    movie_id = db.Column(db.Integer(), primary_key=True)
    user_id = db.Column(db.Integer(), nullable=False)
    rating = db.Column(db.Float(), nullable=False)
    description = db.Column(db.String(length=240), nullable=False)
    time_added = db.Column(db.DateTime(), nullable=False)
    genre = db.Column(db.String(length=50), nullable=False)
    title = db.Column(db.String(length=100), nullable=False)