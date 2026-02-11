# ---------------- FILE NAME ----------------
DATA_FILE = "tasks.txt"


# ---------------- LOAD TASKS ----------------
def load_tasks():
    data = []
    try:
        file = open(DATA_FILE, "r")
        for line in file:
            line = line.strip()
            if line:
                title, completed = line.split(",")
                data.append({
                    "title": title,
                    "completed": completed == "True"
                })
        file.close()
    except FileNotFoundError:
        pass
    return data


# Load tasks when program starts
tasks = load_tasks()


# ---------------- SAVE TASKS ----------------
def save_tasks():
    file = open(DATA_FILE, "w")
    for task in tasks:
        line = task["title"] + "," + str(task["completed"]) + "\n"
        file.write(line)
    file.close()


# ---------------- CORE FUNCTIONS ----------------

# Add new task
def add_task():
    title = input("Enter task: ")

    if title.strip() == "":
        print("Task cannot be empty.")
        return

    tasks.append({
        "title": title,
        "completed": False
    })

    save_tasks()
    print("Task added successfully.")


# View tasks
def view_tasks():
    if not tasks:
        print("No tasks available.")
        return

    print("\n--- Task List ---")
    for i, task in enumerate(tasks, start=1):
        status = "✓" if task["completed"] else "✗"
        print(f"{i}. {task['title']} [{status}]")


# Mark task as completed
def mark_complete():
    view_tasks()

    if not tasks:
        return

    try:
        index = int(input("Enter task number to mark complete: ")) - 1

        if 0 <= index < len(tasks):
            tasks[index]["completed"] = True
            save_tasks()
            print("Task marked as complete.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")


# Delete task
def delete_task():
    view_tasks()

    if not tasks:
        return

    try:
        index = int(input("Enter task number to delete: ")) - 1

        if 0 <= index < len(tasks):
            tasks.pop(index)
            save_tasks()
            print("Task deleted successfully.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")


# ---------------- MENU ----------------
def menu():
    while True:
        print("\n--- To-Do List ---")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Complete")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            add_task()
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            mark_complete()
        elif choice == "4":
            delete_task()
        elif choice == "5":
            print("Exiting program...")
            break
        else:
            print("Invalid choice.")


# ---------------- START PROGRAM ----------------
menu()
