
"""A simple task manager made with Python and Tkinter."""

import json
import tkinter as tk
from tkinter import messagebox
from pathlib import Path


DATA_FILE = Path.home() / ".task_manager" / "tasks.json"


def add_task(tasks, title):
    """Add a new task."""
    title = title.strip()

    if not title:
        raise ValueError("Task title cannot be empty.")

    task = {
        "title": title,
        "completed": False
    }

    tasks.append(task)
    return tasks


def delete_task(tasks, index):
    """Delete a task using its index."""
    if index < 0 or index >= len(tasks):
        raise IndexError("Invalid task index.")

    return tasks.pop(index)


def toggle_task(tasks, index):
    """Change a task's completion status."""
    if index < 0 or index >= len(tasks):
        raise IndexError("Invalid task index.")

    tasks[index]["completed"] = not tasks[index]["completed"]
    return tasks[index]


def load_tasks(path=DATA_FILE):
    """Load tasks from a JSON file."""
    path = Path(path)

    if not path.exists():
        return []

    with open(path, "r", encoding="utf-8") as file:
        tasks = json.load(file)

    if not isinstance(tasks, list):
        raise ValueError("Invalid task file.")

    for task in tasks:
        if (
            not isinstance(task, dict)
            or not isinstance(task.get("title"), str)
            or not isinstance(task.get("completed"), bool)
        ):
            raise ValueError("Invalid task data.")

    return tasks


def save_tasks(tasks, path=DATA_FILE):
    """Save tasks to a JSON file."""
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)

    with open(path, "w", encoding="utf-8") as file:
        json.dump(tasks, file, indent=2, ensure_ascii=False)


def main():
    """Start the task manager."""

    try:
        tasks = load_tasks()
    except (OSError, ValueError, json.JSONDecodeError) as error:
        messagebox.showerror("Error", f"Could not load tasks:\n{error}")
        tasks = []

    window = tk.Tk()
    window.title("Task Manager")
    window.geometry("720x520")
    window.minsize(560, 420)
    window.configure(bg="#0D0E14")

    heading = tk.Label(
        window,
        text="Task Manager",
        font=("Segoe UI", 23, "bold"),
        bg="#0D0E14",
        fg="white"
    )
    heading.pack(pady=20)

    task_entry = tk.Entry(
        window,
        font=("Segoe UI", 13),
        bg="#181A23",
        fg="white",
        insertbackground="white",
        relief="flat"
    )
    task_entry.pack(fill="x", padx=40, ipady=10)

    task_list = tk.Listbox(
        window,
        font=("Segoe UI", 12),
        bg="#181A23",
        fg="white",
        selectbackground="#7C5CFF",
        selectforeground="white",
        borderwidth=0,
        highlightthickness=0
    )
    task_list.pack(fill="both", expand=True, padx=40, pady=20)

    status = tk.Label(
        window,
        text="",
        font=("Segoe UI", 10),
        bg="#0D0E14",
        fg="#00E676"
    )
    status.pack(pady=5)

    def refresh_list():
        task_list.delete(0, tk.END)

        for task in tasks:
            mark = "✓" if task["completed"] else "○"
            task_list.insert(tk.END, f"{mark}  {task['title']}")

    def save_data():
        try:
            save_tasks(tasks)
            return True
        except OSError as error:
            messagebox.showerror("Save Error", str(error))
            return False

    def add_new_task():
        name = task_entry.get()

        try:
            add_task(tasks, name)
        except ValueError:
            messagebox.showwarning(
                "Empty Task",
                "Please enter a task first."
            )
            task_entry.focus_set()
            return

        if save_data():
            refresh_list()
            task_entry.delete(0, tk.END)
            status.config(text="Task added.")

    def get_selected_task():
        selected = task_list.curselection()

        if not selected:
            messagebox.showwarning(
                "No Selection",
                "Please select a task first."
            )
            return None

        return selected[0]

    def change_task_status():
        index = get_selected_task()

        if index is None:
            return

        toggle_task(tasks, index)

        if save_data():
            refresh_list()
            task_list.selection_set(index)
            status.config(text="Task updated.")

    def remove_task():
        index = get_selected_task()

        if index is None:
            return

        delete_task(tasks, index)

        if save_data():
            refresh_list()
            status.config(text="Task deleted.")

    buttons = tk.Frame(window, bg="#0D0E14")
    buttons.pack(pady=15)

    button_style = {
        "bg": "#7C5CFF",
        "fg": "white",
        "activebackground": "#6242E8",
        "activeforeground": "white",
        "font": ("Segoe UI", 10, "bold"),
        "relief": "flat",
        "padx": 15,
        "pady": 10,
        "cursor": "hand2"
    }

    tk.Button(
        buttons,
        text="Add Task",
        command=add_new_task,
        **button_style
    ).grid(row=0, column=0, padx=5)

    tk.Button(
        buttons,
        text="Complete / Undo",
        command=change_task_status,
        **button_style
    ).grid(row=0, column=1, padx=5)

    tk.Button(
        buttons,
        text="Delete Task",
        command=remove_task,
        **button_style
    ).grid(row=0, column=2, padx=5)

    task_entry.bind("<Return>", lambda event: add_new_task())

    refresh_list()
    window.mainloop()


if __name__ == "__main__":
    main()
