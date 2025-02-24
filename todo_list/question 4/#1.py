import sys

class TaskManager:
    """
    A class to manage tasks for a console-based todo list application.
    
    Each task is stored as a dictionary with the following keys:
        - id: Unique integer identifier for the task.
        - task_name: Name/title of the task.
        - task_description: Detailed description of the task.
        - is_finished: Boolean flag indicating if the task has been completed.
    
    Tasks are stored in an in-memory dictionary for O(1) lookup by ID.
    """
    
    def __init__(self):
        """Initializes a new TaskManager instance with an empty task store."""
        self.tasks = {}  # Dictionary mapping task_id to task information.
        self.next_id = 1  # Counter to generate unique task IDs.

    def add(self, task_name: str, task_description: str) -> int:
        """
        Adds a new task to the todo list.

        Args:
            task_name (str): The name of the task.
            task_description (str): The detailed description of the task.

        Returns:
            int: The unique ID of the newly added task.

        Raises:
            ValueError: If task_name or task_description is an empty string.
        """
        if not isinstance(task_name, str) or not task_name.strip():
            raise ValueError("Task name must be a non-empty string.")
        if not isinstance(task_description, str) or not task_description.strip():
            raise ValueError("Task description must be a non-empty string.")
            
        task_id = self.next_id
        self.tasks[task_id] = {
            'id': task_id,
            'task_name': task_name.strip(),
            'task_description': task_description.strip(),
            'is_finished': False
        }
        self.next_id += 1
        return task_id

    def remove(self, task_id: int) -> bool:
        """
        Removes a task by its ID.

        Args:
            task_id (int): The unique identifier of the task to remove.

        Returns:
            bool: True if the task was successfully removed, False if the task does not exist.

        Raises:
            ValueError: If task_id is not a positive integer.
        """
        if not isinstance(task_id, int) or task_id < 1:
            raise ValueError("Task ID must be a positive integer.")

        if task_id in self.tasks:
            del self.tasks[task_id]
            return True
        return False

    def search(self, task_term: str) -> list:
        """
        Searches for tasks by matching the search term in the task name or description.

        Args:
            task_term (str): Term to search for within tasks.

        Returns:
            list[dict]: A list of tasks (as dictionaries) that match the search term.
            
        Raises:
            ValueError: If task_term is not a non-empty string.
        """
        if not isinstance(task_term, str) or not task_term.strip():
            raise ValueError("Search term must be a non-empty string.")

        term_lower = task_term.lower()
        matching_tasks = []
        for task in self.tasks.values():
            if (term_lower in task['task_name'].lower() or 
                term_lower in task['task_description'].lower()):
                matching_tasks.append(task.copy())
        return matching_tasks

    def finish(self, task_id: int) -> bool:
        """
        Marks a task as completed.

        Args:
            task_id (int): The unique identifier of the task to mark as finished.

        Returns:
            bool: True if the task exists and was marked as finished, False otherwise.

        Raises:
            ValueError: If task_id is not a positive integer.
        """
        if not isinstance(task_id, int) or task_id < 1:
            raise ValueError("Task ID must be a positive integer.")

        if task_id in self.tasks:
            self.tasks[task_id]['is_finished'] = True
            return True
        return False

    def get_all(self) -> list:
        """
        Retrieves all tasks with their details.

        Returns:
            list[dict]: A list of all tasks, each represented as a dictionary.
        """
        return [task.copy() for task in self.tasks.values()]

    def clear_all(self) -> bool:
        """
        Deletes all tasks.

        Returns:
            bool: True after successfully clearing all tasks.
        """
        self.tasks.clear()
        return True

def display_task(task: dict) -> None:
    """
    Displays a single task in the format (id, task_name, task_description, is_finished).

    Args:
        task (dict): The task dictionary to display.
    """
    print(f"({task['id']}, {task['task_name']}, {task['task_description']}, {task['is_finished']})")

def main():
    """
    Main entry point for the console-based todo list app.
    
    The user is presented with a menu to interact with the TaskManager.
    """
    task_manager = TaskManager()
    
    menu = """
========== Todo List App ==========
1. Add Task
2. Remove Task
3. Search Tasks
4. Mark Task as Finished
5. Get All Tasks
6. Clear All Tasks
7. Exit
===================================
"""

    while True:
        print(menu)
        choice = input("Enter your choice (1-7): ").strip()
        
        if choice == '1':
            # Add a new task
            try:
                task_name = input("Enter the task name: ").strip()
                task_description = input("Enter the task description: ").strip()
                task_id = task_manager.add(task_name, task_description)
                print(f"Task added successfully with ID: {task_id}\n")
            except ValueError as ve:
                print(f"Error: {ve}\n")
                
        elif choice == '2':
            # Remove an existing task
            try:
                task_id_input = input("Enter the task ID to remove: ").strip()
                task_id = int(task_id_input)
                if task_manager.remove(task_id):
                    print("Task removed successfully.\n")
                else:
                    print("Task not found.\n")
            except ValueError as ve:
                print(f"Error: {ve}\n")
                
        elif choice == '3':
            # Search for tasks
            try:
                term = input("Enter the search term: ").strip()
                results = task_manager.search(term)
                if results:
                    print("Matching tasks:")
                    for task in results:
                        display_task(task)
                    print()
                else:
                    print("No matching tasks found.\n")
            except ValueError as ve:
                print(f"Error: {ve}\n")
                
        elif choice == '4':
            # Mark a task as finished
            try:
                task_id_input = input("Enter the task ID to mark as finished: ").strip()
                task_id = int(task_id_input)
                if task_manager.finish(task_id):
                    print("Task marked as finished.\n")
                else:
                    print("Task not found.\n")
            except ValueError as ve:
                print(f"Error: {ve}\n")
                
        elif choice == '5':
            # List all tasks
            tasks = task_manager.get_all()
            if tasks:
                print("All tasks:")
                for task in tasks:
                    display_task(task)
                print()
            else:
                print("No tasks found.\n")
                
        elif choice == '6':
            # Clear all tasks
            confirm = input("Are you sure you want to clear all tasks? (yes/no): ").strip().lower()
            if confirm == "yes":
                task_manager.clear_all()
                print("All tasks have been cleared.\n")
            else:
                print("Clear all cancelled.\n")
                
        elif choice == '7':
            # Exit the program
            print("Exiting the Todo List App. Goodbye!")
            sys.exit(0)
        else:
            print("Invalid choice. Please select a valid option (1-7).\n")

if __name__ == '__main__':
    main()
