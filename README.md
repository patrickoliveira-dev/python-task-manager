# Task Manager

A command-line task management application developed in Python.

This project was created as a practical study of software development fundamentals, including Object-Oriented Programming (OOP), data persistence, modular architecture, error handling, data processing, sorting algorithms, and software refactoring.

## Features

### Task Management

* Create tasks
* List all tasks
* Edit tasks
* Delete tasks
* Mark tasks as completed

### Task Information

* Title
* Description
* Priority levels (Low, Medium, High)
* Creation date and time
* Completion date and time

### Search and Filtering

* Search tasks by title or description
* Filter all tasks
* Filter pending tasks
* Filter completed tasks
* Filter by priority

### Sorting

* Sort by title
* Sort by creation date
* Sort by priority
* Sort by priority and creation date

### Statistics

* Total number of tasks
* Completed tasks count
* Pending tasks count
* Completion rate
* First created task
* Last completed task

### Exporting

* Export all tasks to a text report (`relatorio_tarefas.txt`)

### Persistence

* JSON-based storage
* Automatic loading and saving
* Protection against corrupted JSON files
* Backward compatibility for tasks created before the priority feature

## Technologies

* Python 3
* JSON
* Object-Oriented Programming (OOP)
* Git
* GitHub

## Project Structure

```text
task_manager/
│
├── main.py
├── tarefas.py
├── tarefas.json
│
├── models/
│   └── tarefa.py
│
├── README.md
└── .gitignore
```

## How to Run

Clone the repository:

```bash
git clone <repository-url>
```

Navigate to the project directory:

```bash
cd task_manager
```

Run the application:

```bash
python main.py
```

## Learning Objectives

This project was built to practice:

* Classes and objects
* Constructors (`__init__`)
* Class methods
* Object serialization
* JSON persistence
* File handling
* Error handling
* Modular architecture
* Refactoring
* Sorting algorithms
* Data filtering
* Searching algorithms
* Git workflow
* GitHub workflow

## Current Version

### v1.0.0

Completed features:

* Task creation
* Task listing
* Task editing
* Task deletion
* Task completion
* Priority system
* Statistics dashboard
* Task filtering
* Task searching
* Task sorting
* Report exporting
* Refactoring of duplicated code
* Input validation improvements

## Future Improvements

* Task categories
* Task deadlines
* Notifications
* Recurring tasks
* Specialized task types using inheritance
* CSV export
* Database integration
* Graphical User Interface (GUI)
* Web version using Flask or Django
* REST API

## Author

Patrick Barboza Oliveira