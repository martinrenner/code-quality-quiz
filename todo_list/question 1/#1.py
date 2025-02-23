
"""
Console-based Todo List App based on ISO/IEC 25010 Requirements

This module implements a TaskManager class which supports the following operations:
- add(task_name: str, task_description: str) -> int
- remove(task_id: int) -> bool
- search(task_term: str) -> list[dict]
- finish(task_id: int) -> bool
- get_all() -> list[dict]
- clear_all() -> bool

It uses an in-memory dictionary to store tasks with unique IDs.
Each task is stored as a dictionary with keys:
    "id": int,
    "task_name": str,
    "task_description": str,
    "is_finished": bool

The console interface provides a menu for the user to interact with the TaskManager.
Proper input validation, error handling, and modular design are applied to ensure high 
code quality, performance, and security.
"""

class TaskManager:
    def __init__(self):
        """
        Initialize the TaskManager with an empty tasks store and a counter for unique IDs.
        """
        self.tasks = {}  # Dictionary to store tasks as id: task_dict
        self.next_id = 1

    def add(self, task_name: str, task_description: str) -> int:
        """
        Adds a new task to the todo list.
        
        Args:
            task_name (str): Name of the task. Must be a non-empty string.
            task_description (str): Description of the task. Must be a non-empty string.
            
        Returns:
            int: Unique task ID of the added task.
            
        Raises:
            ValueError: If task_name or task_description is empty.
        """
        if not task_name.strip() or not task_description.strip():
            raise ValueError("Task name and description cannot be empty.")
        
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
        Removes the task with the specified task_id.
        
        Args:
            task_id (int): The ID of the task to be removed. Must be positive.
            
        Returns:
            bool: True if the task was removed successfully, False otherwise.
        """
        if not isinstance(task_id, int) or task_id <= 0:
            print("Invalid task ID. It must be a positive integer.")
            return False
        
        if task_id in self.tasks:
            del self.tasks[task_id]
            return True
        else:
            print(f"Task with ID {task_id} not found.")
            return False

    def search(self, task_term: str) -> list:
        """
        Searches for tasks by matching the task_term in either the task's name or description.
        
        Args:
            task_term (str): The search term. Must be a non-empty string.
            
        Returns:
            list[dict]: List of tasks (dictionaries) matching the search term.
            
        Raises:
            ValueError: If the task_term is empty.
        """
        if not task_term.strip():
            raise ValueError("Search term cannot be empty.")
        
        term_lower = task_term.strip().lower()
        results = []
        for task in self.tasks.values():
            if (term_lower in task["task_name"].lower() or 
                term_lower in task["task_description"].lower()):
                results.append(task)
        return results

    def finish(self, task_id: int) -> bool:
        """
        Marks the task with the specified task_id as finished.
        
        Args:
            task_id (int): The ID of the task to mark as finished. Must be positive.
            
        Returns:
            bool: True if the task was successfully marked as finished, False otherwise.
        """
        if not isinstance(task_id, int) or task_id <= 0:
            print("Invalid task ID. It must be a positive integer.")
            return False

        task = self.tasks.get(task_id)
        if task is not None:
            task["is_finished"] = True
            return True
        else:
            print(f"Task with ID {task_id} not found.")
            return False

    def get_all(self) -> list:
        """
        Retrieves all tasks in the todo list.
        
        Returns:
            list[dict]: A list of all tasks with details.
        """
        return list(self.tasks.values())

    def clear_all(self) -> bool:
        """
        Clears all tasks from the todo list.
        
        Returns:
            bool: True if all tasks were successfully cleared.
        """
        self.tasks.clear()
        # Optionally, reset next_id for a 'fresh start'
        self.next_id = 1
        return True


def display_task(task: dict) -> None:
    """
    Displays a single task in a readable format.
    
    Args:
        task (dict): The task dictionary with keys 'id', 'task_name', 'task_description', and 'is_finished'.
    """
    status = "Done" if task["is_finished"] else "Pending"
    print(f"ID: {task['id']} | Name: {task['task_name']} | Description: {task['task_description']} | Status: {status}")


def main():
    """
    Console interface for interacting with the Todo List application.
    Provides a menu-driven command loop for the user.
    """
    manager = TaskManager()
    menu = (
        "\nTodo List App Menu:\n"
        "1. Add Task\n"
        "2. Remove Task\n"
        "3. Search Tasks\n"
        "4. Mark Task as Finished\n"
        "5. List All Tasks\n"
        "6. Clear All Tasks\n"
        "7. Exit\n"
        "Enter your choice (1-7): "
    )
    
    while True:
        try:
            choice = input(menu).strip()
            if choice == "1":
                print("\n-- Add Task --")
                task_name = input("Enter task name: ").strip()
                task_description = input("Enter task description: ").strip()
                try:
                    task_id = manager.add(task_name, task_description)
                    print(f"Task added successfully with ID: {task_id}")
                except ValueError as e:
                    print(f"Error: {e}")

            elif choice == "2":
                print("\n-- Remove Task --")
                try:
                    task_id = int(input("Enter task ID to remove: ").strip())
                    if manager.remove(task_id):
                        print("Task removed successfully.")
                except ValueError:
                    print("Invalid input. Please enter a valid integer for task ID.")

            elif choice == "3":
                print("\n-- Search Tasks --")
                task_term = input("Enter search term (in name or description): ").strip()
                try:
                    results = manager.search(task_term)
                    if results:
                        print(f"Found {len(results)} matching task(s):")
                        for task in results:
                            display_task(task)
                    else:
                        print("No tasks match your search.")
                except ValueError as e:
                    print(f"Error: {e}")

            elif choice == "4":
                print("\n-- Mark Task as Finished --")
                try:
                    task_id = int(input("Enter task ID to mark as finished: ").strip())
                    if manager.finish(task_id):
                        print("Task marked as finished.")
                except ValueError:
                    print("Invalid input. Please enter a valid integer for task ID.")

            elif choice == "5":
                print("\n-- List All Tasks --")
                tasks = manager.get_all()
                if tasks:
                    for task in tasks:
                        display_task(task)
                else:
                    print("There are no tasks at the moment.")

            elif choice == "6":
                print("\n-- Clear All Tasks --")
                confirm = input("Are you sure you want to clear all tasks? (yes/no): ").strip().lower()
                if confirm == "yes":
                    if manager.clear_all():
                        print("All tasks have been cleared.")
                else:
                    print("Clear operation cancelled.")

            elif choice == "7":
                print("Exiting Todo List App. Goodbye!")
                break

            else:
                print("Invalid option. Please enter a number between 1 and 7.")

        except Exception as e:
            # Catch all unexpected errors gracefully.
            print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
