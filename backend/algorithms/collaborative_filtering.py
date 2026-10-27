import sys
from pathlib import Path
import numpy as np
import math

project_root = Path(__file__).resolve().parent.parent.parent
sys.path.append(str(project_root))

from backend.get_data import *

def create_movie_user_matrix(users, movies, ratings):
    matrix = np.full((len(users), len(movies)), np.nan)

    for r in ratings:
        user_id = r['user_id']
        movie_id = r['user_id']
        value = r['value']

        matrix[user_id, movie_id] = value

        return matrix


def cosine_similarity(movie_a, movie_b):
    suma = 0
    sum_div_a = 0
    sum_div_b = 0
    counter = 0
    for i in range(len(movie_a)):
        if not np.isnan(movie_a[i]) and not np.isnan(movie_b[i]):
            suma += movie_a[i]*movie_b[i]
            sum_div_a += movie_a[i]**2
            sum_div_b += movie_b[i]**2
            counter += 1
        
    divider = math.sqrt(sum_div_a) * math.sqrt(sum_div_b)
    
    if divider == 0 or counter < 3:
        return 0.0

    return suma / divider


    



def create_similarity_matrix(user_movie_matrix, all_movies):
    matrix = np.full((len(all_movies), len(all_movies)), dtype=float)

    np.fill_diagonal(matrix, 1.0)

    for i in range(len(all_movies)):
        for j in range(i+1, len(all_movies)):
            movie_a = user_movie_matrix[:, i]
            movie_b = user_movie_matrix[:, j]

            similarity = cosine_similarity(movie_a, movie_b)

            matrix[i, j] = similarity
            matrix[j, i] = similarity

    return matrix





def recommend_algorithm():
    users = get_all_users_from_db()
    movies = get_movies_from_db()
    ratings = get_all_ratings_from_db()

    movie_user_matrix = create_movie_user_matrix(users, movies, ratings)

    similarity_matrix = create_similarity_matrix(movie_user_matrix, movies)

    




    