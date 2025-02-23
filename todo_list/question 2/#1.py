
#!/usr/bin/env python3
"""
Console-based Todo List Application

This application uses a TaskManager class to manage tasks using an in-memory data structure.
It provides functionality to add, remove, search, finish, retrieve, and clear tasks.
The code is designed with ISO/IEC 25010 quality attributes in mind, ensuring modularity,
readability, performance, and robust error handling.
"""


class TaskManager:
    """
    Manages a list of tasks in memory. Provides methods to add, remove, search, finish,
    retrieve all tasks, and clear all tasks.
    """
    
    def __init__(self) -> None:
        """
        Initializes the TaskManager with an empty task list and starting unique ID.
        """
        self.tasks = {}  # Stores tasks with key as task id and value as task dictionary.
        self.next_id = 1  # Next unique id to be assigned.

    def add(self, task_name: str, task_description: str) -> int:
        """
        Adds a new task to the list.

        :param task_name: Name of the task.
        :param task_description: Description of the task.
        :return: A unique integer ID for the newly added task.
        :raises ValueError: If task_name or task_description is empty.
        """
        if not task_name.strip():
            raise ValueError("Task name cannot be empty.")
        if not task_description.strip():
            raise ValueError("Task description cannot be empty.")

        task_id = self.next_id
        self.tasks[task_id] = {
            "id": task_id,
            "task_name": task_name,
            "task_description": task_description,
            "is_finished": False
        }
        self.next_id += 1
        return task_id

    def remove(self, task_id: int) -> bool:
        """
        Removes a task by its unique ID.

        :param task_id: Unique ID of the task to remove.
        :return: True if the task was successfully removed, False otherwise.
        """
        # Validate task_id
        if not isinstance(task_id, int) or task_id < 1:
            return False

        if task_id in self.tasks:
            del self.tasks[task_id]
            return True
        return False

    def search(self, task_term: str) -> list[dict]:
        """
        Searches for tasks whose name or description contains the search term (case-insensitive).

        :param task_term: Term to search within task names and descriptions.
        :return: A list of tasks (each as a dict) matching the search term.
        :raises ValueError: If the search term is empty.
        """
        if not task_term.strip():
            raise ValueError("Search term cannot be empty.")
        
        search_lower = task_term.lower()
        results = []
        for task in self.tasks.values():
            if (search_lower in task["task_name"].lower() or
                    search_lower in task["task_description"].lower()):
                results.append(task.copy())
        return results

    def finish(self, task_id: int) -> bool:
        """
        Marks a task as finished using its unique ID.

        :param task_id: Unique ID of the task to mark as completed.
        :return: True if the task was successfully marked as finished, False otherwise.
        """
        if not isinstance(task_id, int) or task_id < 1:
            return False

        if task_id in self.tasks:
            self.tasks[task_id]["is_finished"] = True
            return True
        return False

    def get_all(self) -> list[dict]:
        """
        Retrieves all tasks.

        :return: A list of all tasks, where each task is represented as a dict containing:
                 (id, task_name, task_description, is_finished)
        """
        # Sorted by task id for consistency.
        return [self.tasks[tid].copy() for tid in sorted(self.tasks)]

    def clear_all(self) -> bool:
        """
        Removes all tasks from the list.

        :return: True upon successful clearance of tasks.
        """
        self.tasks.clear()
        return True


def print_task(task: dict) -> None:
    """
    Prints a task's details in the format: (id, task_name, task_description, is_finished)

    :param task: A dictionary containing the task details.
    """
    print(f"({task['id']}, {task['task_name']}, {task['task_description']}, {task['is_finished']})")


def display_menu() -> None:
    """
    Displays the menu options for the Todo List application.
    """
    print("\n--- Todo List Application Menu ---")
    print("1. Add Task")
    print("2. Remove Task")
    print("3. Search Tasks")
    print("4. Mark Task as Finished")
    print("5. Get All Tasks")
    print("6. Clear All Tasks")
    print("7. Exit")


def main() -> None:
    """
    Main method to run the console-based todo list application.
    It parses user input and calls the appropriate methods from TaskManager.
    """
    manager = TaskManager()

    while True:
        display_menu()
        choice = input("Enter your choice (1-7): ").strip()

        if choice == "1":
            # Add Task
            try:
                name = input("Enter task name: ").strip()
                description = input("Enter task description: ").strip()
                task_id = manager.add(name, description)
                print(f"Task added successfully with ID: {task_id}")
            except ValueError as ve:
                print(f"Error: {ve}")

        elif choice == "2":
            # Remove Task
            try:
                task_id_input = input("Enter task ID to remove: ").strip()
                task_id = int(task_id_input)
                if manager.remove(task_id):
                    print("Task removed successfully.")
                else:
                    print("Task removal failed. Please check if the task ID exists.")
            except ValueError:
                print("Invalid input. Please enter a valid integer for task ID.")

        elif choice == "3":
            # Search Tasks
            search_term = input("Enter search term: ").strip()
            try:
                results = manager.search(search_term)
                if results:
                    print("Search Results:")
                    for task in results:
                        print_task(task)
                else:
                    print("No matching tasks found.")
            except ValueError as ve:
                print(f"Error: {ve}")

        elif choice == "4":
            # Mark Task as Finished
            try:
                task_id_input = input("Enter task ID to mark as finished: ").strip()
                task_id = int(task_id_input)
                if manager.finish(task_id):
                    print("Task marked as finished.")
                else:
                    print("Failed to mark task as finished. Please check if the task ID exists.")
            except ValueError:
                print("Invalid input. Please enter a valid integer for task ID.")

        elif choice == "5":
            # Get All Tasks
            tasks = manager.get_all()
            if tasks:
                print("All Tasks:")
                for task in tasks:
                    print_task(task)
            else:
                print("No tasks available.")

        elif choice == "6":
            # Clear All Tasks
            confirmation = input("Are you sure you want to remove all tasks? (yes/no): ").strip().lower()
            if confirmation == "yes":
                manager.clear_all()
                print("All tasks have been cleared.")
            else:
                print("Clear all tasks operation cancelled.")

        elif choice == "7":
            # Exit the application
            print("Exiting the application. Goodbye!")
            break

        else:
            print("Invalid choice. Please select a valid option from the menu.")


if __name__ == "__main__":
    main()
