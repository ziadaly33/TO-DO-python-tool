# main.py

import os

# ===== Logo Function =====
def show_logo():
    logo = r"""
 _______   ____         ____   _____  
|__   __| |  _ \       |  _ \ |  __ \ 
   | |    | | | ||_____| | | || |  | |
   | |    | | | ||_____| | | || |  | |
   | |    | |_| |      | |_| || |__| |
   |_|    |____/        \___/ |_____/ 

                TO DO Tool
           © 2025 — Ziad Ali
"""
    print(logo + "\n")

# ===== Task File Path =====
TASKS_FILE = "tasks.txt"

# ===== Load Tasks =====
def load_tasks():
    try:
        with open(TASKS_FILE, "r") as file:
            return [line.strip() for line in file.readlines()]
    except FileNotFoundError:
        return []

# ===== Save Tasks =====
def save_tasks(tasks):
    with open(TASKS_FILE, "w") as file:
        for task in tasks:
            file.write(task + "\n")

# ===== Add Task =====
def add_task():
    task = input("Enter a new task: ")
    tasks = load_tasks()
    tasks.append(task)
    save_tasks(tasks)
    print("Task added.\n")

# ===== View Tasks =====
def view_tasks():
    tasks = load_tasks()
    if not tasks:
        print("No tasks found.\n")
    else:
        print("Your To-Do List:")
        for idx, task in enumerate(tasks, 1):
            print(f"{idx}. {task}")
        print()

# ===== Delete Task =====
def delete_task():
    tasks = load_tasks()
    view_tasks()
    try:
        num = int(input("Enter task number to delete: "))
        if 1 <= num <= len(tasks):
            removed = tasks.pop(num - 1)
            save_tasks(tasks)
            print(f"Removed: {removed}\n")
        else:
            print("Invalid number.\n")
    except ValueError:
        print("Please enter a valid number.\n")

# ===== Main Menu =====
def main():
    show_logo()
    while True:
        print("To-Do List App")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Delete Task")
        print("4. Exit")
        choice = input("Choose an option: ")
        if choice == "1":
            view_tasks()
        elif choice == "2":
            add_task()
        elif choice == "3":
            delete_task()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice.\n")

# ===== Run Program =====
if __name__ == "__main__":
    main()
