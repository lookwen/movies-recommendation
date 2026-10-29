import numpy as np
import pytest, sys
from pathlib import Path

project_root = Path(__file__).resolve().parent.parent
sys.path.append(str(project_root))

from backend.algorithms.collaborative_filtering import cosine_similarity

def test_identical_movies():
    movie_a = np.array([5, 4, 3, 2, 1])
    movie_b = np.array([5, 4, 3, 2, 1])

    result = cosine_similarity(movie_a, movie_b)

    assert result == pytest.approx(1.0)


def test_less_than_three_common_ratings():
    movie_a = np.array([5, 4, np.nan, np.nan])
    movie_b = np.array([5, 4, 2, np.nan])

    result = cosine_similarity(movie_a, movie_b)

    assert result == 0.0


def test_no_common_ratings():
    movie_a = np.array([5, 4, np.nan, np.nan])
    movie_b = np.array([np.nan, np.nan, 4, 5])

    result = cosine_similarity(movie_a, movie_b)

    assert result == 0.0


def test_opposite_preferences():
    movie_a = np.array([5, 4, 1, 2])
    movie_b = np.array([1, 2, 5, 4])

    result = cosine_similarity(movie_a, movie_b)

    assert result == pytest.approx(-1.0)