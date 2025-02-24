from typing import List, Dict, Optional
from datetime import datetime
import re

class TaskManager:
    """
    A class to manage tasks in a to-do list application.
    
    Attributes:
        _tasks (dict): Dictionary storing tasks with their IDs as keys
        _next_id (int): Counter for generating unique task IDs
    """
    
    def __init__(self):
        """Initialize an empty task manager."""
        self._tasks: Dict[int, Dict] = {}
        self._next_id: int = 1

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
        # Validate inputs
        if not task_name or not task_name.strip():
            raise ValueError("Task name cannot be empty")
        if not task_description or not task_description.strip():
            raise ValueError("Task description cannot be empty")

        # Create new task
        task_id = self._next_id
        self._tasks[task_id] = {
            'id': task_id,
            'task_name': task_name.strip(),
            'task_description': task_description.strip(),
            'is_finished': False,
            'created_at': datetime.now()
        }
        self._next_id += 1
        return task_id

    def remove(self, task_id: int) -> bool:
        """
        Remove a task by its ID.

        Args:
            task_id (int): ID of the task to remove

        Returns:
            bool: True if task was removed, False if task wasn't found
        """
        if not isinstance(task_id, int) or task_id < 1:
            raise ValueError("Invalid task ID")
            
        return bool(self._tasks.pop(task_id, None))

    def search(self, task_term: str) -> List[Dict]:
        """
        Search tasks by name or description.

        Args:
            task_term (str): Search term to match against task names and descriptions

        Returns:
            List[Dict]: List of matching tasks

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
            task_id (int): ID of the task to mark as completed

        Returns:
            bool: True if task was marked as completed, False if task wasn't found
        """
        if not isinstance(task_id, int) or task_id < 1:
            raise ValueError("Invalid task ID")
            
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
        return [self._format_task(task) for task in self._tasks.values()]

    def clear_all(self) -> bool:
        """
        Remove all tasks from the system.

        Returns:
            bool: True if operation was successful
        """
        self._tasks.clear()
        return True

    def _format_task(self, task: Dict) -> Dict:
        """
        Format a task dictionary to match the required output format.

        Args:
            task (Dict): Task dictionary with full details

        Returns:
            Dict: Formatted task dictionary with required fields
        """
        return {
            'id': task['id'],
            'task_name': task['task_name'],
            'task_description': task['task_description'],
            'is_finished': task['is_finished']
        }

    def _validate_task_id(self, task_id: int) -> bool:
        """
        Validate if a task ID exists in the system.

        Args:
            task_id (int): Task ID to validate

        Returns:
            bool: True if task ID exists, False otherwise
        """
        return task_id in self._tasks


# Example usage
task_manager = TaskManager()

# Add tasks
task_id = task_manager.add("Complete project", "Finish the Python project by Friday")
task_manager.add("Buy groceries", "Get milk, bread, and eggs")

# Mark task as complete
task_manager.finish(task_id)

# Search for tasks
results = task_manager.search("project")

# Get all tasks
all_tasks = task_manager.get_all()
