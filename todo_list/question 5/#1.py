
"""
Console-based To-Do List Application

This module implements a simple in-memory to-do list manager that allows the user to add, remove, search, finish,
list, and clear tasks. It follows best practices for clean, modular, and maintainable Python code and adheres to the 
ISO/IEC 25010 standard by emphasizing proper architecture, efficiency, and error handling.

Author: Senior Software Developer
Date: 2023-10
"""

class TaskManager:
    """
    A class to manage tasks in an in-memory to-do list.

    Each task is stored as a dictionary with the following keys:
      - id (int): Unique identifier of the task.
      - task_name (str): The name of the task.
      - task_description (str): A description of the task.
      - is_finished (bool): Status flag indicating if the task is completed.
    """
    def __init__(self):
        """
        Initialize the TaskManager with an empty task storage and a counter for generating unique IDs.
        """
        self._tasks = {}         # Dictionary for storing tasks by their unique id.
        self._next_id = 1        # Next unique id for new tasks.

    def add(self, task_name: str, task_description: str) -> int:
        """
        Add a new task to the to-do list.

        Args:
            task_name (str): The name of the task. Must not be empty.
            task_description (str): The description of the task. Must not be empty.

        Returns:
            int: The unique ID of the task that was added.

        Raises:
            ValueError: If task_name or task_description is empty.
        """
        if not isinstance(task_name, str) or not task_name.strip():
            raise ValueError("Task name cannot be empty.")
        if not isinstance(task_description, str) or not task_description.strip():
            raise ValueError("Task description cannot be empty.")

        task_id = self._next_id
        self._next_id += 1

        self._tasks[task_id] = {
            "id": task_id,
            "task_name": task_name,
            "task_description": task_description,
            "is_finished": False
        }
        return task_id

    def remove(self, task_id: int) -> bool:
        """
        Remove a task from the to-do list by its unique ID.

        Args:
            task_id (int): The unique ID of the task to remove. Must be a positive integer.

        Returns:
            bool: True if the task was removed successfully, False otherwise.
        """
        if not isinstance(task_id, int) or task_id <= 0:
            return False
        if task_id not in self._tasks:
            return False

        del self._tasks[task_id]
        return True

    def search(self, task_term: str) -> list:
        """
        Search tasks by a term that may appear in the task name or task description.

        Args:
            task_term (str): The term to search for. Must be a non-empty string.

        Returns:
            list[dict]: A list of task dictionaries that match the search term.
        """
        if not isinstance(task_term, str) or not task_term.strip():
            return []

        term = task_term.lower()
        results = [
            task for task in self._tasks.values()
            if term in task["task_name"].lower() or term in task["task_description"].lower()
        ]
        return results

    def finish(self, task_id: int) -> bool:
        """
        Mark a task as finished by its unique ID.

        Args:
            task_id (int): The unique ID of the task to mark finished.

        Returns:
            bool: True if the task status was updated successfully, False otherwise.
        """
        if not isinstance(task_id, int) or task_id <= 0:
            return False
        if task_id not in self._tasks:
            return False

        self._tasks[task_id]["is_finished"] = True
        return True

    def get_all(self) -> list:
        """
        Retrieve all tasks in the to-do list.

        Returns:
            list[dict]: A list of all task dictionaries.
        """
        return list(self._tasks.values())

    def clear_all(self) -> bool:
        """
        Delete all tasks from the to-do list.

        Returns:
            bool: True after clearing all tasks.
        """
        self._tasks.clear()
        return True


def main():
    """
    Main function to run the console-based to-do list application.
    It provides a simple command-line interface to interact with the TaskManager.
    """
    manager = TaskManager()
    command_menu = (
        "\n--------- To-Do List Application ---------\n"
        "Available commands:\n"
        "  add       - Add a new task\n"
        "  remove    - Remove an existing task by ID\n"
        "  search    - Search for tasks by a search term\n"
        "  finish    - Mark a task as finished\n"
        "  get_all   - List all tasks\n"
        "  clear_all - Clear all tasks\n"
        "  exit      - Exit the application\n"
    )

    while True:
        print(command_menu)
        command = input("Enter command: ").strip().lower()

        if command == "exit":
            print("Exiting application. Goodbye!")
            break

        elif command == "add":
            task_name = input("Enter task name: ").strip()
            task_description = input("Enter task description: ").strip()

            try:
                task_id = manager.add(task_name, task_description)
                print(f"Task added successfully with ID: {task_id}")
            except ValueError as e:
                print(f"Error: {e}")

        elif command == "remove":
            id_input = input("Enter task ID to remove: ").strip()
            try:
                task_id = int(id_input)
            except ValueError:
                print("Invalid input: Task ID must be a number.")
                continue

            if manager.remove(task_id):
                print("Task removed successfully.")
            else:
                print("Error: Task ID not found or invalid.")

        elif command == "search":
            search_term = input("Enter search term: ").strip()
            results = manager.search(search_term)
            if results:
                print("Matching tasks:")
                for task in results:
                    print(
                        f"ID: {task['id']}, Name: {task['task_name']}, "
                        f"Description: {task['task_description']}, Finished: {task['is_finished']}"
                    )
            else:
                print("No matching tasks found.")

        elif command == "finish":
            id_input = input("Enter task ID to mark as finished: ").strip()
            try:
                task_id = int(id_input)
            except ValueError:
                print("Invalid input: Task ID must be a number.")
                continue

            if manager.finish(task_id):
                print("Task marked as finished.")
            else:
                print("Error: Task ID not found or invalid.")

        elif command == "get_all":
            tasks = manager.get_all()
            if tasks:
                print("Listing all tasks:")
                for task in tasks:
                    print(
                        f"ID: {task['id']}, Name: {task['task_name']}, "
                        f"Description: {task['task_description']}, Finished: {task['is_finished']}"
                    )
            else:
                print("No tasks available.")

        elif command == "clear_all":
            confirmation = input("Are you sure you want to clear all tasks? (y/n): ").strip().lower()
            if confirmation == "y":
                if manager.clear_all():
                    print("All tasks have been cleared.")
                else:
                    print("Error: Could not clear tasks.")
            else:
                print("Clear all operation cancelled.")

        else:
            print("Unknown command. Please try again.")


if __name__ == "__main__":
    main()
