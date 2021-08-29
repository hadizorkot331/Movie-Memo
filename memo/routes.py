from memo import app, db
from memo.models import User, Movie
from flask import render_template, request, get_flashed_messages, flash, redirect, url_for
from memo.forms import RegisterForm, LoginForm
from werkzeug.security import generate_password_hash
from flask_login import login_user, current_user, logout_user
from datetime import datetime

@app.route('/')
def home():
    if current_user.is_authenticated:
        movies = Movie.query.filter_by(user_id=current_user.get_id()).order_by(Movie.time_added.desc())
        return render_template("home.html", movies=movies)
    else:
        return redirect(url_for('login'))

@app.route('/register', methods=['POST', 'GET'])
def register():
    form = RegisterForm()

    if form.validate_on_submit():
        user_to_add = User(username=form.username.data,
                        password=str(generate_password_hash(form.password.data)))  

        db.session.add(user_to_add)
        db.session.commit()

        user = User.query.filter_by(username=form.username.data).first()
        login_user(user)
        return redirect(url_for('home'))

    if form.errors != {}:
        for error in form.errors.values():
            flash(error, category="danger")
            
    return render_template("register.html", form=form)

@app.route('/login', methods=['POST', 'GET'])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        login_user(user)
        flash("Successfully logged in!", category="success")
        return redirect(url_for('home'))
    if form.errors != {}:
        for error in form.errors.values():
            flash(error, category="danger")

    return render_template("login.html", form=form)

@app.route('/add_movie', methods=['POST', 'GET'])
def add_movie():
    if current_user.is_authenticated:
        if request.method == "GET":
            return render_template("add_movie.html")
        elif request.method == "POST":
            title = request.form['title']
            genre = request.form['genre']
            description = request.form['description']
            rating = float(request.form['rating'])

            movie = Movie(user_id=current_user.get_id(),
                            rating=rating,
                            description=description,
                            time_added=datetime.now(),
                            genre=genre,
                            title=title)

            db.session.add(movie)
            db.session.commit()

            flash(f"Added {title}!", category="success")
            return redirect(url_for('home'))
    else:
        flash("Please Login to use this feature!", category="danger")
        return redirect(url_for('login'))

@app.route('/delete', methods=['POST', 'GET'])
def delete():
    if request.method == "POST":
        if current_user.is_authenticated:
            try:
                m_id = int(request.form.get('selection'))
            except TypeError:
                flash("No Movie To Delete", category="danger")
                return redirect(url_for('home'))

            Movie.query.filter_by(movie_id=m_id).delete()
            db.session.commit()
            flash("Deleted", category="success")
            return redirect(url_for('home'))
        else:
            flash('Login to use this feature', category="danger")
            return redirect(url_for('login'))
    else:
        if current_user.is_authenticated:
            movies = Movie.query.filter_by(user_id=current_user.get_id()).order_by(Movie.time_added.desc())
            return render_template("delete.html", movies=movies)
        else:
            flash('Login to use this feature', category="danger")
            return redirect(url_for('login'))

@app.route('/search', methods=['POST', 'GET'])
def search_movies():
    if request.method == "GET":
        if current_user.is_authenticated:
            return render_template("search.html")
        else:
            flash("Please Login to use this feature!", category="danger")
            return redirect(url_for('login'))
    else:
        if current_user.is_authenticated:
            genre = request.form.get('genre')
            movies = Movie.query.filter_by(genre=genre, user_id=current_user.get_id()).order_by(Movie.time_added.desc())
            return render_template("view_ordered.html", movies=movies, genre=genre)
        else:
            flash("Please Login to use this feature!", category="danger")
            return redirect(url_for('login'))

@app.route('/logout')
def logout():
    if current_user.is_authenticated:
        logout_user()

        flash("Logged out!", category="success")
        return redirect(url_for('login'))
    else:
        flash("Can't logout: You are not logged in!", category="danger")
        return redirect(url_for('login'))