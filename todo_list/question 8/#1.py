from typing import List, Dict, Optional
from datetime import datetime
import re

class TaskManager:
    """
    A class to manage todo tasks with CRUD operations and search functionality.
    Implements task management with in-memory storage and input validation.
    """

    def __init__(self):
        """Initialize TaskManager with empty task storage and counter."""
        self._tasks: Dict[int, Dict] = {}
        self._task_counter: int = 0

    def add(self, task_name: str, task_description: str) -> int:
        """
        Add a new task to the task manager.

        Args:
            task_name (str): Name of the task
            task_description (str): Description of the task

        Returns:
            int: Unique ID of the created task

        Raises:
            ValueError: If task_name or task_description is empty or invalid
        """
        # Input validation
        if not self._validate_input(task_name) or not self._validate_input(task_description):
            raise ValueError("Task name and description cannot be empty or contain only whitespace")

        # Generate new task ID
        self._task_counter += 1
        
        # Create new task
        self._tasks[self._task_counter] = {
            'id': self._task_counter,
            'task_name': task_name.strip(),
            'task_description': task_description.strip(),
            'is_finished': False,
            'created_at': datetime.now()
        }
        
        return self._task_counter

    def remove(self, task_id: int) -> bool:
        """
        Remove a task by its ID.

        Args:
            task_id (int): ID of the task to remove

        Returns:
            bool: True if task was removed, False if task wasn't found
        """
        if not isinstance(task_id, int) or task_id <= 0:
            return False
        
        return self._tasks.pop(task_id, None) is not None

    def search(self, task_term: str) -> List[Dict]:
        """
        Search tasks by name or description.

        Args:
            task_term (str): Search term to match against task name or description

        Returns:
            List[Dict]: List of matching tasks
        """
        if not self._validate_input(task_term):
            return []

        search_term = task_term.lower().strip()
        return [
            self._format_task_output(task) for task in self._tasks.values()
            if search_term in task['task_name'].lower() or 
            search_term in task['task_description'].lower()
        ]

    def finish(self, task_id: int) -> bool:
        """
        Mark a task as completed.

        Args:
            task_id (int): ID of the task to mark as completed

        Returns:
            bool: True if task was marked as completed, False if task wasn't found
        """
        if task_id in self._tasks:
            self._tasks[task_id]['is_finished'] = True
            return True
        return False

    def get_all(self) -> List[Dict]:
        """
        Get all tasks in the system.

        Returns:
            List[Dict]: List of all tasks
        """
        return [self._format_task_output(task) for task in self._tasks.values()]

    def clear_all(self) -> bool:
        """
        Remove all tasks from the system.

        Returns:
            bool: True if operation was successful
        """
        self._tasks.clear()
        return True

    @staticmethod
    def _validate_input(input_str: str) -> bool:
        """
        Validate input string.

        Args:
            input_str (str): String to validate

        Returns:
            bool: True if input is valid, False otherwise
        """
        if not isinstance(input_str, str):
            return False
        
        # Check if string is empty or contains only whitespace
        if not input_str or not input_str.strip():
            return False
        
        # Check for potentially harmful characters
        if re.search(r'[<>{}]', input_str):
            return False
            
        return True

    @staticmethod
    def _format_task_output(task: Dict) -> Dict:
        """
        Format task output to match required format.

        Args:
            task (Dict): Task to format

        Returns:
            Dict: Formatted task
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
        task1_id = task_manager.add("Complete report", "Finish quarterly report for Q2")
        task2_id = task_manager.add("Team meeting", "Attend team sync meeting at 2 PM")
        
        # Get all tasks
        print("All tasks:", task_manager.get_all())
        
        # Search for tasks
        print("Search results:", task_manager.search("report"))
        
        # Mark task as completed
        task_manager.finish(task1_id)
        
        # Remove a task
        task_manager.remove(task2_id)
        
        # Get final task list
        print("Final task list:", task_manager.get_all())
        
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
