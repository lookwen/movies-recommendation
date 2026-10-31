import sqlite3
import os, sys
from pathlib import Path

project_root = Path(__file__).resolve().parent.parent.parent
sys.path.append(str(project_root))

from flask import current_app, g
from backend.database.insert_test_data import get_test_data


def get_db():
    if 'db' not in g:
        g.db = sqlite3.connect(
            current_app.config['DATABASE']
        )
        g.db.row_factory = sqlite3.Row

    return g.db


def close_db(e=None):
    db = g.pop('db', None)

    if db is not None:
        db.close()


def init_db():
    db = get_db()

    schema_path = os.path.join(
        os.path.dirname(__file__),
        'schema.sql'
    )

    try:
        with open(schema_path, 'r', encoding='utf-8') as f:
            db.executescript(f.read())

        path_users = project_root / 'data/new_users.json'
        path_ratings = project_root / 'data/ratings_recommendation_test.json'
        path_movies = project_root / 'data/new_movies.json'

        users_json = get_test_data(path_users)
        ratings_json = get_test_data(path_ratings)
        movies_json = get_test_data(path_movies)

        for m in movies_json['movies']:
            db.execute("""
                INSERT INTO movies (
                    id, title, genre, release_date, runtime,
                    plot, poster, average_rating, director, writer, actors
                )
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """, (
                m['Id'],
                m['Title'],
                m['Genre'],
                m['Released'],
                m['Runtime'],
                m['Plot'],
                m['Poster'],
                m['imdbRating'],
                m['Director'],
                m['Writer'],
                m['Actors']
            ))

            
        for u in users_json['users']:
            db.execute("INSERT INTO users VALUES(?, ?, ?, ?)", (u['id'], u['username'], u['email'], u['password']))
        
        for r in ratings_json['ratings']:
            db.execute("INSERT INTO ratings VALUES(?, ?, ?, ?)", (r['id'], r['user_id'], r['movie_id'], r['value']))

        db.commit()

    except:
        raise Exception

def init_app(app):
    app.teardown_appcontext(close_db)

    database_path = app.config['DATABASE']

    os.makedirs(os.path.dirname(database_path), exist_ok=True)

    if not os.path.exists(database_path):
        with app.app_context():
            init_db()