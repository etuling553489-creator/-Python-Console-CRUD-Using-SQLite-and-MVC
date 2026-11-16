import sqlite3

from database import initialize_database
from controllers.student_controller import run
from views.student_view import show_message


def main():
    try:
        initialize_database()

    except sqlite3.Error as error:
        show_message(
            f"Cannot initialize database: {error}"
        )
        return

    run()


if __name__ == "__main__":
    main()
