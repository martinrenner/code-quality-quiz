#!/usr/bin/env python3
"""
Todo List Application

A console-based task management system that allows users to create,
manage and track their tasks with functionality aligned with ISO/IEC 25010
quality standards.

Author: Assistant
"""
import re
from datetime import datetime
from typing import List, Dict, Union, Optional, Any


class TaskManager:
    """
    TaskManager class for managing a todo list with full CRUD operations.
    
    This class provides methods for adding, removing, searching, completing,
    and managing tasks in an in-memory data structure.
    """
    
    def __init__(self):
        """Initialize the TaskManager with an empty task dictionary and counter."""
        self._tasks: Dict[int, Dict[str, Any]] = {}
        self._id_counter: int = 1
    
    def add(self, task_name: str, task_description: str) -> int:
        """
        Add a new task to the todo list.
        
        Args:
            task_name (str): The name/title of the task
            task_description (str): Detailed description of the task
            
        Returns:
            int: The unique ID of the newly created task
            
        Raises:
            ValueError: If the task name or description is empty
        """
        # Input validation
        if not task_name or not isinstance(task_name, str):
            raise ValueError("Task name cannot be empty and must be a string")
        if not task_description or not isinstance(task_description, str):
            raise ValueError("Task description cannot be empty and must be a string")
        
        task_name = task_name.strip()
        task_description = task_description.strip()
        
        # Additional validation after stripping
        if not task_name:
            raise ValueError("Task name cannot be empty or just whitespace")
        if not task_description:
            raise ValueError("Task description cannot be empty or just whitespace")
        
        # Create a new task with a unique ID
        task_id = self._id_counter
        self._tasks[task_id] = {
            "id": task_id,
            "task_name": task_name,
            "task_description": task_description,
            "is_finished": False,
            "created_at": datetime.now(),
            "updated_at": datetime.now()
        }
        self._id_counter += 1
        
        return task_id
    
    def remove(self, task_id: int) -> bool:
        """
        Remove a task from the todo list by its ID.
        
        Args:
            task_id (int): The unique ID of the task to remove
            
        Returns:
            bool: True if the task was successfully removed, False otherwise
            
        Raises:
            ValueError: If task_id is not a positive integer
        """
        if not isinstance(task_id, int) or task_id <= 0:
            raise ValueError("Task ID must be a positive integer")
        
        if task_id in self._tasks:
            del self._tasks[task_id]
            return True
        return False
    
    def search(self, task_term: str) -> List[Dict[str, Any]]:
        """
        Search tasks by name or description.
        
        Args:
            task_term (str): The search term to look for in task names and descriptions
            
        Returns:
            list[dict]: A list of task dictionaries that match the search term
            
        Raises:
            ValueError: If search term is not a string or is empty
        """
        if not isinstance(task_term, str):
            raise ValueError("Search term must be a string")
        
        task_term = task_term.strip().lower()
        
        if not task_term:
            return []
        
        # Using regular expressions for more flexible search
        try:
            pattern = re.compile(task_term, re.IGNORECASE)
            results = []
            
            for task in self._tasks.values():
                if (pattern.search(task["task_name"]) or 
                    pattern.search(task["task_description"])):
                    results.append(self._format_task_output(task))
            
            return results
        except re.error:
            # Handle invalid regex patterns
            # Fall back to simple substring search
            results = []
            for task in self._tasks.values():
                if (task_term in task["task_name"].lower() or 
                    task_term in task["task_description"].lower()):
                    results.append(self._format_task_output(task))
            return results
    
    def finish(self, task_id: int) -> bool:
        """
        Mark a task as completed by its ID.
        
        Args:
            task_id (int): The unique ID of the task to mark as completed
            
        Returns:
            bool: True if the task was successfully marked as completed, False otherwise
            
        Raises:
            ValueError: If task_id is not a positive integer
        """
        if not isinstance(task_id, int) or task_id <= 0:
            raise ValueError("Task ID must be a positive integer")
        
        if task_id in self._tasks:
            task = self._tasks[task_id]
            # Only update if not already finished
            if not task["is_finished"]:
                task["is_finished"] = True
                task["updated_at"] = datetime.now()
            return True
        return False
    
    def get_all(self) -> List[Dict[str, Any]]:
        """
        Retrieve all tasks in the todo list.
        
        Returns:
            list[dict]: A list of all tasks with their details
        """
        return [self._format_task_output(task) for task in self._tasks.values()]
    
    def clear_all(self) -> bool:
        """
        Remove all tasks from the todo list.
        
        Returns:
            bool: True if all tasks were successfully removed
        """
        self._tasks.clear()
        # Reset ID counter only when clearing all tasks
        self._id_counter = 1
        return True
    
    def get_task(self, task_id: int) -> Optional[Dict[str, Any]]:
        """
        Get a specific task by its ID.
        
        Args:
            task_id (int): The unique ID of the task to retrieve
            
        Returns:
            Optional[Dict[str, Any]]: The task dictionary if found, None otherwise
            
        Raises:
            ValueError: If task_id is not a positive integer
        """
        if not isinstance(task_id, int) or task_id <= 0:
            raise ValueError("Task ID must be a positive integer")
        
        if task_id in self._tasks:
            return self._format_task_output(self._tasks[task_id])
        return None
    
    def _format_task_output(self, task: Dict[str, Any]) -> Dict[str, Any]:
        """
        Format a task for output according to the specified format.
        
        Args:
            task (dict): The internal task dictionary
            
        Returns:
            dict: The formatted task dictionary with only the required fields
        """
        return {
            "id": task["id"],
            "task_name": task["task_name"],
            "task_description": task["task_description"],
            "is_finished": task["is_finished"]
        }


def print_task(task: Dict[str, Any]) -> None:
    """
    Helper function to print a task in a user-friendly format.
    
    Args:
        task (dict): The task dictionary to print
    """
    status = "✓" if task["is_finished"] else "□"
    print(f"[{status}] Task #{task['id']}: {task['task_name']}")
    print(f"    Description: {task['task_description']}")
    print()


def main() -> None:
    """
    Main function to demonstrate TaskManager functionality.
    """
    # Create a new TaskManager instance
    manager = TaskManager()
    
    # Add sample tasks
    task1_id = manager.add("Complete project", "Finish the Python project by Friday")
    task2_id = manager.add("Buy groceries", "Milk, eggs, bread, and vegetables")
    task3_id = manager.add("Call mom", "Remember to call mom on her birthday")
    
    # Display all tasks
    print("All Tasks:")
    for task in manager.get_all():
        print_task(task)
    
    # Mark a task as completed
    print("Marking 'Buy groceries' as completed...")
    manager.finish(task2_id)
    
    # Search for tasks
    print("Searching for 'project':")
    search_results = manager.search("project")
    for task in search_results:
        print_task(task)
    
    # Remove a task
    print("Removing 'Call mom'...")
    manager.remove(task3_id)
    
    # Display all tasks again
    print("Updated Task List:")
    for task in manager.get_all():
        print_task(task)
    
    # Clear all tasks
    print("Clearing all tasks...")
    manager.clear_all()
    print(f"Tasks remaining: {len(manager.get_all())}")


if __name__ == "__main__":
    main()
