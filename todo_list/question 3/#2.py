"""
Todo List Application

This module provides a task management system following ISO/IEC 25010 standards
with functionality to add, remove, search, finish, retrieve, and clear tasks.
"""

from typing import List, Dict, Union, Optional
import time


class TaskManager:
    """
    A class that manages todo tasks with various operations.
    
    Attributes:
        _tasks (dict): Internal storage for tasks using ID as key
        _next_id (int): Counter for assigning unique IDs to tasks
    """

    def __init__(self):
        """Initialize an empty task manager with a counter for task IDs."""
        self._tasks = {}  # Using dict for O(1) lookups by ID
        self._next_id = 1  # Start IDs at 1 for better user experience

    def add(self, task_name: str, task_description: str) -> int:
        """
        Add a new task to the manager.
        
        Args:
            task_name: The name/title of the task
            task_description: A detailed description of the task
            
        Returns:
            int: The unique ID assigned to the new task
            
        Raises:
            ValueError: If task_name or task_description is empty
        """
        # Validate inputs
        if not task_name or not isinstance(task_name, str):
            raise ValueError("Task name cannot be empty and must be a string")
        
        if not task_description or not isinstance(task_description, str):
            raise ValueError("Task description cannot be empty and must be a string")
            
        # Create task with unique ID
        task_id = self._next_id
        self._tasks[task_id] = {
            'id': task_id,
            'name': task_name,
            'description': task_description,
            'is_finished': False,
            'created_at': time.time()  # Store creation timestamp
        }
        
        self._next_id += 1
        return task_id

    def remove(self, task_id: int) -> bool:
        """
        Remove a task by its ID.
        
        Args:
            task_id: The unique identifier of the task to remove
            
        Returns:
            bool: True if the task was successfully removed, False otherwise
            
        Raises:
            ValueError: If task_id is not a positive integer
        """
        # Validate input
        if not isinstance(task_id, int) or task_id <= 0:
            raise ValueError("Task ID must be a positive integer")
            
        # Remove task if it exists
        if task_id in self._tasks:
            del self._tasks[task_id]
            return True
        return False

    def search(self, task_term: str) -> List[Dict]:
        """
        Search tasks by name or description matching the search term.
        
        Args:
            task_term: The search term to look for in task names and descriptions
            
        Returns:
            list: A list of dictionaries containing matching tasks
            
        Raises:
            ValueError: If task_term is empty or not a string
        """
        # Validate input
        if not task_term or not isinstance(task_term, str):
            raise ValueError("Search term cannot be empty and must be a string")
            
        result = []
        term_lower = task_term.lower()  # Case-insensitive search
        
        for task in self._tasks.values():
            if (term_lower in task['name'].lower() or 
                term_lower in task['description'].lower()):
                result.append(self._format_task(task))
                
        return result

    def finish(self, task_id: int) -> bool:
        """
        Mark a task as completed.
        
        Args:
            task_id: The unique identifier of the task to mark as completed
            
        Returns:
            bool: True if the task was successfully marked as completed, False otherwise
            
        Raises:
            ValueError: If task_id is not a positive integer
        """
        # Validate input
        if not isinstance(task_id, int) or task_id <= 0:
            raise ValueError("Task ID must be a positive integer")
            
        # Mark task as finished if it exists
        if task_id in self._tasks:
            # Only update if not already finished (idempotent operation)
            if not self._tasks[task_id]['is_finished']:
                self._tasks[task_id]['is_finished'] = True
                self._tasks[task_id]['completed_at'] = time.time()  # Record completion time
            return True
        return False

    def get_all(self) -> List[Dict]:
        """
        Retrieve all tasks.
        
        Returns:
            list: A list of dictionaries containing all tasks
        """
        return [self._format_task(task) for task in self._tasks.values()]

    def clear_all(self) -> bool:
        """
        Remove all tasks from the manager.
        
        Returns:
            bool: True if the operation was successful
        """
        self._tasks.clear()
        return True
        
    def _format_task(self, task: Dict) -> Dict:
        """
        Format a task for external use conforming to the specified format.
        
        Args:
            task: The internal task dictionary
            
        Returns:
            dict: A dictionary with the specified format: (id, name, description, is_finished)
        """
        return {
            'id': task['id'],
            'task_name': task['name'],
            'task_description': task['description'],
            'is_finished': task['is_finished']
        }


def run_todo_app():
    """
    Run the interactive console-based Todo List Application.
    This function provides a user interface for the TaskManager.
    """
    manager = TaskManager()
    
    # Menu options
    menu = """
TodoList Application
-------------------
1. Add a task
2. Remove a task
3. Search tasks
4. Mark task as finished
5. View all tasks
6. Clear all tasks
7. Exit
    """
    
    while True:
        print(menu)
        try:
            choice = int(input("Enter your choice (1-7): ").strip())
            
            if choice == 1:
                # Add task
                task_name = input("Enter task name: ").strip()
                task_description = input("Enter task description: ").strip()
                try:
                    task_id = manager.add(task_name, task_description)
                    print(f"Task added with ID: {task_id}")
                except ValueError as e:
                    print(f"Error: {e}")
                    
            elif choice == 2:
                # Remove task
                try:
                    task_id = int(input("Enter task ID to remove: ").strip())
                    if manager.remove(task_id):
                        print(f"Task {task_id} removed successfully")
                    else:
                        print(f"Task {task_id} not found")
                except ValueError as e:
                    print("Error: Please enter a valid task ID (positive integer)")
                    
            elif choice == 3:
                # Search tasks
                search_term = input("Enter search term: ").strip()
                try:
                    tasks = manager.search(search_term)
                    if tasks:
                        print(f"Found {len(tasks)} matching tasks:")
                        for task in tasks:
                            status = "✓ Completed" if task['is_finished'] else "⬜ Pending"
                            print(f"ID: {task['id']} | {task['task_name']} | {status}")
                            print(f"  Description: {task['task_description']}")
                            print("-" * 40)
                    else:
                        print("No tasks found matching your criteria")
                except ValueError as e:
                    print(f"Error: {e}")
                    
            elif choice == 4:
                # Mark task as finished
                try:
                    task_id = int(input("Enter task ID to mark as finished: ").strip())
                    if manager.finish(task_id):
                        print(f"Task {task_id} marked as finished")
                    else:
                        print(f"Task {task_id} not found")
                except ValueError:
                    print("Error: Please enter a valid task ID (positive integer)")
                    
            elif choice == 5:
                # View all tasks
                tasks = manager.get_all()
                if tasks:
                    print(f"Total tasks: {len(tasks)}")
                    print("-" * 40)
                    for task in tasks:
                        status = "✓ Completed" if task['is_finished'] else "⬜ Pending"
                        print(f"ID: {task['id']} | {task['task_name']} | {status}")
                        print(f"  Description: {task['task_description']}")
                        print("-" * 40)
                else:
                    print("No tasks found")
                    
            elif choice == 6:
                # Clear all tasks
                confirm = input("Are you sure you want to clear all tasks? (y/n): ").strip().lower()
                if confirm == 'y':
                    manager.clear_all()
                    print("All tasks have been cleared")
                else:
                    print("Operation cancelled")
                    
            elif choice == 7:
                # Exit
                print("Exiting the application. Goodbye!")
                break
                
            else:
                print("Invalid choice. Please enter a number between 1 and 7")
                
        except ValueError:
            print("Please enter a valid option (1-7)")
            
        # Wait for user to continue
        input("\nPress Enter to continue...")


if __name__ == "__main__":
    run_todo_app()
