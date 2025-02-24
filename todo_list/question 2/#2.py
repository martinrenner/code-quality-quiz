
from typing import List, Dict, Optional
from datetime import datetime
import re

class TaskManager:
    """
    A class to manage todo tasks with basic CRUD operations.
    
    Attributes:
        _tasks (dict): Internal storage for tasks
        _next_id (int): Counter for generating unique task IDs
    """
    
    def __init__(self):
        """Initialize the TaskManager with empty task storage."""
        self._tasks: Dict[int, Dict] = {}
        self._next_id: int = 1

    def _validate_string_input(self, value: str, field_name: str) -> str:
        """
        Validates string input for task fields.
        
        Args:
            value: The string to validate
            field_name: Name of the field being validated
            
        Returns:
            Stripped string if valid
            
        Raises:
            ValueError: If input is empty or invalid
        """
        if not isinstance(value, str):
            raise ValueError(f"{field_name} must be a string")
        
        cleaned_value = value.strip()
        if not cleaned_value:
            raise ValueError(f"{field_name} cannot be empty")
            
        return cleaned_value

    def _validate_task_id(self, task_id: int) -> None:
        """
        Validates if a task ID exists and is valid.
        
        Args:
            task_id: The ID to validate
            
        Raises:
            ValueError: If ID is invalid
            KeyError: If task doesn't exist
        """
        if not isinstance(task_id, int) or task_id < 1:
            raise ValueError("Task ID must be a positive integer")
        if task_id not in self._tasks:
            raise KeyError(f"Task with ID {task_id} does not exist")

    def add(self, task_name: str, task_description: str) -> int:
        """
        Adds a new task to the task manager.
        
        Args:
            task_name: Name of the task
            task_description: Description of the task
            
        Returns:
            int: ID of the newly created task
            
        Raises:
            ValueError: If inputs are invalid
        """
        # Validate inputs
        task_name = self._validate_string_input(task_name, "Task name")
        task_description = self._validate_string_input(task_description, "Task description")
        
        # Create new task
        task_id = self._next_id
        self._tasks[task_id] = {
            'id': task_id,
            'name': task_name,
            'description': task_description,
            'is_finished': False,
            'created_at': datetime.now()
        }
        self._next_id += 1
        
        return task_id

    def remove(self, task_id: int) -> bool:
        """
        Removes a task by its ID.
        
        Args:
            task_id: ID of the task to remove
            
        Returns:
            bool: True if task was removed successfully
            
        Raises:
            ValueError: If task ID is invalid
            KeyError: If task doesn't exist
        """
        self._validate_task_id(task_id)
        del self._tasks[task_id]
        return True

    def search(self, task_term: str) -> List[Dict]:
        """
        Searches tasks by name or description.
        
        Args:
            task_term: Search term to match against tasks
            
        Returns:
            List of matching tasks
            
        Raises:
            ValueError: If search term is invalid
        """
        search_term = self._validate_string_input(task_term, "Search term")
        pattern = re.compile(search_term, re.IGNORECASE)
        
        return [
            self._format_task(task) for task in self._tasks.values()
            if pattern.search(task['name']) or pattern.search(task['description'])
        ]

    def finish(self, task_id: int) -> bool:
        """
        Marks a task as completed.
        
        Args:
            task_id: ID of the task to mark as completed
            
        Returns:
            bool: True if task was marked as completed successfully
            
        Raises:
            ValueError: If task ID is invalid
            KeyError: If task doesn't exist
        """
        self._validate_task_id(task_id)
        self._tasks[task_id]['is_finished'] = True
        return True

    def get_all(self) -> List[Dict]:
        """
        Retrieves all tasks.
        
        Returns:
            List of all tasks
        """
        return [self._format_task(task) for task in self._tasks.values()]

    def clear_all(self) -> bool:
        """
        Removes all tasks.
        
        Returns:
            bool: True if all tasks were removed successfully
        """
        self._tasks.clear()
        return True

    def _format_task(self, task: Dict) -> Dict:
        """
        Formats a task for output.
        
        Args:
            task: Task dictionary to format
            
        Returns:
            Formatted task dictionary
        """
        return {
            'id': task['id'],
            'task_name': task['name'],
            'task_description': task['description'],
            'is_finished': task['is_finished']
        }



# Example usage
task_manager = TaskManager()

# Add tasks
task1_id = task_manager.add("Complete report", "Finish quarterly report")
task2_id = task_manager.add("Email client", "Send project updates")

# Mark task as complete
task_manager.finish(task1_id)

# Search tasks
results = task_manager.search("report")

# Get all tasks
all_tasks = task_manager.get_all()

# Remove a task
task_manager.remove(task2_id)

# Clear all tasks
task_manager.clear_all()
