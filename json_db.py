

import json
import os

USERS_FILE = "users.json"

def load_users():
    if not os.path.exists(USERS_FILE):
        return []
    with open(USERS_FILE, "r") as file:
        return json.load(file)

def save_user(user):
    users = load_users()
    users.append(user)
    with open(USERS_FILE, "w") as file:
        json.dump(users, file, indent=4)

def find_user(username, password):
    users = load_users()
    for user in users:
        if user["username"] == username and user["password"] == password:
            return user
    return None

def username_exists(username):
    users = load_users()
    return any(user["username"] == username for user in users)
