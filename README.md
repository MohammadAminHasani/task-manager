# Task Manager

A desktop task-management application built with **Python** and **Tkinter**. It provides a simple dark-themed interface for keeping track of everyday tasks. Users can add tasks, mark them as complete or incomplete, and delete tasks they no longer need.

## Features

- Add tasks with a title; empty task names are rejected.
- Mark a task as complete and switch it back to incomplete.
- Delete a selected task.
- Save tasks to a JSON file so they are still available after the application closes.
- Display clear status messages and handle missing selections.
- Keep task-management functions separate from the graphical interface so they can be tested independently.

## How it works

The application stores each task as a dictionary containing a `title` and a Boolean `completed` value. The functions in `project.py` manage task creation, deletion, completion status, and JSON persistence. The Tkinter interface calls these functions and refreshes the task list when the data changes.

The data file is stored at `~/.task_manager/tasks.json` inside the current user's home directory. If the file does not exist yet, the application starts with an empty task list.

## Project files

- `project.py`: core task functions and the `main()` function that starts the GUI.
- `Taskmanager.py`: small launcher for the application.
- `test_project.py`: automated tests for the task functions and file storage.
- `Taskmanager.exe`: previously built Windows executable; rebuild it from the updated source before distributing a current executable.
- `task.ico`: application icon asset.

## Requirements

- Python 3.10 or newer
- Tkinter (included with most standard Python installations)
- pytest (only needed to run the tests)

## Run the application

```bash
python project.py
```

You can also run `python Taskmanager.py`.

## Run the tests

Install pytest if it is not already installed:

```bash
python -m pip install pytest
```

Then run:

```bash
python -m pytest -q
```

## Demo video

Before submitting to CS50P, replace the placeholder below with the public URL of your own demonstration video. Show the application working and explain the main design decisions. Keep the video within the course's time limit.

Video URL: TODO

## Author

MohammadAmin
