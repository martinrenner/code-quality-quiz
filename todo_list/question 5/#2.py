from typing import List, Dict, Optional
from dataclasses import dataclass
from datetime import datetime
import re

@dataclass
class Task:
    """Represents a single task in the todo list."""
    id: int
    name: str
    description: str
    is_finished: bool = False
    created_at: datetime = datetime.now()

class TaskManager:
    """Manages operations for the todo list application."""
    
    def __init__(self):
        """Initialize the TaskManager with an empty task list and ID counter."""
        self._tasks: Dict[int, Task] = {}
        self._current_id: int = 1

    def _validate_string_input(self, value: str, field_name: str) -> None:
        """Validate string inputs for task fields.
        
        Args:
            value: The string to validate
            field_name: Name of the field being validated
            
        Raises:
            ValueError: If validation fails
        """
        if not isinstance(value, str):
            raise ValueError(f"{field_name} must be a string")
        if not value.strip():
            raise ValueError(f"{field_name} cannot be empty")
        if len(value) > 100:  # Reasonable limit for task fields
            raise ValueError(f"{field_name} cannot exceed 100 characters")

    def _validate_task_id(self, task_id: int) -> None:
        """Validate task ID.
        
        Args:
            task_id: The ID to validate
            
        Raises:
            ValueError: If validation fails
        """
        if not isinstance(task_id, int):
            raise ValueError("Task ID must be an integer")
        if task_id <= 0:
            raise ValueError("Task ID must be positive")
        if task_id not in self._tasks:
            raise ValueError("Task ID does not exist")

    def add(self, task_name: str, task_description: str) -> int:
        """Add a new task to the list.
        
        Args:
            task_name: Name of the task
            task_description: Description of the task
            
        Returns:
            int: ID of the newly created task
            
        Raises:
            ValueError: If input validation fails
        """
        self._validate_string_input(task_name, "Task name")
        self._validate_string_input(task_description, "Task description")

        new_task = Task(
            id=self._current_id,
            name=task_name,
            description=task_description
        )
        
        self._tasks[self._current_id] = new_task
        self._current_id += 1
        return new_task.id

    def remove(self, task_id: int) -> bool:
        """Remove a task by its ID.
        
        Args:
            task_id: ID of the task to remove
            
        Returns:
            bool: True if task was removed successfully
            
        Raises:
            ValueError: If task ID is invalid
        """
        self._validate_task_id(task_id)
        del self._tasks[task_id]
        return True

    def search(self, task_term: str) -> List[Dict]:
        """Search tasks by name or description.
        
        Args:
            task_term: Search term to match against tasks
            
        Returns:
            List[Dict]: List of matching tasks
        """
        self._validate_string_input(task_term, "Search term")
        
        results = []
        pattern = re.compile(task_term, re.IGNORECASE)
        
        for task in self._tasks.values():
            if pattern.search(task.name) or pattern.search(task.description):
                results.append(self._task_to_dict(task))
        
        return results

    def finish(self, task_id: int) -> bool:
        """Mark a task as completed.
        
        Args:
            task_id: ID of the task to mark as completed
            
        Returns:
            bool: True if task was marked as completed successfully
            
        Raises:
            ValueError: If task ID is invalid
        """
        self._validate_task_id(task_id)
        self._tasks[task_id].is_finished = True
        return True

    def get_all(self) -> List[Dict]:
        """Get all tasks.
        
        Returns:
            List[Dict]: List of all tasks
        """
        return [self._task_to_dict(task) for task in self._tasks.values()]

    def clear_all(self) -> bool:
        """Remove all tasks.
        
        Returns:
            bool: True if all tasks were removed successfully
        """
        self._tasks.clear()
        return True

    def _task_to_dict(self, task: Task) -> Dict:
        """Convert a Task object to dictionary format.
        
        Args:
            task: Task object to convert
            
        Returns:
            Dict: Dictionary representation of the task
        """
        return {
            'id': task.id,
            'task_name': task.name,
            'task_description': task.description,
            'is_finished': task.is_finished
        }


# Example usage
task_manager = TaskManager()

# Add tasks
task_id = task_manager.add("Complete project", "Finish the Python project by Friday")
task_manager.add("Buy groceries", "Get milk, bread, and eggs")

# Mark task as complete
task_manager.finish(task_id)

# Search tasks
results = task_manager.search("project")

# Get all tasks
all_tasks = task_manager.get_all()
