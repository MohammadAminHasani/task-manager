
# Task Manager

**Author:** MohammadAmin Hasani  
**Language:** Python  
**GUI:** Tkinter

## Video Demo

[Watch the project demonstration](YOUR_VIDEO_LINK)

## Description

Task Manager is a desktop application built with Python and Tkinter to help users organize their everyday tasks. It provides a simple dark-themed graphical interface where users can add tasks, mark them as completed or incomplete, and delete tasks.

I developed this project to combine several Python concepts in one practical application, including functions, data structures, file handling, exception handling, graphical user interfaces, and automated testing.

## Features

- **Add Tasks:** Create tasks by entering a title. Empty titles are not accepted.
- **Complete or Undo:** Change a task's completion status whenever needed.
- **Delete Tasks:** Remove selected tasks from the list.
- **Persistent Storage:** Save tasks in a JSON file so they remain available after closing the application.
- **Input Validation:** Handle empty task titles and invalid task indexes.
- **User Feedback:** Display messages when tasks are added, updated, or deleted, and when an action requires a selection.

## How It Works

Each task is represented by a Python dictionary containing two fields: `title` and `completed`. The application keeps tasks in a list and uses separate functions to add, delete, and update them.

Task data is stored in a JSON file at:

`~/.task_manager/tasks.json`

When the application starts, it loads previously saved tasks. If no data file exists, it starts with an empty list. Changes are saved to the JSON file so task information persists between sessions.

The graphical interface is built with Tkinter. It displays the task list and provides buttons for the main operations. The core task-management functions are kept separate from the interface, making them easier to test independently.

## Project Files

- `project.py`: Contains the task-management functions, data storage logic, and graphical interface.
- `Taskmanager.py`: Provides an alternative entry point for launching the application.
- `test_project.py`: Contains automated tests written with pytest.
- `task.ico`: Application icon.
- `Taskmanager.exe`: Previously built Windows executable.

## Requirements

- Python 3
- Tkinter
- pytest (only required for running tests)

## Installation and Usage

Clone or download the repository, open a terminal in the project directory, and run:

```bash
python project.py
```

Alternatively, launch the application with:

```bash
python Taskmanager.py
```

Enter a task in the input field and use the available buttons to manage your tasks.

## Running Tests

Install pytest if necessary:

```bash
python -m pip install pytest
```

Run the test suite:

```bash
python -m pytest -q
```

The seven tests cover task creation, empty-title validation, task deletion, invalid indexes, completion status changes, saving and loading JSON data, and handling a missing data file.

## Design Decisions

I separated the application's core functions from its graphical interface to make the code more organized and easier to test. JSON was selected as a lightweight, human-readable format for storing task data without requiring a database.

Using pytest also allowed me to verify the main operations independently of the graphical interface.
