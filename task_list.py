import os

# Function to display the menu options
def display_menu():
    print("\n--- Task List Manager ---")
    print("1. Add a new task")
    print("2. Remove a task")
    print("3. View all tasks")
    print("4. Exit")
    choice = input("Choose an option (1-4): ")
    return choice

# Function to add a new task
def add_task(file_name):
    try:
        task = input("Enter the new task: ")
        with open(file_name, 'a') as file:
            file.write(task + "\n")
        print("Task added successfully.")
    except Exception as e:
        print(f"An error occurred while adding the task: {e}")

# Function to remove a task
def remove_task(file_name):
    try:
        # Read all tasks
        with open(file_name, 'r') as file:
            tasks = file.readlines()

        if not tasks:
            print("There are no tasks to remove.")
            return

        # Display tasks for removal
        print("\n--- Current Tasks ---")
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task.strip()}")

        # Prompt user for task to remove
        task_number = int(input("Enter the task number to remove: "))
        if task_number < 1 or task_number > len(tasks):
            print("Invalid task number.")
            return

        # Remove the selected task
        tasks.pop(task_number - 1)

        # Rewrite the tasks to the file
        with open(file_name, 'w') as file:
            file.writelines(tasks)
        print("Task removed successfully.")
    except FileNotFoundError:
        print(f"Error: The task file '{file_name}' does not exist.")
    except ValueError:
        print("Invalid input. Please enter a valid number.")
    except Exception as e:
        print(f"An error occurred while removing the task: {e}")

# Function to view all tasks
def view_tasks(file_name):
    try:
        if not os.path.exists(file_name):
            print("No tasks available. The task file is missing.")
            return

        with open(file_name, 'r') as file:
            tasks = file.readlines()

        if not tasks:
            print("No tasks found.")
        else:
            print("\n--- Current Tasks ---")
            for index, task in enumerate(tasks, start=1):
                print(f"{index}. {task.strip()}")
    except Exception as e:
        print(f"An error occurred while viewing tasks: {e}")

# Main function to run the task list manager
def main():
    file_name = "tasks.txt"  # File where tasks are stored

    # Check if the file exists, if not, create it
    if not os.path.exists(file_name):
        with open(file_name, 'w'):  # Create an empty file
            pass

    while True:
        choice = display_menu()

        if choice == '1':
            add_task(file_name)
        elif choice == '2':
            remove_task(file_name)
        elif choice == '3':
            view_tasks(file_name)
        elif choice == '4':
            print("\nThank you for using the Task List Manager. Goodbye!")
            break
        else:
            print("\nInvalid option. Please try again.")

# Run the application
if __name__ == "__main__":
    main()
