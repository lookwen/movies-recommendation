import json, os, sqlite3
from pathlib import Path
import sys

project_root = Path(__file__).resolve().parent.parent
sys.path.append(str(project_root))

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


def delete_users():
    sqliteConnection = sqlite3.connect('database/users.db')
    cursor = sqliteConnection.cursor()
    cursor.execute("DELETE from user")
    cursor.execute("DELETE from ratings")
    sqliteConnection.commit()
    cursor.close()


def update_movies():
    try:
        sqliteConnection = sqlite3.connect('database/users.db')
        cursor = sqliteConnection.cursor()
        json_data = get_json_data()
        cursor.execute("ALTER TABLE movies ADD COLUMN director TEXT")
        cursor.execute("ALTER TABLE movies ADD COLUMN writer TEXT")
        cursor.execute("ALTER TABLE movies ADD COLUMN actors TEXT")
    
        for m in json_data['movies']:
            cursor.execute("UPDATE movies SET director = ? WHERE id = ?", (m['Director'], m["Id"]))
            cursor.execute("UPDATE movies SET writer = ? WHERE id = ?", (m['Writer'], m["Id"]))
            cursor.execute("UPDATE movies SET actors = ? WHERE id = ?", (m['Actors'], m["Id"]))
        
        sqliteConnection.commit()
        cursor.close()
    except:
        raise Exception




if __name__ == '__main__':
    pass
