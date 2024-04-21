#This file was created by ChatGPT4 on Apr 21st 2024
#This is intended as a demonstration of the Codey chatbot.
# File: pyquerydesk.py
# Description: A simple task management system for demonstrating the PyQueryDesk project.

class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)
        return f"Task added: {task}"

    def list_tasks(self):
        return "\n".join(self.tasks) if self.tasks else "No tasks found."

    def delete_task(self, task):
        if task in self.tasks:
            self.tasks.remove(task)
            return f"Task removed: {task}"
        return "Task not found."

def main():
    tm = TaskManager()
    print("Welcome to PyQueryDesk - Your simple task manager")
    while True:
        print("\nOptions: add, list, delete, exit")
        action = input("What would you like to do? ").strip().lower()
        if action == 'add':
            task = input("Enter a task to add: ")
            print(tm.add_task(task))
        elif action == 'list':
            print("Current tasks:")
            print(tm.list_tasks())
        elif action == 'delete':
            task = input("Enter a task to delete: ")
            print(tm.delete_task(task))
        elif action == 'exit':
            print("Exiting PyQueryDesk. Goodbye!")
            break
        else:
            print("Invalid option. Please choose from add, list, delete, exit.")

if __name__ == "__main__":
    main()
