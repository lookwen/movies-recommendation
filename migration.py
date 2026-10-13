import json
import sqlite3
from pathlib import Path

from backend.get_data import get_json_data
from backend.database import db as _db

database_path = Path('backend/database/users.db')

def migrate_movies():
    data = get_json_data()
    movies = data['movies']

    try:
        conn = sqlite3.connect(database_path)
        cursor = conn.cursor()
        cursor.execute("""      
            CREATE TABLE IF NOT EXISTS movies(
                id INTEGER PRIMARY KEY,
                title TEXT NOT NULL,
                genre TEXT NOT NULL,
                release_date TEXT,
                runtime TEXT NOT NULL,
                plot TEXT,
                average_rating TEXT NOT NULL
            )
    """)

        for movie in movies:
            cursor.execute(
                "INSERT INTO movies (id, title, genre, release_date, runtime, plot, average_rating) VALUES (?, ?, ?, ?, ?, ?, ?)",
                (movie['Id'], movie['Title'], movie['Genre'], movie['Released'], movie['Runtime'], movie['Plot'], movie['Ratings'][0]['Value'])
    )
            
        conn.commit()

    except:
        raise Exception
    finally:
        conn.close()


    
def insert_poster():
    data = get_json_data()
    movies = data['movies']

    try:
        conn = sqlite3.connect(database_path)
        cursor = conn.cursor()

        cursor.execute("ALTER TABLE movies ADD COLUMN poster TEXT")
        conn.commit()

        for m in movies:
            cursor.execute(
                "UPDATE movies SET poster = ? WHERE id = ?",
                (m['Poster'], m['Id'])
            )

        conn.commit()

    except:
        raise Exception
    finally:
        conn.close()


def create_ratings():
    try:
        conn = sqlite3.connect(database_path)
        cursor = conn.cursor()

        cursor.execute(
            """
                CREATE TABLE IF NOT EXISTS ratings(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    user_id INTEGER NOT NULL,
                    movie_id INTEGER NOT NULL,
                    value INTEGER CHECK (value > 0 AND value <= 5),
                    FOREIGN KEY (user_id) REFERENCES users(id),
                    FOREIGN KEY (movie_id) REFERENCES movies(id),
                    UNIQUE(user_id, movie_id)
                    )
            """)
        conn.commit()

    except:
        raise Exception
    finally:
        conn.close()


if __name__ == '__main__':
    #migrate_movies()
    #insert_poster()
    #create_ratings()

    print("Done")


