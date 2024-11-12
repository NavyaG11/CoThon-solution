# storage.py

import json
import os

class Storage:
    def __init__(self, filename="data/tasks.json"):
        self.filename = filename
        os.makedirs(os.path.dirname(self.filename), exist_ok=True)
        if not os.path.exists(self.filename):
            self.save_tasks([])

    def load_tasks(self):
        try:
            with open(self.filename, "r") as file:
                return json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            return []

    def save_tasks(self, tasks):
        with open(self.filename, "w") as file:
            json.dump(tasks, file, indent=4)
