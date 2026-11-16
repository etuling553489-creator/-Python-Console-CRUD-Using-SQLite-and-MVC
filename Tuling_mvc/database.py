import sqlite3
from pathlib import Path


DB_PATH = Path(__file__).resolve().parent / "students.db"


def get_connection():
    return sqlite3.connect(DB_PATH)


def initialize_database():
    connection = get_connection()

    try:
        connection.execute("""
            CREATE TABLE IF NOT EXISTS students (
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                course TEXT NOT NULL
            )
        """)

        connection.commit()

    finally:
        connection.close()
