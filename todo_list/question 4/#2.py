from typing import List, Dict, Optional
from datetime import datetime
import re

class TaskManager:
    """
    A class to manage todo tasks with basic CRUD operations.
    
    Attributes:
        tasks (dict): Dictionary storing tasks with their IDs as keys
        current_id (int): Counter for generating unique task IDs
    """
    
    def __init__(self):
        """Initialize an empty task manager."""
        self.tasks: Dict[int, Dict] = {}
        self.current_id: int = 1

    def validate_input(self, text: str, field_name: str) -> str:
        """
        Validates input text for task fields.

        Args:
            text (str): The input text to validate
            field_name (str): Name of the field being validated

        Returns:
            str: Validated and sanitized text

        Raises:
            ValueError: If input is empty or contains only whitespace
        """
        if not text or not text.strip():
            raise ValueError(f"{field_name} cannot be empty")
        return text.strip()

    def add(self, task_name: str, task_description: str) -> int:
        """
        Adds a new task to the manager.

        Args:
            task_name (str): Name of the task
            task_description (str): Description of the task

        Returns:
            int: Unique ID of the created task

        Raises:
            ValueError: If task_name or task_description is invalid
        """
        try:
            validated_name = self.validate_input(task_name, "Task name")
            validated_desc = self.validate_input(task_description, "Task description")
            
            task = {
                'id': self.current_id,
                'task_name': validated_name,
                'task_description': validated_desc,
                'is_finished': False,
                'created_at': datetime.now()
            }
            
            self.tasks[self.current_id] = task
            self.current_id += 1
            return task['id']
            
        except ValueError as e:
            raise ValueError(f"Failed to add task: {str(e)}")

    def remove(self, task_id: int) -> bool:
        """
        Removes a task by its ID.

        Args:
            task_id (int): ID of the task to remove

        Returns:
            bool: True if task was removed, False if task wasn't found

        Raises:
            ValueError: If task_id is invalid
        """
        if not isinstance(task_id, int) or task_id < 1:
            raise ValueError("Invalid task ID")
            
        return self.tasks.pop(task_id, None) is not None

    def search(self, task_term: str) -> List[Dict]:
        """
        Searches tasks by name or description.

        Args:
            task_term (str): Search term to match against tasks

        Returns:
            List[Dict]: List of matching tasks

        Raises:
            ValueError: If search term is invalid
        """
        try:
            term = self.validate_input(task_term, "Search term")
            pattern = re.compile(term, re.IGNORECASE)
            
            return [
                task for task in self.tasks.values()
                if pattern.search(task['task_name']) or 
                pattern.search(task['task_description'])
            ]
            
        except ValueError as e:
            raise ValueError(f"Invalid search term: {str(e)}")

    def finish(self, task_id: int) -> bool:
        """
        Marks a task as completed.

        Args:
            task_id (int): ID of the task to mark as completed

        Returns:
            bool: True if task was marked as completed, False if task wasn't found

        Raises:
            ValueError: If task_id is invalid
        """
        if not isinstance(task_id, int) or task_id < 1:
            raise ValueError("Invalid task ID")
            
        if task_id in self.tasks:
            self.tasks[task_id]['is_finished'] = True
            return True
        return False

    def get_all(self) -> List[Dict]:
        """
        Retrieves all tasks.

        Returns:
            List[Dict]: List of all tasks
        """
        return list(self.tasks.values())

    def clear_all(self) -> bool:
        """
        Removes all tasks from the manager.

        Returns:
            bool: True if operation was successful
        """
        self.tasks.clear()
        return True

    def get_task_by_id(self, task_id: int) -> Optional[Dict]:
        """
        Retrieves a specific task by ID.

        Args:
            task_id (int): ID of the task to retrieve

        Returns:
            Optional[Dict]: Task dictionary if found, None otherwise

        Raises:
            ValueError: If task_id is invalid
        """
        if not isinstance(task_id, int) or task_id < 1:
            raise ValueError("Invalid task ID")
            
        return self.tasks.get(task_id)


def main():
    try:
        # Create task manager instance
        manager = TaskManager()
        
        # Add tasks
        task1_id = manager.add("Complete report", "Finish quarterly report")
        task2_id = manager.add("Email client", "Send project updates")
        
        # Search tasks
        results = manager.search("report")
        print("Search results:", results)
        
        # Mark task as complete
        manager.finish(task1_id)
        
        # Get all tasks
        all_tasks = manager.get_all()
        print("All tasks:", all_tasks)
        
        # Remove a task
        manager.remove(task2_id)
        
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")

if __name__ == "__main__":
    main()
