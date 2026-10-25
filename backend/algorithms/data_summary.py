from pathlib import Path
import json, os, sys
import numpy as np

project_root = Path(__file__).resolve().parent.parent.parent
sys.path.append(str(project_root))

from backend.get_data import *


def get_average_movie_ratings():
    movies = get_movies_from_db()
    movies_len = len(movies)
    
    movies_av = movies_len * [(0, 0)]
    
    for i in range(movies_len):
        ratings = get_ratings_by_movie_from_db(i)

        if not ratings:
            continue

        values = [r['value'] for r in ratings]

        movies_av[i] = (np.mean(values), len(values))
    
    movies_av.sort(key=lambda s: (-s[0], -s[1]))
    
    return movies_av

        



if __name__ == "__main__":
    pass

