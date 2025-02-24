
from typing import List, Dict, Optional
from datetime import datetime

class TaskManager:
    """
    A class to manage todo tasks with CRUD operations and search functionality.
    Implements in-memory storage with efficient operations and comprehensive error handling.
    """

    def __init__(self):
        """Initialize the TaskManager with an empty task storage and task counter."""
        self._tasks: Dict[int, dict] = {}
        self._task_counter: int = 0

    def add(self, task_name: str, task_description: str) -> int:
        """
        Add a new task to the task manager.

        Args:
            task_name (str): The name of the task
            task_description (str): The description of the task

        Returns:
            int: The unique ID of the created task

        Raises:
            ValueError: If task_name or task_description is empty or invalid
        """
        # Input validation
        if not task_name or not task_name.strip():
            raise ValueError("Task name cannot be empty")
        if not task_description or not task_description.strip():
            raise ValueError("Task description cannot be empty")

        # Sanitize inputs
        task_name = task_name.strip()
        task_description = task_description.strip()

        # Generate new task ID
        self._task_counter += 1
        task_id = self._task_counter

        # Create and store new task
        self._tasks[task_id] = {
            'id': task_id,
            'task_name': task_name,
            'task_description': task_description,
            'is_finished': False,
            'created_at': datetime.now()
        }

        return task_id

    def remove(self, task_id: int) -> bool:
        """
        Remove a task by its ID.

        Args:
            task_id (int): The ID of the task to remove

        Returns:
            bool: True if task was removed, False if task wasn't found

        Raises:
            ValueError: If task_id is invalid
        """
        if not isinstance(task_id, int) or task_id <= 0:
            raise ValueError("Invalid task ID")

        return self._tasks.pop(task_id, None) is not None

    def search(self, task_term: str) -> List[dict]:
        """
        Search tasks by name or description.

        Args:
            task_term (str): The search term to look for

        Returns:
            List[dict]: List of tasks matching the search term

        Raises:
            ValueError: If search term is empty or invalid
        """
        if not task_term or not task_term.strip():
            raise ValueError("Search term cannot be empty")

        task_term = task_term.lower().strip()
        results = []

        for task in self._tasks.values():
            if (task_term in task['task_name'].lower() or 
                task_term in task['task_description'].lower()):
                results.append(self._format_task(task))

        return results

    def finish(self, task_id: int) -> bool:
        """
        Mark a task as completed.

        Args:
            task_id (int): The ID of the task to mark as completed

        Returns:
            bool: True if task was marked as completed, False if task wasn't found

        Raises:
            ValueError: If task_id is invalid
        """
        if not isinstance(task_id, int) or task_id <= 0:
            raise ValueError("Invalid task ID")

        if task_id in self._tasks:
            self._tasks[task_id]['is_finished'] = True
            return True
        return False

    def get_all(self) -> List[dict]:
        """
        Get all tasks.

        Returns:
            List[dict]: List of all tasks
        """
        return [self._format_task(task) for task in self._tasks.values()]

    def clear_all(self) -> bool:
        """
        Remove all tasks.

        Returns:
            bool: True if operation was successful
        """
        self._tasks.clear()
        return True

    def _format_task(self, task: dict) -> dict:
        """
        Format a task for output.

        Args:
            task (dict): The task to format

        Returns:
            dict: Formatted task with selected fields
        """
        return {
            'id': task['id'],
            'task_name': task['task_name'],
            'task_description': task['task_description'],
            'is_finished': task['is_finished']
        }

def main():
    """Main function to demonstrate TaskManager usage."""
    task_manager = TaskManager()

    try:
        # Add some sample tasks
        task1_id = task_manager.add("Complete project", "Finish the Python project by Friday")
        task2_id = task_manager.add("Buy groceries", "Get milk, bread, and eggs")
        
        # Display all tasks
        print("\nAll tasks:")
        for task in task_manager.get_all():
            print(task)

        # Mark a task as completed
        task_manager.finish(task1_id)
        
        # Search for tasks
        print("\nSearch results for 'project':")
        search_results = task_manager.search("project")
        for task in search_results:
            print(task)

        # Remove a task
        task_manager.remove(task2_id)
        
        print("\nRemaining tasks:")
        for task in task_manager.get_all():
            print(task)

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")

if __name__ == "__main__":
    main()
