from flask import Flask, render_template, url_for
import os, sys
from pathlib import Path

project_root = Path(__file__).resolve().parent.parent
sys.path.append(str(project_root))

from backend.get_data import get_json_data

app = Flask(__name__)

@app.route('/')
def hello():
    return render_template("base.html")

@app.route('/api/movies')
def get_data():
    data = get_json_data()
    return data


if __name__ == '__main__':
    app.run(debug=True)



