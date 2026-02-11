# ---------------- MAIN DATA STRUCTURE ----------------

DATA_FILE = "students.txt"


# Function to load students from file
def load_students_from_file():
    data = {}
    try:
        file = open(DATA_FILE, "r")
        for line in file:
            line = line.strip()
            if line:  # skip empty lines
                roll, name, branch = line.split(",")
                data[roll] = {"name": name, "branch": branch}
        file.close()
    except FileNotFoundError:
        pass
    return data


# Load existing data at start
students = load_students_from_file()


# Function to save students to file
def save_students_to_file():
    file = open(DATA_FILE, "w")
    for roll, student in students.items():
        line = roll + "," + student["name"] + "," + student["branch"] + "\n"
        file.write(line)
    file.close()


# ----------- Core Functions -----------


# Function to add a new student
def add_student():
    name = input("Enter student name: ")
    roll = input("Enter roll number: ")
    branch = input("Enter branch: ")

    if roll in students:
        print("Student with this roll number already exists.")
        return

    students[roll] = {"name": name, "branch": branch}
    save_students_to_file()
    print("Student added successfully!")


# Function to view students
def view_students():
    if not students:
        print("No students found.")
        return

    print("\n--- Student List ---")
    for i, (roll, student) in enumerate(students.items(), start=1):
        print(f"{i}. Name: {student['name']}, Roll: {roll}, Branch: {student['branch']}")


# Function to update student
def update_student():
    roll = input("Enter roll number of student to update: ")

    if roll not in students:
        print("Student not found.")
        return

    print("Student found.")
    name = input("Enter new name: ")
    branch = input("Enter new branch: ")

    students[roll] = {"name": name, "branch": branch}
    save_students_to_file()
    print("Student updated successfully!")


# Function to delete student
def delete_student():
    roll = input("Enter roll number of student to delete: ")

    if roll not in students:
        print("Student not found.")
        return

    del students[roll]
    save_students_to_file()
    print("Student deleted successfully!")


# Main menu
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
