"""
Task Manager Module - A console-based to-do list application.

This module provides functionality to manage tasks with features including adding,
removing, searching, and completing tasks with an in-memory storage solution.
"""
from typing import List, Dict, Optional, Union
import datetime


class TaskManager:
    """
    TaskManager class handles operations for a to-do list application.
    
    This class provides methods to add, remove, search, and manage tasks
    with validation and error handling throughout.
    """
    
    def __init__(self):
        """Initialize the TaskManager with an empty task collection and ID counter."""
        self._tasks: Dict[int, Dict] = {}
        self._next_id: int = 1
    
    def add(self, task_name: str, task_description: str) -> int:
        """
        Add a new task to the task manager.
        
        Args:
            task_name (str): The name of the task.
            task_description (str): The description of the task.
            
        Returns:
            int: The unique ID assigned to the new task.
            
        Raises:
            ValueError: If task_name or task_description is empty.
        """
        # Validate inputs
        if not task_name or not task_name.strip():
            raise ValueError("Task name cannot be empty")
        if not task_description or not task_description.strip():
            raise ValueError("Task description cannot be empty")
        
        # Create task with unique ID
        task_id = self._next_id
        self._next_id += 1
        
        # Store the task with creation timestamp
        self._tasks[task_id] = {
            'id': task_id,
            'task_name': task_name.strip(),
            'task_description': task_description.strip(),
            'is_finished': False,
            'created_at': datetime.datetime.now()
        }
        
        return task_id
    
    def remove(self, task_id: int) -> bool:
        """
        Remove a task by its ID.
        
        Args:
            task_id (int): The unique ID of the task to remove.
            
        Returns:
            bool: True if the task was successfully removed, False otherwise.
            
        Raises:
            ValueError: If task_id is negative.
        """
        # Validate task_id
        if task_id <= 0:
            raise ValueError("Task ID must be a positive integer")
        
        # Check if task exists
        if task_id not in self._tasks:
            return False
        
        # Remove the task
        del self._tasks[task_id]
        return True
    
    def search(self, task_term: str) -> List[Dict]:
        """
        Search for tasks by name or description.
        
        Args:
            task_term (str): The search term to look for in task names and descriptions.
            
        Returns:
            List[Dict]: A list of tasks matching the search term.
            
        Raises:
            ValueError: If task_term is empty.
        """
        # Validate search term
        if not task_term or not task_term.strip():
            raise ValueError("Search term cannot be empty")
        
        task_term = task_term.lower().strip()
        results = []
        
        # Search for matching tasks
        for task in self._tasks.values():
            if (task_term in task['task_name'].lower() or 
                task_term in task['task_description'].lower()):
                results.append(self._format_task(task))
        
        return results
    
    def finish(self, task_id: int) -> bool:
        """
        Mark a task as completed.
        
        Args:
            task_id (int): The unique ID of the task to mark as completed.
            
        Returns:
            bool: True if the task was successfully marked as completed, False otherwise.
            
        Raises:
            ValueError: If task_id is negative.
        """
        # Validate task_id
        if task_id <= 0:
            raise ValueError("Task ID must be a positive integer")
        
        # Check if task exists
        if task_id not in self._tasks:
            return False
        
        # Mark task as completed
        self._tasks[task_id]['is_finished'] = True
        return True
    
    def get_all(self) -> List[Dict]:
        """
        Retrieve all tasks.
        
        Returns:
            List[Dict]: A list of all tasks.
        """
        return [self._format_task(task) for task in self._tasks.values()]
    
    def clear_all(self) -> bool:
        """
        Delete all tasks.
        
        Returns:
            bool: True if all tasks were successfully cleared.
        """
        self._tasks.clear()
        return True
    
    def _format_task(self, task: Dict) -> Dict:
        """
        Format a task to the standard output format.
        
        Args:
            task (Dict): The task to format.
            
        Returns:
            Dict: The formatted task with required fields.
        """
        return {
            'id': task['id'],
            'task_name': task['task_name'],
            'task_description': task['task_description'],
            'is_finished': task['is_finished']
        }


def main():
    """Example usage of the TaskManager class."""
    task_manager = TaskManager()
    
    # Add some tasks
    task1_id = task_manager.add("Complete project", "Finish the Python to-do list project")
    task2_id = task_manager.add("Buy groceries", "Milk, eggs, bread, and vegetables")
    task3_id = task_manager.add("Schedule meeting", "Team meeting for project updates")
    
    print("All tasks:")
    for task in task_manager.get_all():
        print(f"ID: {task['id']}, Name: {task['task_name']}, "
              f"Finished: {task['is_finished']}")
    
    # Mark a task as finished
    task_manager.finish(task1_id)
    
    # Search for tasks
    print("\nSearch results for 'project':")
    for task in task_manager.search("project"):
        print(f"ID: {task['id']}, Name: {task['task_name']}, "
              f"Description: {task['task_description']}, Finished: {task['is_finished']}")
    
    # Remove a task
    task_manager.remove(task2_id)
    
    print("\nRemaining tasks:")
    for task in task_manager.get_all():
        print(f"ID: {task['id']}, Name: {task['task_name']}, "
              f"Finished: {task['is_finished']}")
    
    # Clear all tasks
    task_manager.clear_all()
    print("\nTasks after clearing:", task_manager.get_all())


if __name__ == "__main__":
    main()
