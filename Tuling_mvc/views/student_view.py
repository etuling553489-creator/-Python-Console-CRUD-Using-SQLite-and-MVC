def show_message(message):
    print(message)


def show_menu():
    print("\n===== STUDENT RECORD MANAGEMENT =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Update Student")
    print("4. Delete Student")
    print("5. Exit")

    return input("Choose an option: ").strip()


def read_required_text(prompt):
    while True:
        value = input(prompt).strip()

        if value:
            return value

        print("This field cannot be blank.")


def read_student_details():
    name = read_required_text("Enter student name: ")
    course = read_required_text("Enter course: ")

    return name, course


def read_student_id():
    while True:
        try:
            student_id = int(input("Enter student ID: "))

            if student_id > 0:
                return student_id

            print("ID must be greater than zero.")

        except ValueError:
            print("Please enter a valid whole number.")


def show_students(students):
    if not students:
        print("No students found.")
        return

    print("\nSTUDENT LIST")
    print(f"{'ID':<6} {'Name':<25} Course")
    print("-" * 50)

    for student_id, name, course in students:
        print(f"{student_id:<6} {name:<25} {course}")


def confirm_delete(name):
    answer = input(
        f"Delete {name}? Type YES to confirm: "
    ).strip()

    return answer == "YES"
