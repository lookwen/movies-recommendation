import json, os
from pathlib import Path
import sys

project_root = Path(__file__).resolve().parent.parent

def get_json_data():
    try:
        filename = 'movies.json'
        full_path = Path(project_root / 'data' / filename)

        with open(full_path, 'r', encoding='utf-8') as f:
            content = f.read()
            json_content = json.loads(content)

            return json_content

    except:
        raise Exception



if __name__ == '__main__':
    data = get_json_data()
    print(data)