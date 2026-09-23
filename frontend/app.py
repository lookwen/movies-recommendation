from flask import Flask, render_template, url_for
import os, sys
from pathlib import Path

project_root = Path(__file__).resolve().parent.parent
sys.path.append(str(project_root))

from backend.get_data import get_json_data

app = Flask(__name__)

@app.route('/')
def base():
    return render_template("base.html")

@app.route('/register', methods=['GET', 'POST'])
def register():
    msg='test'

    return render_template('register.html', msg=msg)


@app.route('/login', methods=['GET', 'POST'])
def login():
    msg='test_login'

    return render_template('login.html', msg=msg)


@app.route('/api/movies')
def get_data():
    data = get_json_data()
    return data


if __name__ == '__main__':
    app.run(debug=True)



