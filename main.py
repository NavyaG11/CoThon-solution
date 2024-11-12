# main.py

from task_manager import TaskManager

def display_menu():
    print("\n--- To-Do List ---")
    print("1. View all tasks")
    print("2. Add a new task")
    print("3. Delete a task")
    print("4. Exit")

def main():
    task_manager = TaskManager()

    while True:
        display_menu()
        choice = input("Choose an option (1-4): ")

        if choice == "1":
            tasks = task_manager.get_tasks()
            if tasks:
                print("\nYour Tasks:")
                for idx, task in enumerate(tasks, start=1):
                    print(f"{idx}. {task}")
            else:
                print("No tasks found.")
        
        elif choice == "2":
            task = input("Enter the new task: ")
            task_manager.add_task(task)
            print("Task added successfully.")
        
        elif choice == "3":
            tasks = task_manager.get_tasks()
            if tasks:
                print("\nSelect a task to delete:")
                for idx, task in enumerate(tasks, start=1):
                    print(f"{idx}. {task}")
                try:
                    delete_index = int(input("Task number to delete: ")) - 1
                    task_manager.delete_task(delete_index)
                    print("Task deleted successfully.")
                except (ValueError, IndexError):
                    print("Invalid selection. Please try again.")
            else:
                print("No tasks to delete.")
        
        elif choice == "4":
            print("Exiting the To-Do List. Goodbye!")
            break

        else:
            print("Invalid choice. Please choose between 1 and 4.")

if __name__ == "__main__":
    main()
