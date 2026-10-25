from pathlib import Path
import json, os, sys
import numpy as np

project_root = Path(__file__).resolve().parent.parent.parent
sys.path.append(str(project_root))

from backend.get_data import *


def print_ratings():
    ratings_0 = get_all_users_from_db()
        



if __name__ == "__main__":
    print_ratings()

