"""
Console-based Todo List Application
Meets the requirements of ISO/IEC 25010.

This application provides a todo list interface that allows you to:
    - Add a new task
    - Remove an existing task
    - Search tasks by name or description
    - Mark a task as completed
    - Retrieve all tasks
    - Clear all tasks

The tasks are stored in-memory in an efficient dictionary data structure,
and the code is organized for clarity, maintainability, and testability.
"""

class TaskManager:
    """
    Manages tasks for a todo list application.

    Attributes:
        tasks (dict): A dictionary mapping task IDs to task details.
        next_id (int): The next available unique ID for new tasks.
    """
    
    def __init__(self) -> None:
        """Initializes TaskManager with an empty task store."""
        self.tasks = {}
        self.next_id = 1

    def add(self, task_name: str, task_description: str) -> int:
        """
        Adds a new task to the todo list.

        Args:
            task_name (str): The name of the task.
            task_description (str): The description of the task.

        Returns:
            int: The unique ID assigned to the new task.

        Raises:
            ValueError: If the task name or description is empty.
        """
        if not isinstance(task_name, str) or not task_name.strip():
            raise ValueError("Task name cannot be empty.")
        if not isinstance(task_description, str) or not task_description.strip():
            raise ValueError("Task description cannot be empty.")

        task_id = self.next_id
        self.tasks[task_id] = {
            "id": task_id,
            "task_name": task_name.strip(),
            "task_description": task_description.strip(),
            "is_finished": False
        }
        self.next_id += 1
        return task_id

    def remove(self, task_id: int) -> bool:
        """
        Removes a task identified by task_id.

        Args:
            task_id (int): The unique ID of the task to remove.

        Returns:
            bool: True if the task was removed successfully, False otherwise.
        """
        if not isinstance(task_id, int) or task_id <= 0:
            return False
        if task_id in self.tasks:
            del self.tasks[task_id]
            return True
        return False

    def search(self, task_term: str) -> list:
        """
        Searches for tasks with a matching term in the task name or description.

        Args:
            task_term (str): The term to search for.

        Returns:
            list[dict]: A list of tasks that match the search term.
                        Each task is represented as a dictionary with keys:
                        (id, task_name, task_description, is_finished)
        """
        if not isinstance(task_term, str) or not task_term.strip():
            # Return empty list if there is no valid search term.
            return []
        term = task_term.strip().lower()
        return [
            task for task in self.tasks.values()
            if term in task["task_name"].lower() or term in task["task_description"].lower()
        ]

    def finish(self, task_id: int) -> bool:
        """
        Marks a task as completed.

        Args:
            task_id (int): The unique ID of the task to mark as finished.

        Returns:
            bool: True if the task was found and marked finished, False otherwise.
        """
        if not isinstance(task_id, int) or task_id <= 0:
            return False
        if task_id in self.tasks:
            self.tasks[task_id]["is_finished"] = True
            return True
        return False

    def get_all(self) -> list:
        """
        Retrieves all tasks in the todo list.

        Returns:
            list[dict]: A list of all tasks, where each task is represented as a dictionary.
        """
        return list(self.tasks.values())

    def clear_all(self) -> bool:
        """
        Clears all tasks from the todo list.

        Returns:
            bool: True after all tasks have been cleared.
        """
        self.tasks.clear()
        return True

def print_tasks(tasks: list) -> None:
    """
    Prints a list of tasks in a user-friendly format.

    Args:
        tasks (list): A list of task dictionaries to display.
    """
    if not tasks:
        print("No tasks to display.")
        return

    print("\nCurrent Tasks:")
    print("-" * 40)
    for task in tasks:
        status = "Finished" if task["is_finished"] else "Pending"
        print(f"ID: {task['id']}")
        print(f"Task: {task['task_name']}")
        print(f"Description: {task['task_description']}")
        print(f"Status: {status}")
        print("-" * 40)

def display_menu() -> None:
    """
    Displays the menu options for the Todo List application.
    """
    menu = """
Todo List Application Menu:
1. Add Task
2. Remove Task
3. Search Tasks
4. Finish Task
5. Get All Tasks
6. Clear All Tasks
7. Exit
"""
    print(menu)

def main():
    """
    The main function to run the console-based Todo List application.
    """
    manager = TaskManager()

    while True:
        display_menu()
        choice = input("Please select an option (1-7): ").strip()

        if choice == "1":
            # Add Task
            try:
                name = input("Enter task name: ").strip()
                description = input("Enter task description: ").strip()
                task_id = manager.add(name, description)
                print(f"Task added successfully with ID: {task_id}\n")
            except ValueError as ve:
                print(f"Error: {ve}\n")

        elif choice == "2":
            # Remove Task
            try:
                task_id_input = input("Enter task ID to remove: ").strip()
                task_id = int(task_id_input)
                if manager.remove(task_id):
                    print("Task removed successfully.\n")
                else:
                    print("Failed to remove task. Task may not exist.\n")
            except ValueError:
                print("Invalid input. Please enter a valid numeric task ID.\n")

        elif choice == "3":
            # Search Tasks
            term = input("Enter search term: ").strip()
            results = manager.search(term)
            if results:
                print_tasks(results)
            else:
                print("No matching tasks found.\n")

        elif choice == "4":
            # Finish Task
            try:
                task_id_input = input("Enter task ID to mark as finished: ").strip()
                task_id = int(task_id_input)
                if manager.finish(task_id):
                    print("Task marked as finished.\n")
                else:
                    print("Task not found or error occurred.\n")
            except ValueError:
                print("Invalid input. Please enter a valid numeric task ID.\n")

        elif choice == "5":
            # Get All Tasks
            tasks = manager.get_all()
            print_tasks(tasks)

        elif choice == "6":
            # Clear All Tasks
            confirm = input("Are you sure you want to clear all tasks? (y/n): ").strip().lower()
            if confirm == "y":
                manager.clear_all()
                print("All tasks have been cleared.\n")
            else:
                print("Clear all tasks canceled.\n")

        elif choice == "7":
            print("Exiting the Todo List application. Goodbye!")
            break

        else:
            print("Invalid option selected. Please choose a valid option from 1 to 7.\n")

if __name__ == "__main__":
    main()
