import json
import os

class UserManager:
    def __init__(self, filename="users.json"):
        self.filename = filename
        self.users = self.load_users()

    def load_users(self):
        if not os.path.exists(self.filename):
            return {}
        with open(self.filename, "r") as f:
            return json.load(f)

    def save_users(self):
        with open(self.filename, "w") as f:
            json.dump(self.users, f, indent=4)

    def add_user(self, email, password):
        if email in self.users:
            return False  # user already exists
        self.users[email] = password
        self.save_users()
        return True

    def verify_user(self, email, password):
        return self.users.get(email) == password
