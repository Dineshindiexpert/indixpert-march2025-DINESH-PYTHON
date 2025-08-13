import json
import os

class User:
    def __init__(self, username, role):
        self.username = username
        self.role = role

    @staticmethod
    def load_users(filepath):
        if not os.path.exists(filepath):
            return []
        with open(filepath, 'r') as f:
            try:
                return json.load(f)
            except json.JSONDecodeError:
                return []

    @staticmethod
    def authenticate(username, password, filepath, required_role=None):
        users = User.load_users(filepath)
        for user in users:
            if user['username'] == username and user['password'] == password:
                if required_role is None or user['role'] == required_role:
                    return User(username, user['role'])
        return None 