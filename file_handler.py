import json
from user import User

def save_users(users):
    with open("data/users.json", "w") as file:
        json.dump(users, file)

def load_users():
    try:
        with open("data/users.json", "r") as file:
            data = json.load(file)
            return {username: User.from_dict(user_data) for username, user_data in data.items()}
    except FileNotFoundError:
        return {}

