import sys
from pathlib import Path
import numpy as np
import math

project_root = Path(__file__).resolve().parent.parent.parent
sys.path.append(str(project_root))

from backend.get_data import *

def create_user_movie_matrix(users, movies, ratings):
    matrix = np.full((len(users), len(movies)), np.nan)

    for r in ratings:
        user_id = r['user_id']
        movie_id = r['movie_id']
        value = r['value']

        matrix[user_id, movie_id] = value

    return matrix


def cosine_similarity(movie_a, movie_b):
    mask = ~np.isnan(movie_a) & ~np.isnan(movie_b)

    if np.count_nonzero(mask) < 3:
        return 0.0

    a = movie_a[mask] - 3
    b = movie_b[mask] - 3

    denominator = np.linalg.norm(a) * np.linalg.norm(b)

    if denominator == 0:
        return 0.0

    return float(np.dot(a, b) / denominator)


    

def create_similarity_matrix(user_movie_matrix, all_movies):
    matrix = np.zeros((len(all_movies), len(all_movies)), dtype=float)

    np.fill_diagonal(matrix, 1.0)

    for i in range(len(all_movies)):
        for j in range(i+1, len(all_movies)):
            movie_a = user_movie_matrix[:, i]
            movie_b = user_movie_matrix[:, j]

            similarity = cosine_similarity(movie_a, movie_b)

            matrix[i, j] = similarity
            matrix[j, i] = similarity

    return matrix




def reccomend_movies(user_id, user_movie_matrix, similarity_matrix):
    user_ratings = user_movie_matrix[user_id, :]

    not_rated = np.where(np.isnan(user_ratings))[0]
    
    if len(not_rated) == 0:
        return []

    not_rated_movies = []
    center_point = 3
    mask = ~np.isnan(user_ratings)
    ratings = user_ratings[mask]
    for movie_id in range(len(not_rated)):
        weights = similarity_matrix[not_rated[movie_id]][mask]
        
        numerator = np.dot(weights, ratings - 3)
        denominator = np.sum(np.abs(weights))

        if denominator == 0:
            not_rated_movies.append({"movie_id" : int(not_rated[movie_id]),"predicted_value" : float(3.0)})
        else:
            not_rated_movies.append({"movie_id" : int(not_rated[movie_id]), "predicted_value" : float(np.clip(3 + numerator/denominator, 1, 5))})
        
    not_rated_movies.sort(
        key=lambda movie: movie["predicted_value"],
        reverse=True
    )

    return not_rated_movies



def recommend_algorithm(user_id):
    if user_id is None:
        return []
    
    users = get_all_users_from_db()
    movies = get_movies_from_db()
    ratings = get_all_ratings_from_db()

    user_movie_matrix = create_user_movie_matrix(users, movies, ratings)

    similarity_matrix = create_similarity_matrix(user_movie_matrix, movies)

    all_recommendation = reccomend_movies(user_id, user_movie_matrix, similarity_matrix)

    return [movie["movie_id"] for movie in all_recommendation[:10]]








    