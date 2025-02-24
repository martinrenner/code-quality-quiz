"""
Console-Based To-Do List Application

This module implements a clean, modular, and efficient Python application for managing a to-do list.
It adheres to the ISO/IEC 25010 standard by providing proper architecture, error handling, efficiency,
and maintainability.

The application defines a TaskManager class with the following interface:
    - add(task_name: str, task_description: str) -> int
    - remove(task_id: int) -> bool
    - search(task_term: str) -> list[dict]
    - finish(task_id: int) -> bool
    - get_all() -> list[dict]
    - clear_all() -> bool

The tasks are stored in an in-memory data structure.
A simple console-based interface is provided for user interaction.
"""

from dataclasses import dataclass, asdict
from typing import List, Dict


@dataclass
class Task:
    """
    Data class representing a single task.
    Attributes:
        id (int): Unique task identifier.
        task_name (str): Name/title of the task.
        task_description (str): Detailed description of the task.
        is_finished (bool): True if the task has been marked as completed.
    """
    id: int
    task_name: str
    task_description: str
    is_finished: bool = False


class TaskManager:
    """
    A manager for to-do tasks. Provides methods for adding, removing, searching, finishing tasks,
    retrieving all tasks and clearing all tasks.
    """

    def __init__(self):
        """Initialize the TaskManager with an empty task store and starting ID."""
        self.tasks: Dict[int, Task] = {}
        self.next_id: int = 1

    def add(self, task_name: str, task_description: str) -> int:
        """
        Add a new task to the to-do list.
        Args:
            task_name (str): The name/title of the task. Must be a non-empty string.
            task_description (str): The description of the task.
        Returns:
            int: The unique ID assigned to the task.
        Raises:
            ValueError: If task_name is an empty string or not a string.
        """
        if not isinstance(task_name, str) or not task_name.strip():
            raise ValueError("Task name must be a non-empty string.")
        if not isinstance(task_description, str):
            raise ValueError("Task description must be a string.")

        task_id = self.next_id
        new_task = Task(id=task_id,
                        task_name=task_name.strip(),
                        task_description=task_description.strip())
        self.tasks[task_id] = new_task
        self.next_id += 1

        return task_id

    def remove(self, task_id: int) -> bool:
        """
        Remove a task from the to-do list by its ID.
        Args:
            task_id (int): The unique ID of the task to remove.
        Returns:
            bool: True if the task existed and was removed; False otherwise.
        """
        if not isinstance(task_id, int) or task_id <= 0:
            return False

        if task_id in self.tasks:
            del self.tasks[task_id]
            return True
        return False

    def search(self, task_term: str) -> List[Dict]:
        """
        Search for tasks by matching the search term in task name or description.
        Args:
            task_term (str): The term to search for.
        Returns:
            List[Dict]: A list of tasks (as dictionaries) that match the search criteria.
        """
        if not isinstance(task_term, str) or not task_term.strip():
            # Return empty list if search term is invalid or empty.
            return []

        term = task_term.lower().strip()
        results = []
        for task in self.tasks.values():
            if term in task.task_name.lower() or term in task.task_description.lower():
                results.append(asdict(task))
        return results

    def finish(self, task_id: int) -> bool:
        """
        Mark a task as finished/completed.
        Args:
            task_id (int): The unique ID of the task to mark as finished.
        Returns:
            bool: True if the task was found and marked finished; False otherwise.
        """
        if not isinstance(task_id, int) or task_id <= 0:
            return False

        task = self.tasks.get(task_id)
        if task:
            task.is_finished = True
            return True
        return False

    def get_all(self) -> List[Dict]:
        """
        Retrieve all tasks with their details.
        Returns:
            List[Dict]: A list of all tasks represented as dictionaries.
        """
        # Return tasks sorted by their ID for consistency.
        return [asdict(task) for task in sorted(self.tasks.values(), key=lambda t: t.id)]

    def clear_all(self) -> bool:
        """
        Delete all tasks in the to-do list.
        Returns:
            bool: True after all tasks have been cleared.
        """
        self.tasks.clear()
        return True


def print_task(task: Dict) -> None:
    """
    Prints the details of a single task.
    Args:
        task (Dict): The task dictionary containing id, task_name, task_description, and is_finished.
    """
    status = "Finished" if task.get("is_finished") else "Pending"
    print(f"ID: {task.get('id')}\n"
          f"Name: {task.get('task_name')}\n"
          f"Description: {task.get('task_description')}\n"
          f"Status: {status}\n"
          "---------------------------")


def main():
    """
    The main loop for the console-based to-do list application.
    """
    manager = TaskManager()

    menu = """
    ================================
    To-Do List Application Menu:
    1. Add Task
    2. Remove Task
    3. Search Tasks
    4. Finish Task
    5. Get All Tasks
    6. Clear All Tasks
    7. Exit
    ================================
    """

    while True:
        print(menu)
        choice = input("Enter your choice (1-7): ").strip()

        if choice == "1":
            # Add Task
            try:
                task_name = input("Enter task name: ").strip()
                task_description = input("Enter task description: ").strip()
                task_id = manager.add(task_name, task_description)
                print(f"Task added with ID: {task_id}\n")
            except ValueError as ve:
                print(f"Error: {ve}\n")

        elif choice == "2":
            # Remove Task
            task_id_input = input("Enter task ID to remove: ").strip()
            try:
                task_id = int(task_id_input)
                if manager.remove(task_id):
                    print(f"Task with ID {task_id} removed successfully.\n")
                else:
                    print(f"No task found with ID {task_id}.\n")
            except ValueError:
                print("Invalid ID. Please enter a valid integer.\n")

        elif choice == "3":
            # Search Tasks
            term = input("Enter search term: ").strip()
            results = manager.search(term)
            if results:
                print(f"Found {len(results)} matching task(s):")
                for task in results:
                    print_task(task)
            else:
                print("No tasks matched your search.\n")

        elif choice == "4":
            # Finish Task
            task_id_input = input("Enter task ID to mark as finished: ").strip()
            try:
                task_id = int(task_id_input)
                if manager.finish(task_id):
                    print(f"Task with ID {task_id} marked as finished.\n")
                else:
                    print(f"No task found with ID {task_id}.\n")
            except ValueError:
                print("Invalid ID. Please enter a valid integer.\n")

        elif choice == "5":
            # Get All Tasks
            tasks = manager.get_all()
            if tasks:
                print("All Tasks:")
                for task in tasks:
                    print_task(task)
            else:
                print("No tasks available.\n")

        elif choice == "6":
            # Clear All Tasks
            confirmation = input("Are you sure you want to clear all tasks? (y/n): ").strip().lower()
            if confirmation == "y":
                manager.clear_all()
                print("All tasks have been cleared.\n")
            else:
                print("Clear all tasks aborted.\n")

        elif choice == "7":
            print("Exiting To-Do List Application. Goodbye!")
            break

        else:
            print("Invalid choice. Please select a valid option from the menu.\n")


if __name__ == '__main__':
    main()
