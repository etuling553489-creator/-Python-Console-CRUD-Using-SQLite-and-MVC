import sqlite3

from models import student_model as model
from views import student_view as view


def add_student():
    name, course = view.read_student_details()

    student_id = model.create_student(name, course)

    view.show_message(
        f"Student added successfully! ID: {student_id}"
    )


def list_students():
    students = model.get_all_students()

    view.show_students(students)


def edit_student():
    student_id = view.read_student_id()

    student = model.get_student(student_id)

    if student is None:
        view.show_message("Student not found.")
        return

    view.show_message("Current student record:")
    view.show_students([student])

    view.show_message("Enter the replacement details:")
    name, course = view.read_student_details()

    updated = model.update_student(
        student_id, name, course
    )

    if updated:
        view.show_message("Student updated successfully!")
    else:
        view.show_message("Student not found.")


def remove_student():
    student_id = view.read_student_id()

    student = model.get_student(student_id)

    if student is None:
        view.show_message("Student not found.")
        return

    if not view.confirm_delete(student[1]):
        view.show_message("Deletion cancelled.")
        return

    deleted = model.delete_student(student_id)

    if deleted:
        view.show_message("Student deleted successfully!")
    else:
        view.show_message("Student not found.")


def run():
    while True:
        choice = view.show_menu()

        try:
            if choice == "1":
                add_student()

            elif choice == "2":
                list_students()

            elif choice == "3":
                edit_student()

            elif choice == "4":
                remove_student()

            elif choice == "5":
                view.show_message("Goodbye!")
                break

            else:
                view.show_message(
                    "Invalid option. Please choose 1 to 5."
                )

        except sqlite3.Error as error:
            view.show_message(
                f"Database operation failed: {error}"
            )
