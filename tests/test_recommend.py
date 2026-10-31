import numpy as np
import pytest, sys
from pathlib import Path

project_root = Path(__file__).resolve().parent.parent
sys.path.append(str(project_root))

from backend.algorithms.collaborative_filtering import reccomend_movies


def test_no_recommend_rated_movies():
    similarity_matrix = np.eye(4)
    user_movie_matrix = np.array([[5, np.nan, 3, np.nan]])

    recommended = reccomend_movies(0, user_movie_matrix, similarity_matrix)

    recommended_ids = {movie["movie_id"] for movie in recommended}

    assert recommended_ids == {1, 3}
    assert len(recommended) == 2



def test_default_prediction_when_no_similarity():
    similarity_matrix = np.eye(4)
    user_movie_matrix = np.array([[5, 2, np.nan, np.nan]])

    recommended = reccomend_movies(0, user_movie_matrix, similarity_matrix)

    assert all(movie["predicted_value"] == pytest.approx(3.0) for movie in recommended) and len(recommended) == 2


def test_prediction_with_similarity():
    user_movie_matrix = np.array([[5, 1, np.nan]])
    similarity_matrix = np.array([
        [1.0, 0.0, 0.8],
        [0.0, 1.0, 0.4],
        [0.8, 0.4, 1.0]
    ])

    recommended = reccomend_movies(0, user_movie_matrix, similarity_matrix)
    
    assert len(recommended) == 1
    assert recommended[0]["movie_id"] == 2
    assert pytest.approx(3.66, 0.01) == recommended[0]['predicted_value']