"""
Console-based Todo List Application

This application implements a simple in-memory todo list manager using a TaskManager class.
It supports adding, removing, searching, marking tasks as finished, retrieving all tasks,
and clearing all tasks. The code adheres to best practices for modularity, efficiency,
and error handling according to ISO/IEC 25010 quality requirements.
"""

class TaskManager:
    """
    Manages tasks in a todo list using an in-memory data structure.
    Each task is represented as a dictionary with the following keys:
        - id: Unique task identifier.
        - task_name: Name/title of the task.
        - task_description: Description of the task.
        - is_finished: Boolean flag that indicates whether the task is completed.
    """

    def __init__(self):
        """Initializes the TaskManager with an empty tasks dictionary and id counter."""
        self.tasks = {}       # Stores tasks with key as task_id for quick lookup.
        self.next_id = 1      # Next available unique task ID.

    def add(self, task_name: str, task_description: str) -> int:
        """
        Adds a task to the todo list.
        
        Args:
            task_name (str): The name/title of the task (must not be empty).
            task_description (str): A description of the task (must not be empty).

        Returns:
            int: The unique task ID if added successfully; returns -1 if invalid input.
        """
        if not task_name.strip():
            print("Error: Task name cannot be empty.")
            return -1
        if not task_description.strip():
            print("Error: Task description cannot be empty.")
            return -1

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
        Removes a task by its ID.
        
        Args:
            task_id (int): The ID of the task to remove (must be positive).

        Returns:
            bool: True if the task was removed; False if the task does not exist or ID is invalid.
        """
        if task_id < 1:
            print("Error: Task ID must be a positive integer.")
            return False
        if task_id in self.tasks:
            del self.tasks[task_id]
            return True
        else:
            print(f"Error: Task with ID {task_id} does not exist.")
            return False

    def search(self, task_term: str) -> list:
        """
        Searches tasks by a keyword in the task name or description.
        
        Args:
            task_term (str): The search keyword (must not be empty).

        Returns:
            list: A list of task dictionaries that match the search term.
                  If no matches are found, an empty list is returned.
        """
        if not task_term.strip():
            print("Error: Search term cannot be empty.")
            return []

        term = task_term.lower().strip()
        results = []
        for task in self.tasks.values():
            if term in task["task_name"].lower() or term in task["task_description"].lower():
                results.append(task)
        if not results:
            print("No matching tasks found.")
        return results

    def finish(self, task_id: int) -> bool:
        """
        Marks a task as finished.
        
        Args:
            task_id (int): The ID of the task to mark as finished.

        Returns:
            bool: True if the task was successfully marked finished; False if the task does not exist or ID is invalid.
        """
        if task_id < 1:
            print("Error: Task ID must be a positive integer.")
            return False
        if task_id in self.tasks:
            if self.tasks[task_id]["is_finished"]:
                print("Warning: Task is already marked as finished.")
            else:
                self.tasks[task_id]["is_finished"] = True
            return True
        else:
            print(f"Error: Task with ID {task_id} does not exist.")
            return False

    def get_all(self) -> list:
        """
        Retrieves all tasks.
        
        Returns:
            list: A list of all task dictionaries.
        """
        return list(self.tasks.values())

    def clear_all(self) -> bool:
        """
        Clears all tasks from the todo list.
        
        Returns:
            bool: True after clearing all tasks.
        """
        self.tasks.clear()
        return True


def main():
    """
    Entry point for the console-based todo list app.
    Provides a command-line interface for interacting with the TaskManager.
    """
    task_manager = TaskManager()
    print("Welcome to the Todo List App!")
    print("Type 'help' to see available commands.\n")

    while True:
        try:
            user_input = input("Enter command: ").strip().lower()
        except (KeyboardInterrupt, EOFError):
            print("\nExiting the application.")
            break

        if user_input == "exit":
            print("Goodbye!")
            break

        elif user_input == "help":
            print("""
Available commands:
  add       - Add a new task.
  remove    - Remove a task by ID.
  search    - Search tasks by a keyword.
  finish    - Mark a task as finished.
  get_all   - List all tasks.
  clear_all - Clear all tasks.
  help      - Show this help message.
  exit      - Exit the application.
            """)

        elif user_input == "add":
            task_name = input("Enter task name: ")
            task_description = input("Enter task description: ")
            task_id = task_manager.add(task_name, task_description)
            if task_id > 0:
                print(f"Task added with ID: {task_id}")

        elif user_input == "remove":
            task_id_str = input("Enter task ID to remove: ")
            try:
                task_id = int(task_id_str)
                if task_manager.remove(task_id):
                    print(f"Task {task_id} removed successfully.")
            except ValueError:
                print("Error: Please enter a valid integer for task ID.")

        elif user_input == "search":
            term = input("Enter search term: ")
            results = task_manager.search(term)
            if results:
                print("Matching tasks:")
                for t in results:
                    print(f"(ID: {t['id']}, Name: {t['task_name']}, Description: {t['task_description']}, Finished: {t['is_finished']})")

        elif user_input == "finish":
            task_id_str = input("Enter task ID to mark as finished: ")
            try:
                task_id = int(task_id_str)
                if task_manager.finish(task_id):
                    print(f"Task {task_id} marked as finished.")
            except ValueError:
                print("Error: Please enter a valid integer for task ID.")

        elif user_input == "get_all":
            tasks = task_manager.get_all()
            if tasks:
                print("Current tasks:")
                for t in tasks:
                    print(f"(ID: {t['id']}, Name: {t['task_name']}, Description: {t['task_description']}, Finished: {t['is_finished']})")
            else:
                print("No tasks available.")

        elif user_input == "clear_all":
            confirm = input("Are you sure you want to clear all tasks? (y/n): ").strip().lower()
            if confirm == "y":
                task_manager.clear_all()
                print("All tasks have been cleared.")
            else:
                print("Operation cancelled.")

        else:
            print("Invalid command. Type 'help' to see available commands.")


if __name__ == "__main__":
    main()
