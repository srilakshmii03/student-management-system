students = []
# Function to add a new student
def add_student():
    name = input("Enter student name: ")
    roll = input("Enter roll number: ")
    branch = input("Enter branch: ")

    student = {
        "name": name,
        "roll": roll,
        "branch": branch
    }

    students.append(student)
    print("Student added successfully!")
# Function to view the existing students
def view_students():
    if not students:
        print("No students found.")
    else:
        print("\n--- Student List ---")
        for i, student in enumerate(students, start=1):
            print(f"{i}. Name: {student['name']}, Roll: {student['roll']}, Branch: {student['branch']}")
# Function to update existing students data
def update_student():
    roll = input("Enter roll number of student to update: ")

    for student in students:
        if student["roll"] == roll:
            print("Student found.")
            student["name"] = input("Enter new name: ")
            student["branch"] = input("Enter new branch: ")
            print("Student updated successfully!")
            return
    print("Student not found.")
# Function to delete students
def delete_student():
    roll = input("Enter roll number of student to delete: ")

    for student in students:
        if student["roll"] == roll:
            students.remove(student)
            print("Student deleted successfully!")
            return

    print("Student not found.")
# Main function
def menu():
    while True:
        print("\n--- Student Management System ---")
        print("1. Add Student")
        print("2. View Students")
        print("3. Update Student")
        print("4. Delete Student")
        print("5. Exit")

        choice = input("Enter your choice: ")

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

menu()


