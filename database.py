import sqlite3


def get_connection():
    return sqlite3.connect("tasks.db")


# -------------------------
# CREATE DATABASE + TABLE
# -------------------------

connection = get_connection()
cursor = connection.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS tasks (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    done BOOLEAN NOT NULL
)
""")

connection.commit()


# -------------------------
# INSERT DEFAULT TASKS ONLY ONCE
# -------------------------

cursor.execute("SELECT COUNT(*) FROM tasks")
count = cursor.fetchone()[0]

if count == 0:
    cursor.executemany(
        "INSERT INTO tasks (title, done) VALUES (?, ?)",
        [
            ("Buy milk", 0),
            ("Study Python", 0),
            ("Complete Assignment", 1)
        ]
    )

    connection.commit()


connection.close()


# -------------------------
# GET ALL TASKS
# -------------------------

def get_all_tasks():

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("SELECT id, title, done FROM tasks")

    rows = cursor.fetchall()

    tasks = []

    for row in rows:
        tasks.append({
            "id": row[0],
            "title": row[1],
            "done": bool(row[2])
        })

    connection.close()

    return tasks


def create_task(title):

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute(
        "INSERT INTO tasks (title, done) VALUES (?, ?)",
        (title, 0)
    )

    connection.commit()

    task_id = cursor.lastrowid

    connection.close()

    return {
        "id": task_id,
        "title": title,
        "done": False
    }


def get_task_by_id(task_id):

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute(
        "SELECT id, title, done FROM tasks WHERE id = ?",
        (task_id,)
    )

    row = cursor.fetchone()

    connection.close()

    if row:
        return {
            "id": row[0],
            "title": row[1],
            "done": bool(row[2])
        }

    return None


def update_task(task_id, title, done):

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute(
        "UPDATE tasks SET title = ?, done = ? WHERE id = ?",
        (title, done, task_id)
    )

    connection.commit()

    if cursor.rowcount == 0:
        connection.close()
        return None

    connection.close()

    return {
        "id": task_id,
        "title": title,
        "done": done
    }
def delete_task(task_id):

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute(
        "DELETE FROM tasks WHERE id = ?",
        (task_id,)
    )

    connection.commit()

    if cursor.rowcount == 0:
        connection.close()
        return False

    connection.close()

    return True