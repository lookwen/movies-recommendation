import json, os
from pathlib import Path
import sys

project_root = Path(__file__).resolve().parent.parent

from backend.database import db as _db

def get_json_data():
    try:
        filename = 'new_movies.json'
        full_path = Path(project_root / 'data' / filename)

        with open(full_path, 'r', encoding='utf-8') as f:
            content = f.read()
            json_content = json.loads(content)

            return json_content

    except:
        raise FileNotFoundError

def get_movies_from_db():
    try:
        db = _db.get_db()
        res = db.execute('SELECT * FROM movies')
        rows = res.fetchall()

        data_json = crete_json_from_rows(rows)
        return data_json

    except:
        raise Exception 


def crete_json_from_rows(rows):
    json_object = []
    
    for row in rows:
        json_object.append(dict(row))

    return json_object

def get_ratings_from_db(user_id):
    try:
        db = _db.get_db()
        res = db.execute("SELECT * FROM ratings JOIN movies ON ratings.movie_id = movies.id WHERE user_id = ?", (user_id,))
    
        ratings = res.fetchall()
    
        if not ratings:
            rows = None
        else:
            rows = [dict(row) for row in ratings]
        
        return rows
    
    except:
        raise Exception


if __name__ == '__main__':
    get_movies_from_db()