#!/usr/bin/env python3
import json
import os
from dataclasses import dataclass, asdict
from typing import List, Optional

DATA_FILE = "tasks.json"

@dataclass
class Task:
    title: str
    description: str
    category: str
    completed: bool = False

    def mark_completed(self):
        self.completed = True

def load_tasks() -> List[Task]:
    if not os.path.exists(DATA_FILE):
        return []
    try:
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            raw = json.load(f)
            return [Task(**item) for item in raw]
    except (json.JSONDecodeError, FileNotFoundError):
        return []

def save_tasks(tasks: List[Task]) -> None:
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump([asdict(t) for t in tasks], f, indent=2, ensure_ascii=False)

def print_task(idx: int, task: Task) -> None:
    status = "✅" if task.completed else "⏳"
    print(f"[{idx}] {status} {task.title}  (Category: {task.category})")
    print(f"     {task.description}")

def list_tasks(tasks: List[Task], *, only_category: Optional[str] = None, show_all: bool = True) -> None:
    if not tasks:
        print("No tasks found.")
        return
    filtered = tasks
    if only_category:
        filtered = [t for t in tasks if t.category.lower() == only_category.lower()]
        if not filtered:
            print(f"No tasks in category '{only_category}'.")
            return
    for i, t in enumerate(filtered):
        if show_all or not t.completed:
            print_task(i, t)

def add_task(tasks: List[Task]) -> None:
    title = input("Title: ").strip()
    if not title:
        print("Title cannot be empty.")
        return
    description = input("Description: ").strip()
    category = input("Category (e.g., Work, Personal, Urgent): ").strip() or "General"
    tasks.append(Task(title=title, description=description, category=category))
    print("Task added.")

def edit_task(tasks: List[Task]) -> None:
    if not tasks:
        print("No tasks to edit.")
        return
    try:
        idx = int(input("Enter task index to edit: "))
        t = tasks[idx]
    except (ValueError, IndexError):
        print("Invalid index.")
        return
    new_title = input(f"New title (leave blank to keep '{t.title}'): ").strip()
    new_desc = input(f"New description (leave blank to keep current): ").strip()
    new_cat = input(f"New category (leave blank to keep '{t.category}'): ").strip()
    if new_title:
        t.title = new_title
    if new_desc:
        t.description = new_desc
    if new_cat:
        t.category = new_cat
    print("Task updated.")

def mark_completed(tasks: List[Task]) -> None:
    if not tasks:
        print("No tasks to complete.")
        return
    try:
        idx = int(input("Enter task index to mark completed: "))
        tasks[idx].mark_completed()
        print("Task marked as completed.")
    except (ValueError, IndexError):
        print("Invalid index.")

def delete_task(tasks: List[Task]) -> None:
    if not tasks:
        print("No tasks to delete.")
        return
    try:
        idx = int(input("Enter task index to delete: "))
        removed = tasks.pop(idx)
        print(f"Deleted task: {removed.title}")
    except (ValueError, IndexError):
        print("Invalid index.")

def search_tasks(tasks: List[Task]) -> None:
    term = input("Search term (in title): ").strip().lower()
    if not term:
        print("Search term cannot be empty.")
        return
    results = [(i, t) for i, t in enumerate(tasks) if term in t.title.lower()]
    if not results:
        print("No matching tasks found.")
        return
    for i, t in results:
        print_task(i, t)

def menu():
    print("\n==== Personal To-Do List ====")
    print("1. Add Task")
    print("2. View All Tasks")
    print("3. View Tasks by Category")
    print("4. Search Tasks by Title")
    print("5. Edit Task")
    print("6. Mark Task Completed")
    print("7. Delete Task")
    print("8. Save & Exit")

def main():
    tasks = load_tasks()
    while True:
        menu()
        choice = input("Choose an option (1-8): ").strip()
        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            list_tasks(tasks)
        elif choice == "3":
            cat = input("Enter category to filter: ").strip()
            list_tasks(tasks, only_category=cat)
        elif choice == "4":
            search_tasks(tasks)
        elif choice == "5":
            edit_task(tasks)
        elif choice == "6":
            mark_completed(tasks)
        elif choice == "7":
            delete_task(tasks)
        elif choice == "8":
            save_tasks(tasks)
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 8.")

if __name__ == "__main__":
    main()
