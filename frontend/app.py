from flask import Flask, render_template, url_for, session, request
import os, sys, sqlite3, re
from pathlib import Path



project_root = Path(__file__).resolve().parent.parent
sys.path.append(str(project_root))

from backend.get_data import get_json_data
from backend.database import db

app = Flask(__name__)

app.config['DATABASE'] = project_root / 'backend' / 'database' / 'users.db'

db.init_app(app)

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

        con = sqlite3.connect(app.config['DATABASE'])
        cur = con.cursor()
        res = cur.execute(
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
            cur.execute("INSERT INTO user VALUES (NULL, ?, ?, ?)", (username, email, password))
            con.commit()
            msg = 'You have successfully registered!'
        return render_template('auth/register.html', msg=msg)

    return render_template('auth/register.html', msg=msg)


@app.route('/login', methods=['GET', 'POST'])
def login():
    msg='test_login'

    return render_template('auth/login.html', msg=msg)


@app.route('/api/movies')
def get_data():
    data = get_json_data()
    return data


if __name__ == '__main__':
    app.run(debug=True)



