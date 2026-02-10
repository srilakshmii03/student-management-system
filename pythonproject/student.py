# ================================
# STUDENT MANAGEMENT SYSTEM
# ================================

# ---------- Helper Functions ----------
def get_non_empty_input(prompt):
    while True:
        value = input(prompt).strip()
        if value:
            return value
        else:
            print("Input cannot be empty. Please try again.")


# ---------- Main Data Structure ----------
# Dictionary: roll_number -> student details
students = {}


# ---------- Core Functions ----------

# Add a new student
def add_student():
    name = get_non_empty_input("Enter student name: ")
    roll = get_non_empty_input("Enter roll number: ")
    branch = get_non_empty_input("Enter branch: ")

    if roll in students:
        print("Student with this roll number already exists.")
        return

    students[roll] = {
        "name": name,
        "roll": roll,
        "branch": branch
    }

    print("Student added successfully!")


# View all students
def view_students():
    if not students:
        print("No students found.")
        return

    print("\n--- Student List ---")
    for i, student in enumerate(students.values(), start=1):
        print(
            f"{i}. Name: {student['name']}, "
            f"Roll: {student['roll']}, "
            f"Branch: {student['branch']}"
        )


# Update student details
def update_student():
    roll = get_non_empty_input("Enter roll number of student to update: ")

    if roll not in students:
        print("Student not found.")
        return

    print("Student found.")
    students[roll]["name"] = get_non_empty_input("Enter new name: ")
    students[roll]["branch"] = get_non_empty_input("Enter new branch: ")

    print("Student updated successfully!")


# Delete a student
def delete_student():
    roll = get_non_empty_input("Enter roll number of student to delete: ")

    if roll in students:
        del students[roll]
        print("Student deleted successfully!")
    else:
        print("Student not found.")


# ---------- Menu Function ----------
def menu():
    while True:
        print("\n--- Student Management System ---")
        print("1. Add Student")
        print("2. View Students")
        print("3. Update Student")
        print("4. Delete Student")
        print("5. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            update_student()
        elif choice == "4":
            delete_student()
        elif choice == "5":
            print("Exiting program...")
            break
        else:
            print("Invalid choice. Please try again.")


# ---------- Program Start ----------
menu()
