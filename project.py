
import tkinter as tk
from tkinter import messagebox
import json
from pathlib import Path

file_path = Path.home() / ".task_manager" / "tasks.json"


def add_task(tasks, task_name):
    task_name = task_name.strip()

    if not task_name:
        raise ValueError("Task title cannot be empty.")

    tasks.append({
        "title": task_name,
        "completed": False
    })
    return tasks

def delete_task(tasks, number):
    if number < 0 or number >= len(tasks):
        raise IndexError("Invalid task number.")

    return tasks.pop(number)


def complete_task(tasks, number):
    if number < 0 or number >= len(tasks):
        return False

    tasks[number]["completed"] = not tasks[number]["completed"]
    return True

def toggle_task(tasks, number):
    if number < 0 or number >= len(tasks):
        raise IndexError("Invalid task number.")

    tasks[number]["completed"] = not tasks[number]["completed"]
    return tasks[number]


def complete_task(tasks, number):
    return toggle_task(tasks, number)


def load_tasks(path=file_path):
    path = Path(path)

    if not path.exists():
        return []

    with open(path, "r", encoding="utf-8") as file:
        return json.load(file)

def save_tasks(tasks, path=file_path):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)

    with open(path, "w", encoding="utf-8") as file:
        json.dump(tasks, file, ensure_ascii=False, indent=2)


def main():
    tasks = load_tasks()

    window = tk.Tk()
    window.title("Task Manager")
    window.geometry("720x520")
    window.configure(bg="#0D0E14")

    title = tk.Label(
        window,
        text="Task Manager",
        font=("Segoe UI", 23, "bold"),
        bg="#0D0E14",
        fg="white"
    )
    title.pack(pady=20)

    task_entry = tk.Entry(
        window,
        font=("Segoe UI", 13),
        bg="#181A23",
        fg="white",
        insertbackground="white"
    )
    task_entry.pack(fill="x", padx=40, ipady=10)

    task_list = tk.Listbox(
        window,
        font=("Segoe UI", 12),
        bg="#181A23",
        fg="white",
        selectbackground="#7C5CFF",
        borderwidth=0
    )
    task_list.pack(fill="both", expand=True, padx=40, pady=20)

    status = tk.Label(
        window,
        text="",
        bg="#0D0E14",
        fg="#00E676"
    )
    status.pack(pady=5)

    def show_tasks():
        task_list.delete(0, tk.END)

        for task in tasks:
            if task["completed"]:
                text = "✓  " + task["title"]
            else:
                text = "○  " + task["title"]

            task_list.insert(tk.END, text)

    def add_new_task():
        name = task_entry.get()

        if not add_task(tasks, name):
            messagebox.showwarning("Warning", "Please enter a task first.")
            task_entry.focus_set()
            return

        save_tasks(tasks)
        show_tasks()
        task_entry.delete(0, tk.END)
        status.config(text="Task added.")

    def get_selected():
        selected = task_list.curselection()

        if not selected:
            messagebox.showwarning("Warning", "Please select a task first.")
            return None

        return selected[0]

    def change_status():
        number = get_selected()

        if number is None:
            return

        complete_task(tasks, number)
        save_tasks(tasks)
        show_tasks()
        task_list.selection_set(number)
        status.config(text="Task updated.")

    def remove_task():
        number = get_selected()

        if number is None:
            return

        delete_task(tasks, number)
        save_tasks(tasks)
        show_tasks()
        status.config(text="Task deleted.")

    buttons = tk.Frame(window, bg="#0D0E14")
    buttons.pack(pady=15)

    button_style = {
        "bg": "#7C5CFF",
        "fg": "white",
        "font": ("Segoe UI", 10, "bold"),
        "relief": "flat",
        "padx": 15,
        "pady": 10
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
        command=change_status,
        **button_style
    ).grid(row=0, column=1, padx=5)

    tk.Button(
        buttons,
        text="Delete Task",
        command=remove_task,
        **button_style
    ).grid(row=0, column=2, padx=5)

    task_entry.bind("<Return>", lambda event: add_new_task())

    show_tasks()
    window.mainloop()


if __name__ == "__main__":
    main()
