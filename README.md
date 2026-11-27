# Coding Session Tracker

A command-line interface (CLI) that logs and tracks daily work hours using SQLite for persistent storage.

**Tech Stack:** Python, SQLite, pytest, Git

## Commands

- **`add <topic> <hours>`** — Validates that hours are positive, records the session date, and inserts the new session into the database.
- **`list`** — Checks for existing records and displays each session's topic and hours, along with weekly and total hours.
- **`delete <id>`** — Validates the session ID and deletes the corresponding record from the database.

## Usage

```bash
python cli.py add "SQLite" 1.5
python cli.py list
python cli.py delete 1