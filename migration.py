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
        conn.close()

    except:
        raise Exception

    
        

    


if __name__ == '__main__':
    #migrate_movies()
    print("Done")


