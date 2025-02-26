"""
Todo List Application

This module implements a console-based todo list application that allows users to 
manage tasks through various operations like adding, removing, searching, and completing tasks.

The implementation follows ISO/IEC 25010 quality standards focusing on:
- Functional suitability
- Performance efficiency
- Compatibility
- Usability
- Reliability
- Security
- Maintainability
- Portability
"""

from typing import List, Dict, Optional, Union, Tuple
import time


class TaskManager:
    """
    Manages todo tasks with operations for adding, removing, searching, and completing tasks.
    
    This class provides a complete interface for task management with efficient data structures
    and comprehensive error handling.
    """

    def __init__(self):
        """Initialize TaskManager with empty task storage and counter for unique IDs."""
        self._tasks = {}  # Dictionary for O(1) access by ID
        self._next_id = 1  # Counter for generating unique IDs

    def add(self, task_name: str, task_description: str) -> int:
        """
        Add a new task to the todo list.
        
        Args:
            task_name (str): The name/title of the task.
            task_description (str): A description of the task.
            
        Returns:
            int: The unique ID assigned to the new task.
            
        Raises:
            ValueError: If task_name or task_description is empty or invalid.
        """
        # Validate inputs
        if not task_name or not isinstance(task_name, str):
            raise ValueError("Task name cannot be empty and must be a string.")
        if not task_description or not isinstance(task_description, str):
            raise ValueError("Task description cannot be empty and must be a string.")
            
        # Create new task
        task_id = self._next_id
        self._tasks[task_id] = {
            'id': task_id,
            'name': task_name.strip(),
            'description': task_description.strip(),
            'is_finished': False,
            'created_at': time.time()
        }
        
        self._next_id += 1
        return task_id

    def remove(self, task_id: int) -> bool:
        """
        Remove a task by its ID.
        
        Args:
            task_id (int): The unique identifier of the task to remove.
            
        Returns:
            bool: True if the task was successfully removed, False if the task was not found.
            
        Raises:
            ValueError: If task_id is not a positive integer.
        """
        if not isinstance(task_id, int) or task_id <= 0:
            raise ValueError("Task ID must be a positive integer.")
            
        if task_id in self._tasks:
            del self._tasks[task_id]
            return True
        
        return False

    def search(self, search_term: str) -> List[Dict]:
        """
        Search for tasks containing the search term in their name or description.
        
        Args:
            search_term (str): The term to search for in task names and descriptions.
            
        Returns:
            List[Dict]: A list of tasks that match the search criteria, each as a dictionary.
            
        Raises:
            ValueError: If search_term is empty or not a string.
        """
        if not search_term or not isinstance(search_term, str):
            raise ValueError("Search term cannot be empty and must be a string.")
            
        search_term = search_term.lower().strip()
        result = []
        
        for task in self._tasks.values():
            if (search_term in task['name'].lower() or 
                search_term in task['description'].lower()):
                result.append(self._format_task_output(task))
                
        return result

    def finish(self, task_id: int) -> bool:
        """
        Mark a task as completed.
        
        Args:
            task_id (int): The unique identifier of the task to mark as completed.
            
        Returns:
            bool: True if the task was successfully marked as completed,
                  False if the task was not found or already completed.
                  
        Raises:
            ValueError: If task_id is not a positive integer.
        """
        if not isinstance(task_id, int) or task_id <= 0:
            raise ValueError("Task ID must be a positive integer.")
            
        if task_id in self._tasks and not self._tasks[task_id]['is_finished']:
            self._tasks[task_id]['is_finished'] = True
            return True
            
        return False

    def get_all(self) -> List[Dict]:
        """
        Retrieve all tasks.
        
        Returns:
            List[Dict]: A list of all tasks in the system, each as a dictionary.
        """
        return [self._format_task_output(task) for task in self._tasks.values()]

    def clear_all(self) -> bool:
        """
        Delete all tasks from the system.
        
        Returns:
            bool: True if the operation was successful (always returns True).
        """
        self._tasks.clear()
        return True
        
    def _format_task_output(self, task: Dict) -> Dict:
        """
        Format a task for output according to the required format.
        
        Args:
            task (Dict): The internal task representation.
            
        Returns:
            Dict: A formatted task dictionary with only the required fields.
        """
        return {
            'id': task['id'],
            'task_name': task['name'],
            'task_description': task['description'],
            'is_finished': task['is_finished']
        }


def main():
    """
    Run the Todo List application with a simple command-line interface.
    
    This function demonstrates the usage of the TaskManager class with 
    a basic command-line interaction loop.
    """
    task_manager = TaskManager()
    
    print("=== Todo List Application ===")
    
    while True:
        print("\nOperations:")
        print("1. Add a new task")
        print("2. Remove a task")
        print("3. Search tasks")
        print("4. Mark task as finished")
        print("5. View all tasks")
        print("6. Clear all tasks")
        print("0. Exit")
        
        choice = input("\nSelect operation (0-6): ")
        
        try:
            if choice == '1':
                name = input("Enter task name: ")
                description = input("Enter task description: ")
                task_id = task_manager.add(name, description)
                print(f"Task added with ID: {task_id}")
                
            elif choice == '2':
                task_id = int(input("Enter task ID to remove: "))
                if task_manager.remove(task_id):
                    print("Task removed successfully.")
                else:
                    print("Task not found.")
                    
            elif choice == '3':
                term = input("Enter search term: ")
                results = task_manager.search(term)
                if results:
                    print(f"Found {len(results)} tasks:")
                    for task in results:
                        status = "Completed" if task['is_finished'] else "Pending"
                        print(f"ID: {task['id']} - {task['task_name']} ({status})")
                        print(f"  Description: {task['task_description']}")
                else:
                    print("No tasks found matching your search.")
                    
            elif choice == '4':
                task_id = int(input("Enter task ID to mark as finished: "))
                if task_manager.finish(task_id):
                    print("Task marked as finished.")
                else:
                    print("Task not found or already completed.")
                    
            elif choice == '5':
                tasks = task_manager.get_all()
                if tasks:
                    print(f"All tasks ({len(tasks)}):")
                    for task in tasks:
                        status = "Completed" if task['is_finished'] else "Pending"
                        print(f"ID: {task['id']} - {task['task_name']} ({status})")
                        print(f"  Description: {task['task_description']}")
                else:
                    print("No tasks in the list.")
                    
            elif choice == '6':
                confirm = input("Are you sure you want to clear all tasks? (yes/no): ")
                if confirm.lower() == 'yes':
                    task_manager.clear_all()
                    print("All tasks have been cleared.")
                else:
                    print("Operation canceled.")
                    
            elif choice == '0':
                print("Exiting application. Goodbye!")
                break
                
            else:
                print("Invalid choice. Please try again.")
                
        except ValueError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"Unexpected error: {e}")


if __name__ == "__main__":
    main()
