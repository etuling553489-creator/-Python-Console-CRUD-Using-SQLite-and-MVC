from database import get_connection


def create_student(name, course):
    connection = get_connection()

    try:
        cursor = connection.execute(
            "INSERT INTO students (name, course) VALUES (?, ?)",
            (name, course)
        )

        connection.commit()

        return cursor.lastrowid

    finally:
        connection.close()


def get_all_students():
    connection = get_connection()

    try:
        cursor = connection.execute(
            "SELECT id, name, course FROM students ORDER BY id"
        )

        return cursor.fetchall()

    finally:
        connection.close()


def get_student(student_id):
    connection = get_connection()

    try:
        cursor = connection.execute(
            "SELECT id, name, course FROM students WHERE id = ?",
            (student_id,)
        )

        return cursor.fetchone()

    finally:
        connection.close()


def update_student(student_id, name, course):
    connection = get_connection()

    try:
        cursor = connection.execute(
            "UPDATE students SET name = ?, course = ? WHERE id = ?",
            (name, course, student_id)
        )

        connection.commit()

        return cursor.rowcount > 0

    finally:
        connection.close()


def delete_student(student_id):
    connection = get_connection()

    try:
        cursor = connection.execute(
            "DELETE FROM students WHERE id = ?",
            (student_id,)
        )

        connection.commit()

        return cursor.rowcount > 0

    finally:
        connection.close()
