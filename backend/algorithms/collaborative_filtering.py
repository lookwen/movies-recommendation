import sys
from pathlib import Path
import numpy as np

project_root = Path(__file__).resolve().parent.parent.parent
sys.path.append(str(project_root))

from backend.get_data import *

def create_movie_user_matrix():
    users = get_all_users_from_db()
    movies = get_movies_from_db()
    ratings = get_all_ratings_from_db()

    matrix = np.full((len(users), len(movies)), np.nan)

    for r in ratings:
        user_id = r['user_id']
        movie_id = r['user_id']
        value = r['value']

        matrix[user_id, movie_id] = value

        return matrix
    
