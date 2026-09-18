import json


def get_json_data(filename):
    with open(filename, "r", encoding='utf-8') as f:
        data = json.load(f)
        return data


movies = get_json_data('movies.json')

for m in movies['movies']:
    m['Genre'] = m['Genre'].replace(",", " ").split()
    print(m['Genre'])