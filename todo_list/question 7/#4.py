
from typing import List, Dict, Optional
from datetime import datetime
import re

class TaskManager:
    """
    A class to manage todo tasks with CRUD operations and additional functionality.
    Implements ISO/IEC 25010 quality requirements.
    """

    def __init__(self):
        """Initialize the TaskManager with an empty task storage and counter."""
        self._tasks: Dict[int, Dict] = {}
        self._counter: int = 1

    def add(self, task_name: str, task_description: str) -> int:
        """
        Add a new task to the todo list.

        Args:
            task_name (str): The name of the task
            task_description (str): The description of the task

        Returns:
            int: The unique ID of the created task

        Raises:
            ValueError: If task_name or task_description is empty or invalid
        """
        # Input validation
        if not self._validate_input(task_name) or not self._validate_input(task_description):
            raise ValueError("Task name and description must be non-empty strings")

        # Create task with sanitized inputs
        task = {
            'id': self._counter,
            'task_name': self._sanitize_input(task_name),
            'task_description': self._sanitize_input(task_description),
            'is_finished': False,
            'created_at': datetime.now()
        }

        self._tasks[self._counter] = task
        self._counter += 1
        return task['id']

    def remove(self, task_id: int) -> bool:
        """
        Remove a task by its ID.

        Args:
            task_id (int): The unique identifier of the task

        Returns:
            bool: True if task was removed, False if task wasn't found
        """
        if not isinstance(task_id, int) or task_id < 1:
            return False
        
        return self._tasks.pop(task_id, None) is not None

    def search(self, task_term: str) -> List[Dict]:
        """
        Search tasks by name or description.

        Args:
            task_term (str): The search term

        Returns:
            List[Dict]: List of matching tasks
        """
        if not self._validate_input(task_term):
            return []

        sanitized_term = self._sanitize_input(task_term).lower()
        return [
            self._format_task(task) for task in self._tasks.values()
            if sanitized_term in task['task_name'].lower() or 
               sanitized_term in task['task_description'].lower()
        ]

    def finish(self, task_id: int) -> bool:
        """
        Mark a task as completed.

        Args:
            task_id (int): The unique identifier of the task

        Returns:
            bool: True if task was marked as completed, False if task wasn't found
        """
        if task_id not in self._tasks:
            return False
        
        self._tasks[task_id]['is_finished'] = True
        return True

    def get_all(self) -> List[Dict]:
        """
        Retrieve all tasks.

        Returns:
            List[Dict]: List of all tasks
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

    @staticmethod
    def _validate_input(text: str) -> bool:
        """
        Validate input string.

        Args:
            text (str): Input string to validate

        Returns:
            bool: True if input is valid, False otherwise
        """
        return isinstance(text, str) and text.strip() != ""

    @staticmethod
    def _sanitize_input(text: str) -> str:
        """
        Sanitize input string by removing excessive whitespace and special characters.

        Args:
            text (str): Input string to sanitize

        Returns:
            str: Sanitized string
        """
        # Remove special characters except basic punctuation
        text = re.sub(r'[^\w\s.,!?-]', '', text)
        # Normalize whitespace
        return ' '.join(text.split())

    @staticmethod
    def _format_task(task: Dict) -> Dict:
        """
        Format task for output.

        Args:
            task (Dict): Task to format

        Returns:
            Dict: Formatted task with required fields
        """
        return {
            'id': task['id'],
            'task_name': task['task_name'],
            'task_description': task['task_description'],
            'is_finished': task['is_finished']
        }


def main():
    # Create TaskManager instance
    task_manager = TaskManager()

    try:
        # Add some tasks
        task1_id = task_manager.add("Complete project", "Finish the Python todo list project")
        task2_id = task_manager.add("Buy groceries", "Get milk, bread, and eggs")

        # Search for tasks
        search_results = task_manager.search("project")
        print("Search results:", search_results)

        # Mark task as completed
        task_manager.finish(task1_id)

        # Get all tasks
        all_tasks = task_manager.get_all()
        print("All tasks:", all_tasks)

        # Remove a task
        task_manager.remove(task2_id)

        # Clear all tasks
        task_manager.clear_all()

    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
