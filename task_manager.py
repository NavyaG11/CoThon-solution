# task_manager.py

from storage import Storage

class TaskManager:
    def __init__(self):
        self.storage = Storage()

    def get_tasks(self):
        return self.storage.load_tasks()

    def add_task(self, task):
        tasks = self.get_tasks()
        tasks.append(task)
        self.storage.save_tasks(tasks)

    def delete_task(self, index):
        tasks = self.get_tasks()
        if 0 <= index < len(tasks):
            tasks.pop(index)
            self.storage.save_tasks(tasks)
