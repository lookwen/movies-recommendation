import sqlite3
import os

from flask import current_app, g


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

    with open(schema_path, 'r', encoding='utf-8') as f:
        db.executescript(f.read())


def init_app(app):
    app.teardown_appcontext(close_db)

    database_path = app.config['DATABASE']

    os.makedirs(os.path.dirname(database_path), exist_ok=True)

    if not os.path.exists(database_path):
        with app.app_context():
            init_db()