# Task 8 - Simple To-Do List

tasks = []


def add_task():
    task = input("Enter a task: ").strip()
    if task:
        tasks.append(task)
        print("Task added successfully.")
    else:
        print("Task cannot be empty.")


def view_tasks():
    if not tasks:
        print("Your to-do list is empty.")
    else:
        print("\nYour To-Do List:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")


def update_task():
    view_tasks()
    if tasks:
        try:
            number = int(input("Enter the task number to update: "))
            if 1 <= number <= len(tasks):
                new_task = input("Enter the updated task: ").strip()
                if new_task:
                    tasks[number - 1] = new_task
                    print("Task updated successfully.")
                else:
                    print("Task cannot be empty.")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Please enter a valid number.")


def remove_task():
    view_tasks()
    if tasks:
        try:
            number = int(input("Enter the task number to remove: "))
            if 1 <= number <= len(tasks):
                removed = tasks.pop(number - 1)
                print(f'Removed task: "{removed}"')
            else:
                print("Invalid task number.")
        except ValueError:
            print("Please enter a valid number.")


def main():
    while True:
        print("\n===== TO-DO LIST =====")
        print("1. Add task")
        print("2. View tasks")
        print("3. Update task")
        print("4. Remove task")
        print("5. Exit")

        choice = input("Choose an option (1-5): ").strip()

        if choice == "1":
            add_task()
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            update_task()
        elif choice == "4":
            remove_task()
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please select a number from 1 to 5.")


if __name__ == "__main__":
    main()
