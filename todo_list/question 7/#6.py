class TaskManager:
    """
    Manages a collection of tasks stored in memory.
    Each task is represented as a dictionary with the following keys:
      - id (int)
      - task_name (str)
      - task_description (str)
      - is_finished (bool)
    """

    def __init__(self):
        """Initializes the TaskManager with an empty task store and an ID counter."""
        self._tasks = {}  # Internal dict to store tasks by their unique ID.
        self._next_id = 1

    def add(self, task_name: str, task_description: str) -> int:
        """
        Adds a new task with the given name and description.

        Args:
            task_name (str): The name of the task.
            task_description (str): A description of the task.

        Returns:
            int: The unique ID assigned to the new task.

        Raises:
            ValueError: If task_name or task_description is empty.
        """
        if not task_name.strip():
            raise ValueError("Task name cannot be empty.")
        if not task_description.strip():
            raise ValueError("Task description cannot be empty.")

        task_id = self._next_id
        self._next_id += 1

        self._tasks[task_id] = {
            'id': task_id,
            'task_name': task_name,
            'task_description': task_description,
            'is_finished': False
        }
        return task_id

    def remove(self, task_id: int) -> bool:
        """
        Removes a task by its unique ID.

        Args:
            task_id (int): The unique ID of the task to remove.

        Returns:
            bool: True if the removal was successful, False if the task does not exist
                  or if the task_id is invalid.
        """
        if not isinstance(task_id, int) or task_id < 1:
            return False
        return self._tasks.pop(task_id, None) is not None

    def search(self, task_term: str) -> list[dict]:
        """
        Searches for tasks that contain the provided search term in their name or description.

        Args:
            task_term (str): The search keyword.

        Returns:
            list[dict]: A list of task dictionaries matching the search criteria.
        """
        if task_term is None:
            return []
        term_lower = task_term.lower()
        return [
            task for task in self._tasks.values()
            if term_lower in task['task_name'].lower() or term_lower in task['task_description'].lower()
        ]

    def finish(self, task_id: int) -> bool:
        """
        Marks the specified task as finished.

        Args:
            task_id (int): The unique ID of the task to complete.

        Returns:
            bool: True if the task was marked as finished, or False if not found/invalid.
        """
        if not isinstance(task_id, int) or task_id < 1:
            return False
        task = self._tasks.get(task_id)
        if task is None:
            return False
        task['is_finished'] = True
        return True

    def get_all(self) -> list[dict]:
        """
        Retrieves all tasks.

        Returns:
            list[dict]: A list of all tasks, each task represented as a dictionary.
        """
        return list(self._tasks.values())

    def clear_all(self) -> bool:
        """
        Clears all tasks from the manager.

        Returns:
            bool: Always True as the operation succeeds.
        """
        self._tasks.clear()
        return True


def print_task(task: dict) -> None:
    """
    Prints out a task in a readable format.

    Args:
        task (dict): A dictionary containing task details.
    """
    status = "✓" if task['is_finished'] else "✗"
    print(f"ID: {task['id']} | Name: {task['task_name']} | Description: {task['task_description']} | Finished: {status}")


def display_all_tasks(task_manager: TaskManager) -> None:
    """
    Prints all tasks stored in the TaskManager.

    Args:
        task_manager (TaskManager): The instance managing tasks.
    """
    tasks = task_manager.get_all()
    if not tasks:
        print("No tasks available.")
    else:
        print("\nCurrent Tasks:")
        for task in tasks:
            print_task(task)


def main():
    """
    Runs the console-based to-do list application, allowing the user to manage tasks.
    Available commands are:
      - add:      Add a new task.
      - remove:   Remove an existing task by its ID.
      - search:   Search tasks by a term in their name or description.
      - finish:   Mark a task as completed.
      - get_all:  List all tasks.
      - clear_all:Delete all tasks.
      - help:     Display the list of commands.
      - exit:     Quit the application.
    """
    task_manager = TaskManager()
    print("Welcome to the To-Do List Application!")
    print("Type 'help' to see the list of available commands.")

    while True:
        command = input("\nCommand: ").strip().lower()

        if command == "help":
            print("\nAvailable commands:")
            print("  add       - Add a new task")
            print("  remove    - Remove a task by ID")
            print("  search    - Search tasks by a term")
            print("  finish    - Mark a task as finished by ID")
            print("  get_all   - List all tasks")
            print("  clear_all - Delete all tasks")
            print("  exit      - Quit the application")

        elif command == "add":
            try:
                task_name = input("Enter task name: ").strip()
                task_description = input("Enter task description: ").strip()
                task_id = task_manager.add(task_name, task_description)
                print(f"Task added successfully with ID {task_id}.")
            except ValueError as ve:
                print(f"Error: {ve}")

        elif command == "remove":
            task_id_str = input("Enter task ID to remove: ").strip()
            try:
                task_id = int(task_id_str)
                if task_manager.remove(task_id):
                    print(f"Task ID {task_id} removed successfully.")
                else:
                    print(f"Task ID {task_id} not found or invalid.")
            except ValueError:
                print("Invalid input. Please enter a valid integer for task ID.")

        elif command == "search":
            term = input("Enter search term: ").strip()
            results = task_manager.search(term)
            if results:
                print(f"Found {len(results)} matching task(s):")
                for task in results:
                    print_task(task)
            else:
                print("No matching tasks found.")

        elif command == "finish":
            task_id_str = input("Enter task ID to mark as finished: ").strip()
            try:
                task_id = int(task_id_str)
                if task_manager.finish(task_id):
                    print(f"Task ID {task_id} marked as finished.")
                else:
                    print(f"Task ID {task_id} not found or invalid.")
            except ValueError:
                print("Invalid input. Please enter a valid integer for task ID.")

        elif command == "get_all":
            display_all_tasks(task_manager)

        elif command == "clear_all":
            confirmation = input("Are you sure you want to clear all tasks? (yes/no): ").strip().lower()
            if confirmation == "yes":
                task_manager.clear_all()
                print("All tasks have been cleared.")
            else:
                print("Operation cancelled.")

        elif command == "exit":
            print("Exiting the application. Goodbye!")
            break

        else:
            print("Unknown command. Type 'help' to see available commands.")


if __name__ == "__main__":
    main()
