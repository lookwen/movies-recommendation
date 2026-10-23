from werkzeug.security import generate_password_hash, check_password_hash
import json, sqlite3


def get_test_data(filename):
    try:
        with open(filename, "r", encoding='utf-8') as f:
            content = f.read()
            json_content = json.loads(content)
    
            return json_content
    except:
        raise Exception


def add_id_into_ratings():
    try:
        with open("ratings.json", "r", encoding='utf-8') as f:
            content = f.read()
            json_content = json.loads(content)


        for i in range(len(json_content['ratings'])):
            json_content['ratings'][i]['id'] = i
        
        for i in range(len(json_content['ratings'])):
            json_content['ratings'][i]['user_id'] = json_content['ratings'][i]['user_id']-2



        with open("new_ratings.json", "w", encoding='utf-8') as f:
            json.dump(json_content, f, ensure_ascii=False, indent=4)

        
    except:
        raise Exception

def insert_into_database_test_data():
    users_json = get_test_data("users.json")
    ratings_json = get_test_data("new_ratings.json")

    try:
        sqlConn = sqlite3.connect("users.db")
        cursor = sqlConn.cursor()

        # for u in users_json['users']:
        #     cursor.execute("INSERT INTO user VALUES(?, ?, ?, ?)", (u['id'], u['username'], u['email'], u['password']))

        for r in ratings_json['ratings']:
            cursor.execute("INSERT INTO ratings VALUES(?, ?, ?, ?)", (r['id'], r['user_id'], r['movie_id'], r['value']))

        sqlConn.commit()
        sqlConn.close()

    except:
        raise Exception

    


if __name__ == "__main__":
    insert_into_database_test_data()
    pass
