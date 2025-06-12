# ==============================================================================
# Task 1: TO-DO LIST Application (Command-line based)
# This program allows users to manage their tasks: add, view, mark as complete,
# and delete. Tasks are stored in memory for the duration of the program.
# ==============================================================================
import os

def clear_screen():
    """Clears the console screen for better readability."""
    os.system('cls' if os.name == 'nt' else 'clear')

def display_menu():
    """Displays the main menu options to the user."""
    print("\n--- TO-DO LIST ---")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task as Complete")
    print("4. Delete Task")
    print("5. Exit")
    print("------------------")

def add_task(tasks):
    """
    Adds a new task to the list.
    Each task is stored as a dictionary with a 'task' description and a 'completed' status.
    Args:
        tasks (list): The list of task dictionaries.
    """
    task_description = input("Enter the task description: ").strip()
    if task_description:
        tasks.append({"task": task_description, "completed": False})
        print(f"Task '{task_description}' added successfully!")
    else:
        print("Task description cannot be empty. Task not added.")

def view_tasks(tasks):
    """
    Displays all tasks currently in the list, showing their number and completion status.
    Args:
        tasks (list): The list of task dictionaries.
    """
    if not tasks:
        print("\nYour to-do list is empty! Add some tasks.")
        return

    print("\n--- Your Tasks ---")
    for i, task in enumerate(tasks):
        # '✓' for completed tasks, ' ' (space) for incomplete tasks
        status = "✓" if task["completed"] else " "
        print(f"{i + 1}. [{status}] {task['task']}")
    print("------------------")

def mark_task_complete(tasks):
    """
    Marks a task as complete based on its sequential number in the displayed list.
    Args:
        tasks (list): The list of task dictionaries.
    """
    view_tasks(tasks) # Show tasks first so user knows which number to pick
    if not tasks: # If view_tasks indicated the list is empty, exit
        return

    try:
        task_num_input = input("Enter the number of the task to mark as complete: ")
        task_num = int(task_num_input)
        
        # Adjust for 0-based indexing (user input is 1-based)
        if 1 <= task_num <= len(tasks):
            if not tasks[task_num - 1]["completed"]:
                tasks[task_num - 1]["completed"] = True
                print(f"Task '{tasks[task_num - 1]['task']}' marked as complete!")
            else:
                print(f"Task '{tasks[task_num - 1]['task']}' is already completed.")
        else:
            print("Invalid task number. Please enter a number from the list.")
    except ValueError:
        print("Invalid input. Please enter a numerical task number.")

def delete_task(tasks):
    """
    Deletes a task from the list based on its sequential number.
    Args:
        tasks (list): The list of task dictionaries.
    """
    view_tasks(tasks) # Show tasks first so user knows which number to pick
    if not tasks: # If view_tasks indicated the list is empty, exit
        return

    try:
        task_num_input = input("Enter the number of the task to delete: ")
        task_num = int(task_num_input)

        # Adjust for 0-based indexing (user input is 1-based)
        if 1 <= task_num <= len(tasks):
            removed_task = tasks.pop(task_num - 1) # .pop() removes item at index and returns it
            print(f"Task '{removed_task['task']}' deleted successfully!")
        else:
            print("Invalid task number. Please enter a number from the list.")
    except ValueError:
        print("Invalid input. Please enter a numerical task number.")

def run_todo_list():
    """
    Main function to run the To-Do List application.
    It manages the application loop, displaying the menu and handling user choices.
    """
    tasks = [] # Initialize an empty list to store tasks
    while True:
        clear_screen() # Clear the screen before displaying the menu for a cleaner look
        display_menu()
        choice = input("Enter your choice (1-5): ").strip()

        if choice == '1':
            add_task(tasks)
        elif choice == '2':
            view_tasks(tasks)
        elif choice == '3':
            mark_task_complete(tasks)
        elif choice == '4':
            delete_task(tasks)
        elif choice == '5':
            print("Exiting To-Do List. Goodbye!")
            break # Exit the while loop to terminate the program
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")
        
        # Pause before clearing screen for next menu display, allowing user to read output
        input("\nPress Enter to continue...") 

# This line calls the main function to start the To-Do List application.
# When you run this Python script, the program will begin execution here.
if __name__ == "__main__":
    run_todo_list()
