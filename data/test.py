import json


def get_json_data(filename):
    with open(filename, "r", encoding='utf-8') as f:
        data = json.load(f)
        return data


movies = get_json_data('movies.json')

for i in range(len(movies['movies'])):
    movies['movies'][i]['Id'] = i

def save_json_data(filename):
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(movies, f)


save_json_data("new_movies.json")
