import json

from backend.get_data import get_json_data
from backend.database import db



def migrate_movies():
    data = get_json_data()
    movies = data['movies']
    


if __name__ == '__main__':
    migrate_movies()


