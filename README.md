# Personal To-Do List Application

A simple command-line To-Do List app using Python and JSON file storage.

## Features
- Add, view, edit, complete, and delete tasks
- Categorize tasks (Work, Personal, Urgent, etc.)
- Persist data in `tasks.json`
- Filter and search by category or title
- Clean prompts and validation

## Quick Start
```bash
python todo.py
```
Tasks are stored in `tasks.json` in the same folder.

## File Structure
```
/todo_app
  ├── todo.py
  ├── tasks.json
  └── README.md
```

## Notes
- JSON-based storage avoids the complexity of a database.
- Cross-platform and runs locally with Python 3.8+.
