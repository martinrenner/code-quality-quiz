
from typing import Dict, List, Optional
from datetime import datetime
import re

class TaskManager:
    """
    A class to manage todo tasks with basic CRUD operations.
    
    Attributes:
        _tasks (Dict): Internal storage for tasks
        _next_id (int): Counter for generating unique task IDs
    """
    
    def __init__(self):
        """Initialize an empty task manager."""
        self._tasks: Dict[int, dict] = {}
        self._next_id: int = 1

    def _validate_string_input(self, text: str, field_name: str) -> None:
        """
        Validate string input for task fields.
        
        Args:
            text: String to validate
            field_name: Name of the field being validated
            
        Raises:
            ValueError: If input is invalid
        """
        if not isinstance(text, str):
            raise ValueError(f"{field_name} must be a string")
        if not text.strip():
            raise ValueError(f"{field_name} cannot be empty")
        if len(text) > 200:  # Reasonable length limit
            raise ValueError(f"{field_name} is too long (max 200 characters)")
        if not re.match(r'^[\w\s\-.,!?()]+$', text):
            raise ValueError(f"{field_name} contains invalid characters")

    def _validate_task_id(self, task_id: int) -> None:
        """
        Validate task ID.
        
        Args:
            task_id: ID to validate
            
        Raises:
            ValueError: If ID is invalid
        """
        if not isinstance(task_id, int):
            raise ValueError("Task ID must be an integer")
        if task_id <= 0:
            raise ValueError("Task ID must be positive")
        if task_id not in self._tasks:
            raise ValueError("Task ID does not exist")

    def add(self, task_name: str, task_description: str) -> int:
        """
        Add a new task to the manager.
        
        Args:
            task_name: Name of the task
            task_description: Description of the task
            
        Returns:
            int: Unique ID of the created task
            
        Raises:
            ValueError: If inputs are invalid
        """
        self._validate_string_input(task_name, "Task name")
        self._validate_string_input(task_description, "Task description")

        task_id = self._next_id
        self._tasks[task_id] = {
            'id': task_id,
            'name': task_name.strip(),
            'description': task_description.strip(),
            'is_finished': False,
            'created_at': datetime.now()
        }
        self._next_id += 1
        return task_id

    def remove(self, task_id: int) -> bool:
        """
        Remove a task by its ID.
        
        Args:
            task_id: ID of the task to remove
            
        Returns:
            bool: True if task was removed, False otherwise
            
        Raises:
            ValueError: If task_id is invalid
        """
        self._validate_task_id(task_id)
        del self._tasks[task_id]
        return True

    def search(self, task_term: str) -> List[dict]:
        """
        Search tasks by name or description.
        
        Args:
            task_term: Search term
            
        Returns:
            List[dict]: List of matching tasks
            
        Raises:
            ValueError: If search term is invalid
        """
        self._validate_string_input(task_term, "Search term")
        term = task_term.lower().strip()
        
        return [
            self._format_task(task) for task in self._tasks.values()
            if term in task['name'].lower() or term in task['description'].lower()
        ]

    def finish(self, task_id: int) -> bool:
        """
        Mark a task as completed.
        
        Args:
            task_id: ID of the task to mark as completed
            
        Returns:
            bool: True if task was marked as completed
            
        Raises:
            ValueError: If task_id is invalid
        """
        self._validate_task_id(task_id)
        if self._tasks[task_id]['is_finished']:
            return False
        self._tasks[task_id]['is_finished'] = True
        return True

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
            bool: True if all tasks were removed
        """
        self._tasks.clear()
        return True

    def _format_task(self, task: dict) -> dict:
        """
        Format a task for output.
        
        Args:
            task: Task dictionary
            
        Returns:
            dict: Formatted task dictionary
        """
        return {
            'id': task['id'],
            'task_name': task['name'],
            'task_description': task['description'],
            'is_finished': task['is_finished']
        }


# Usage example
task_manager = TaskManager()

# Add tasks
task1_id = task_manager.add("Complete report", "Finish quarterly report")
task2_id = task_manager.add("Email client", "Send project updates")

# Get all tasks
all_tasks = task_manager.get_all()

# Search tasks
results = task_manager.search("report")

# Mark task as complete
task_manager.finish(task1_id)

# Remove task
task_manager.remove(task2_id)

# Clear all tasks
task_manager.clear_all()
