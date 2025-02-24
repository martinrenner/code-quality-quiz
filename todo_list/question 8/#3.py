from typing import List, Dict, Optional
from datetime import datetime
import re

class TaskError(Exception):
    """Base exception class for task-related errors"""
    pass

class TaskNotFoundError(TaskError):
    """Exception raised when a task is not found"""
    pass

class InvalidInputError(TaskError):
    """Exception raised when input validation fails"""
    pass

class TaskManager:
    """
    A class to manage todo tasks with CRUD operations.
    
    Attributes:
        tasks (dict): Dictionary storing tasks with task ID as key
        current_id (int): Counter for generating unique task IDs
    """
    
    def __init__(self):
        """Initialize TaskManager with empty task storage"""
        self.tasks: Dict[int, Dict] = {}
        self.current_id: int = 1

    def _validate_string_input(self, input_str: str, field_name: str) -> None:
        """
        Validate string input for task fields.
        
        Args:
            input_str: String to validate
            field_name: Name of the field being validated
            
        Raises:
            InvalidInputError: If validation fails
        """
        if not isinstance(input_str, str):
            raise InvalidInputError(f"{field_name} must be a string")
        if not input_str.strip():
            raise InvalidInputError(f"{field_name} cannot be empty")
        if len(input_str) > 200:  # Reasonable limit for text fields
            raise InvalidInputError(f"{field_name} is too long (max 200 characters)")

    def add(self, task_name: str, task_description: str) -> int:
        """
        Add a new task to the todo list.
        
        Args:
            task_name: Name of the task
            task_description: Detailed description of the task
            
        Returns:
            int: Unique ID of the created task
            
        Raises:
            InvalidInputError: If input validation fails
        """
        # Validate inputs
        self._validate_string_input(task_name, "Task name")
        self._validate_string_input(task_description, "Task description")
        
        # Create task
        task_id = self.current_id
        self.tasks[task_id] = {
            'id': task_id,
            'name': task_name.strip(),
            'description': task_description.strip(),
            'is_finished': False,
            'created_at': datetime.now()
        }
        self.current_id += 1
        return task_id

    def remove(self, task_id: int) -> bool:
        """
        Remove a task by its ID.
        
        Args:
            task_id: Unique identifier of the task
            
        Returns:
            bool: True if task was removed, False otherwise
            
        Raises:
            InvalidInputError: If task_id is invalid
        """
        if not isinstance(task_id, int) or task_id < 1:
            raise InvalidInputError("Task ID must be a positive integer")
            
        return bool(self.tasks.pop(task_id, None))

    def search(self, task_term: str) -> List[Dict]:
        """
        Search tasks by name or description.
        
        Args:
            task_term: Search term to match against task name or description
            
        Returns:
            List[Dict]: List of matching tasks
            
        Raises:
            InvalidInputError: If search term is invalid
        """
        self._validate_string_input(task_term, "Search term")
        
        search_pattern = re.compile(task_term.strip(), re.IGNORECASE)
        return [
            task for task in self.tasks.values()
            if search_pattern.search(task['name']) or 
               search_pattern.search(task['description'])
        ]

    def finish(self, task_id: int) -> bool:
        """
        Mark a task as completed.
        
        Args:
            task_id: Unique identifier of the task
            
        Returns:
            bool: True if task was marked as completed, False if task not found
            
        Raises:
            InvalidInputError: If task_id is invalid
        """
        if not isinstance(task_id, int) or task_id < 1:
            raise InvalidInputError("Task ID must be a positive integer")
            
        if task_id in self.tasks:
            self.tasks[task_id]['is_finished'] = True
            return True
        return False

    def get_all(self) -> List[Dict]:
        """
        Get all tasks in the todo list.
        
        Returns:
            List[Dict]: List of all tasks
        """
        return list(self.tasks.values())

    def clear_all(self) -> bool:
        """
        Remove all tasks from the todo list.
        
        Returns:
            bool: True if operation was successful
        """
        self.tasks.clear()
        return True

    def get_task(self, task_id: int) -> Optional[Dict]:
        """
        Get a specific task by ID.
        
        Args:
            task_id: Unique identifier of the task
            
        Returns:
            Optional[Dict]: Task dictionary if found, None otherwise
            
        Raises:
            InvalidInputError: If task_id is invalid
        """
        if not isinstance(task_id, int) or task_id < 1:
            raise InvalidInputError("Task ID must be a positive integer")
            
        return self.tasks.get(task_id)


# Create task manager
tm = TaskManager()

# Add tasks
task1_id = tm.add("Complete report", "Finish quarterly report")
task2_id = tm.add("Email client", "Send project updates")

# Search tasks
results = tm.search("report")

# Mark task as complete
tm.finish(task1_id)

# Get all tasks
all_tasks = tm.get_all()

# Remove a task
tm.remove(task2_id)

# Clear all tasks
tm.clear_all()
