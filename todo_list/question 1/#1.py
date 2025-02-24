"""
Console-based Todo List Application
This application implements a todo list manager conforming to requirements in ISO/IEC 25010.
It provides key functionalities such as add, remove, search, finish, get_all, and clear_all.

Usage:
    Run the script and follow the console instructions to manage your todo tasks.

Each task is stored using the following format:
    {
        "id": int,
        "task_name": str,
        "task_description": str,
        "is_finished": bool
    }
"""

from typing import List, Dict


class TaskManager:
    """
    Manages todo list tasks in memory.
    Provides methods to add, remove, search, finish, retrieve, and clear tasks.
    """

    def __init__(self) -> None:
        """
        Initialize the TaskManager with an empty task storage and unique id counter.
        """
        self.tasks: Dict[int, Dict] = {}
        self.next_id: int = 1

    def add(self, task_name: str, task_description: str) -> int:
        """
        Adds a new task to the todo list.

        Args:
            task_name (str): The name of the task. Must be non-empty.
            task_description (str): A description of the task. Must be non-empty.

        Returns:
            int: A unique identifier for the new task.

        Raises:
            ValueError: If task_name or task_description is empty.
        """
        # Validate inputs to prevent adding invalid tasks.
        if not isinstance(task_name, str) or not task_name.strip():
            raise ValueError("Task name cannot be empty.")
        if not isinstance(task_description, str) or not task_description.strip():
            raise ValueError("Task description cannot be empty.")

        # Create a new task dictionary.
        task_id = self.next_id
        self.tasks[task_id] = {
            "id": task_id,
            "task_name": task_name.strip(),
            "task_description": task_description.strip(),
            "is_finished": False,
        }
        self.next_id += 1  # Increment counter for next task unique ID.
        return task_id

    def remove(self, task_id: int) -> bool:
        """
        Removes a task from the todo list by its unique ID.

        Args:
            task_id (int): The ID of the task to remove.

        Returns:
            bool: True if removal was successful; False if task_id is invalid or not found.
        """
        if not isinstance(task_id, int) or task_id <= 0:
            return False
        if task_id in self.tasks:
            del self.tasks[task_id]
            return True
        return False

    def search(self, task_term: str) -> List[Dict]:
        """
        Searches for tasks that contain the search term in their name or description.

        Args:
            task_term (str): The term to search for.

        Returns:
            List[Dict]: A list of tasks matching the search criteria.
        """
        if not isinstance(task_term, str) or not task_term.strip():
            # If empty search term, return empty list
            return []

        term = task_term.strip().lower()
        results = []
        for task in self.tasks.values():
            if term in task["task_name"].lower() or term in task["task_description"].lower():
                results.append(task)
        return results

    def finish(self, task_id: int) -> bool:
        """
        Marks a task as finished.

        Args:
            task_id (int): The ID of the task to mark as finished.

        Returns:
            bool: True if the task was found and marked as finished; False otherwise.
        """
        if not isinstance(task_id, int) or task_id <= 0:
            return False

        task = self.tasks.get(task_id)
        if task:
            task["is_finished"] = True
            return True
        return False

    def get_all(self) -> List[Dict]:
        """
        Retrieves all tasks from the todo list.

        Returns:
            List[Dict]: A list containing all tasks.
        """
        return list(self.tasks.values())

    def clear_all(self) -> bool:
        """
        Clears all tasks from the todo list.

        Returns:
            bool: True if tasks were successfully cleared.
        """
        self.tasks.clear()
        # Optional: Reset the task ID counter if desired.
        self.next_id = 1
        return True


def main() -> None:
    """
    Entry point for the console-based todo list app.
    Handles user interactions and calls TaskManager methods.
    """
    manager = TaskManager()
    print("Welcome to the Todo List App!")
    print("Available commands: add, remove, search, finish, get_all, clear_all, exit")

    while True:
        command = input("\nEnter a command: ").strip().lower()

        if command == "add":
            task_name = input("Task name: ").strip()
            task_description = input("Task description: ").strip()
            try:
                task_id = manager.add(task_name, task_description)
                print(f"Task added successfully with ID: {task_id}")
            except ValueError as ve:
                print(f"Error: {ve}")

        elif command == "remove":
            task_id_str = input("Enter task ID to remove: ").strip()
            try:
                task_id = int(task_id_str)
                if manager.remove(task_id):
                    print("Task removed successfully.")
                else:
                    print("Task not found or invalid ID.")
            except ValueError:
                print("Invalid input. Please enter an integer for the task ID.")

        elif command == "search":
            term = input("Enter search term: ").strip()
            results = manager.search(term)
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
            task_id_str = input("Enter task ID to mark as finished: ").strip()
            try:
                task_id = int(task_id_str)
                if manager.finish(task_id):
                    print("Task marked as finished.")
                else:
                    print("Task not found or invalid ID.")
            except ValueError:
                print("Invalid input. Please enter an integer for the task ID.")

        elif command == "get_all":
            tasks = manager.get_all()
            if tasks:
                print("All tasks:")
                for task in tasks:
                    print(
                        f"ID: {task['id']}, Name: {task['task_name']}, "
                        f"Description: {task['task_description']}, Finished: {task['is_finished']}"
                    )
            else:
                print("No tasks found.")

        elif command == "clear_all":
            confirm = input("Are you sure you want to clear all tasks? (yes/no): ").strip().lower()
            if confirm == "yes":
                if manager.clear_all():
                    print("All tasks cleared successfully.")
                else:
                    print("Failed to clear tasks.")
            else:
                print("Clear all canceled.")

        elif command == "exit":
            print("Exiting application. Goodbye!")
            break

        else:
            print("Invalid command. Please try again.")


if __name__ == "__main__":
    main()
