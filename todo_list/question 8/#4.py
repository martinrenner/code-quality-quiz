"""
Todo List Application

A console-based Todo List manager that allows users to add, remove, search, 
and manage tasks according to ISO/IEC 25010 quality standards.
"""

from typing import List, Dict, Union, Optional, Any
import time
import re


class TaskManager:
    """
    Manages a collection of tasks with operations for adding, removing,
    searching, and modifying task status.
    
    Attributes:
        tasks (dict): Dictionary storing tasks with their IDs as keys
        next_id (int): Counter for assigning unique IDs to new tasks
    """
    
    def __init__(self) -> None:
        """Initialize an empty task manager with a task counter."""
        self.tasks: Dict[int, Dict[str, Any]] = {}
        self.next_id: int = 1
    
    def add(self, task_name: str, task_description: str) -> int:
        """
        Add a new task to the task manager.
        
        Args:
            task_name (str): The name of the task
            task_description (str): Detailed description of the task
            
        Returns:
            int: The unique ID of the newly created task
            
        Raises:
            ValueError: If task_name or task_description is empty or invalid
        """
        # Validate inputs
        if not task_name or not isinstance(task_name, str):
            raise ValueError("Task name cannot be empty and must be a string")
        if not task_description or not isinstance(task_description, str):
            raise ValueError("Task description cannot be empty and must be a string")
        
        # Sanitize inputs
        task_name = task_name.strip()
        task_description = task_description.strip()
        
        if not task_name:
            raise ValueError("Task name cannot be empty after trimming whitespace")
        
        # Create task with unique ID
        task_id = self.next_id
        self.tasks[task_id] = {
            'id': task_id,
            'task_name': task_name,
            'task_description': task_description,
            'is_finished': False,
            'created_at': time.time()
        }
        self.next_id += 1
        
        return task_id
    
    def remove(self, task_id: int) -> bool:
        """
        Remove a task by its ID.
        
        Args:
            task_id (int): The unique identifier of the task to remove
            
        Returns:
            bool: True if the task was successfully removed, False otherwise
            
        Raises:
            ValueError: If task_id is not a positive integer
        """
        if not isinstance(task_id, int) or task_id <= 0:
            raise ValueError("Task ID must be a positive integer")
        
        if task_id in self.tasks:
            del self.tasks[task_id]
            return True
        return False
    
    def search(self, task_term: str) -> List[Dict[str, Any]]:
        """
        Search for tasks by name or description.
        
        Args:
            task_term (str): The search term to look for in task names or descriptions
            
        Returns:
            list: List of dictionaries containing matching tasks
            
        Raises:
            ValueError: If task_term is empty or not a string
        """
        if not isinstance(task_term, str):
            raise ValueError("Search term must be a string")
        
        task_term = task_term.strip().lower()
        if not task_term:
            return []
        
        # Use regex for more flexible search
        try:
            pattern = re.compile(f".*{re.escape(task_term)}.*", re.IGNORECASE)
            results = []
            
            for task in self.tasks.values():
                if (pattern.search(task['task_name']) or 
                    pattern.search(task['task_description'])):
                    results.append(self._format_task(task))
            
            return results
        except re.error:
            # Handle regex compilation errors
            return self._simple_search(task_term)
    
    def _simple_search(self, term: str) -> List[Dict[str, Any]]:
        """
        Perform a simple substring search when regex fails.
        
        Args:
            term (str): Search term
            
        Returns:
            list: Matching tasks
        """
        term = term.lower()
        results = []
        
        for task in self.tasks.values():
            if (term in task['task_name'].lower() or 
                term in task['task_description'].lower()):
                results.append(self._format_task(task))
        
        return results
    
    def finish(self, task_id: int) -> bool:
        """
        Mark a task as completed.
        
        Args:
            task_id (int): The unique identifier of the task to mark as completed
            
        Returns:
            bool: True if the task was successfully marked as completed, False otherwise
            
        Raises:
            ValueError: If task_id is not a positive integer
        """
        if not isinstance(task_id, int) or task_id <= 0:
            raise ValueError("Task ID must be a positive integer")
        
        if task_id in self.tasks:
            # Only update if not already finished
            if not self.tasks[task_id]['is_finished']:
                self.tasks[task_id]['is_finished'] = True
                self.tasks[task_id]['completed_at'] = time.time()
                return True
            return False  # Task was already finished
        return False  # Task not found
    
    def get_all(self) -> List[Dict[str, Any]]:
        """
        Get all tasks in the system.
        
        Returns:
            list: List of dictionaries containing all tasks
        """
        return [self._format_task(task) for task in self.tasks.values()]
    
    def clear_all(self) -> bool:
        """
        Remove all tasks from the system.
        
        Returns:
            bool: True if the operation was successful
        """
        self.tasks.clear()
        return True
    
    def _format_task(self, task: Dict[str, Any]) -> Dict[str, Any]:
        """
        Format a task for output to ensure consistent structure.
        
        Args:
            task (dict): The internal task representation
            
        Returns:
            dict: A dictionary with standardized keys
        """
        return {
            'id': task['id'],
            'task_name': task['task_name'],
            'task_description': task['task_description'],
            'is_finished': task['is_finished']
        }


def demo_usage():
    """Demonstrate the usage of the TaskManager class."""
    task_manager = TaskManager()
    
    # Adding tasks
    task1_id = task_manager.add("Complete project", "Finish the Todo List app implementation")
    task2_id = task_manager.add("Write documentation", "Document the code and API")
    
    print("All tasks after adding:")
    for task in task_manager.get_all():
        print(task)
    
    # Marking a task as finished
    task_manager.finish(task1_id)
    
    print("\nAll tasks after marking one as finished:")
    for task in task_manager.get_all():
        print(task)
    
    # Searching for tasks
    print("\nSearch results for 'code':")
    for task in task_manager.search("code"):
        print(task)
    
    # Removing a task
    task_manager.remove(task2_id)
    
    print("\nAll tasks after removing one:")
    for task in task_manager.get_all():
        print(task)
    
    # Clearing all tasks
    task_manager.clear_all()
    
    print("\nAll tasks after clearing all:")
    print(task_manager.get_all())


if __name__ == "__main__":
    demo_usage()
