# flyrank-backend-a2-fastapi-sqlite
A CRUD Task Manager REST API built with FastAPI and SQLite for the FlyRank Backend Internship Week 3 Assignment. Supports persistent task storage with complete Create, Read, Update, and Delete operations.


# FlyRank Backend Internship - Week 3 Assignment A2

## Connecting CRUD API to SQLite Database

This project is a REST API built using **FastAPI** and **SQLite**. It allows users to create, read, update, and delete tasks while storing the data permanently in a SQLite database.

Unlike Assignment 1, where tasks were stored in memory and disappeared after restarting the server, this version stores all tasks in `tasks.db`, so the data persists between server restarts.

---

## Features

- Create new tasks
- View all tasks
- View a single task by ID
- Update existing tasks
- Delete tasks
- SQLite database persistence
- Automatic database creation
- Automatic table creation
- Automatic seeding of sample tasks

---

## Technologies Used

- Python 3
- FastAPI
- SQLite
- Uvicorn
- Pydantic
- DB Browser for SQLite

---

## Project Structure

```
project/
│
├── main.py
├── database.py
├── tasks.db
├── README.md
```

---

## API Endpoints

| Method | Endpoint | Description |
|---------|----------|-------------|
| GET | / | Home |
| GET | /tasks | Get all tasks |
| GET | /tasks/{id} | Get task by ID |
| POST | /tasks | Create a task |
| PUT | /tasks/{id} | Update a task |
| DELETE | /tasks/{id} | Delete a task |

---

## Database

The project uses **SQLite** because:

- Lightweight
- No database server required
- Stores data in a single file (`tasks.db`)
- Automatically creates the database
- Data remains after restarting the server

---

## Database Schema

Table Name:

```
tasks
```

Columns:

| Column | Type |
|---------|------|
| id | INTEGER PRIMARY KEY AUTOINCREMENT |
| title | TEXT |
| done | BOOLEAN |

---

## SQL Query Example

```sql
SELECT * FROM tasks;
```

This query returns every task stored in the database.

---

## Running the Project

### Install dependencies

```bash
pip install fastapi uvicorn
```

### Start the server

```bash
uvicorn main:app --reload
```

Open Swagger UI:

```
http://127.0.0.1:8000/docs
```

---

## Database Screenshot

Insert your DB Browser screenshot here.

Example:

```
docs/database.png
```

---

## Assignment Requirements Completed

- SQLite database created automatically
- Tasks table created automatically
- Seed data inserted only once
- GET all tasks
- GET task by ID
- POST task
- PUT task
- DELETE task
- Persistent database storage
- SQL queries executed using DB Browser

---

## Author

Created by **Warda Shahid** for the **FlyRank Backend Internship Week 3 Assignment A2**.
