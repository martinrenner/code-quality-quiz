from typing import List, Dict, Optional
from datetime import datetime
import re

class TaskManager:
    """
    A class to manage todo list tasks with CRUD operations.
    
    Attributes:
        _tasks (dict): Internal storage for tasks
        _next_id (int): Counter for generating unique task IDs
    """
    
    def __init__(self):
        """Initialize the TaskManager with empty task storage."""
        self._tasks: Dict[int, Dict] = {}
        self._next_id: int = 1

    def _validate_string_input(self, text: str, field_name: str) -> None:
        """
        Validates string input for task fields.

        Args:
            text (str): The input text to validate
            field_name (str): Name of the field being validated

        Raises:
            ValueError: If the input is empty or contains only whitespace
        """
        if not text or text.isspace():
            raise ValueError(f"{field_name} cannot be empty or whitespace")

    def _validate_task_id(self, task_id: int) -> None:
        """
        Validates task ID existence and format.

        Args:
            task_id (int): The task ID to validate

        Raises:
            ValueError: If the task ID is invalid
            KeyError: If the task ID doesn't exist
        """
        if not isinstance(task_id, int) or task_id < 1:
            raise ValueError("Task ID must be a positive integer")
        if task_id not in self._tasks:
            raise KeyError(f"Task with ID {task_id} does not exist")

    def add(self, task_name: str, task_description: str) -> int:
        """
        Adds a new task to the todo list.

        Args:
            task_name (str): Name of the task
            task_description (str): Description of the task

        Returns:
            int: Unique ID of the created task

        Raises:
            ValueError: If task_name or task_description is invalid
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
        Removes a task from the todo list.

        Args:
            task_id (int): ID of the task to remove

        Returns:
            bool: True if task was removed successfully

        Raises:
            ValueError: If task_id is invalid
            KeyError: If task_id doesn't exist
        """
        self._validate_task_id(task_id)
        del self._tasks[task_id]
        return True

    def search(self, task_term: str) -> List[Dict]:
        """
        Searches for tasks matching the search term in name or description.

        Args:
            task_term (str): Search term to match against tasks

        Returns:
            List[Dict]: List of matching tasks

        Raises:
            ValueError: If search term is invalid
        """
        self._validate_string_input(task_term, "Search term")
        
        pattern = re.compile(task_term.strip(), re.IGNORECASE)
        matching_tasks = []

        for task in self._tasks.values():
            if (pattern.search(task['name']) or 
                pattern.search(task['description'])):
                matching_tasks.append(self._format_task_output(task))

        return matching_tasks

    def finish(self, task_id: int) -> bool:
        """
        Marks a task as completed.

        Args:
            task_id (int): ID of the task to mark as completed

        Returns:
            bool: True if task was marked as completed successfully

        Raises:
            ValueError: If task_id is invalid
            KeyError: If task_id doesn't exist
        """
        self._validate_task_id(task_id)
        self._tasks[task_id]['is_finished'] = True
        return True

    def get_all(self) -> List[Dict]:
        """
        Retrieves all tasks in the todo list.

        Returns:
            List[Dict]: List of all tasks
        """
        return [self._format_task_output(task) for task in self._tasks.values()]

    def clear_all(self) -> bool:
        """
        Removes all tasks from the todo list.

        Returns:
            bool: True if all tasks were cleared successfully
        """
        self._tasks.clear()
        return True

    def _format_task_output(self, task: Dict) -> Dict:
        """
        Formats a task for output according to specified format.

        Args:
            task (Dict): Task to format

        Returns:
            Dict: Formatted task dictionary
        """
        return {
            'id': task['id'],
            'task_name': task['name'],
            'task_description': task['description'],
            'is_finished': task['is_finished']
        }


# Usage example
todo = TaskManager()

# Add tasks
task1_id = todo.add("Complete project", "Finish the Python project by Friday")
task2_id = todo.add("Buy groceries", "Get milk, bread, and eggs")

# Mark task as complete
todo.finish(task1_id)

# Search for tasks
results = todo.search("project")

# Get all tasks
all_tasks = todo.get_all()

# Remove a task
todo.remove(task2_id)

# Clear all tasks
todo.clear_all()
