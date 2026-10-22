from flask import Flask, render_template, url_for, session, request, redirect, flash
import os, sys, sqlite3, re
from pathlib import Path



project_root = Path(__file__).resolve().parent.parent
sys.path.append(str(project_root))

from backend.get_data import get_json_data, get_movies_from_db, get_ratings_from_db
from backend.database import db as _db

app = Flask(__name__)

app.config['DATABASE'] = project_root / 'backend' / 'database' / 'users.db'
app.config['SECRET_KEY'] = 'dev-secret-key-change-later'

_db.init_app(app)



@app.route('/')
def base():
    return render_template("base.html")

@app.route('/register', methods=['GET', 'POST'])
def register():
    msg=''
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form and 'email' in request.form:
        username = request.form['username']
        password = request.form['password']
        email = request.form['email']

        db = _db.get_db()

        res = db.execute(
            "SELECT * FROM user WHERE username = ? OR email = ?", (username, email)
        )
        account = res.fetchone()

        if account:
            msg = 'Account already exists!'
        elif not re.match(r'[^@]+@[^@]+\.[^@]+', email):
            msg = 'Invalid email address!'
        elif not re.match(r'[A-Za-z0-9]+', username):
            msg = 'Username must contain only letters and numbers!'
        elif not username or not password or not email:
            msg = 'Please fill out the form!'
        else:
            db.execute("INSERT INTO user VALUES (NULL, ?, ?, ?)", (username, email, password))
            db.commit()
            msg = 'You have successfully registered!'
        return render_template('auth/register.html', msg=msg)

    return render_template('auth/register.html', msg=msg)


@app.route('/login', methods=['GET', 'POST'])
def login():
    msg=''
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
        username = request.form['username']
        password = request.form['password']

        db = _db.get_db()
        res = db.execute('SELECT * FROM user WHERE username = ? AND password = ?', (username, password))
        account = res.fetchone()

        if account:
            session['loggedin'] = True
            session['user_id'] = account['id']
            session['username'] = account['username']
            return render_template('base.html', msg='Logged in successfully!')
        else:
            msg = 'Incorrect login/password!'
    return render_template('auth/login.html', msg=msg)

@app.route('/logout')
def logout():
    session.pop('loggedin', None)
    session.pop('user_id', None)
    session.pop('username', None)
    return redirect(url_for('base'))



#TODO Adding rating to a movie



@app.route('/rate/<int:movie_id>', methods=['GET', 'POST'])
def rate_movie(movie_id):
    data = get_json_data()
    movie = data['movies'][movie_id]
    title = movie['Title']
    img = movie['Poster']

    if not session.get('user_id'):
        #flash('Musisz się zalogować, aby móc ocenić film.')
        return redirect(url_for('login'))

    msg=''
    if request.method == 'POST':
        user_id = session['user_id']
        value = request.form['rating']

        db = _db.get_db()
        res = db.execute("SELECT * FROM ratings WHERE user_id = ? AND movie_id = ?", (user_id, movie_id))
        existing_rating = res.fetchone()

        if existing_rating:
            msg = "You have already rated this movie."
            return render_template('rate/rate.html', movie_id=movie_id, title=title, img=img, msg=msg)

        db.execute(
            "INSERT INTO ratings (user_id, movie_id, value) VALUES (?, ?, ?)",
            (user_id, movie_id, value)
        )
        db.commit()
        return redirect(url_for('base'))
        
    return render_template('rate/rate.html', movie_id=movie_id, title=title, img=img, msg=msg)


@app.route('/raitings', methods=['GET', 'POST'])
def get_my_raitings():
    if not session.get('user_id'):
        return redirect(url_for('login'))

    if request.method == 'POST':
        action = request.form.get('action')
        rate_id = request.form.get('rating_id')
        db = _db.get_db()

        if action == 'delete':
            res = db.execute("DELETE FROM ratings WHERE id = ?", (rate_id,))
            db.commit()
        elif action == 'edit':
            print("edit")
    
    msg=''

    return render_template('my_ratings.html')



@app.route('/api/ratings')
def get_ratings():
    if not session.get('user_id'):
        return None

    user_id = session['user_id']
    ratings = get_ratings_from_db(user_id)

    return ratings
    


@app.route('/api/movies')
def get_data():
    _data = get_movies_from_db()

    return _data


if __name__ == '__main__':
    app.run(debug=True)



