class TaskManager:
    """
    A class that manages a collection of tasks in a to-do list application.
    
    This class provides functionality to add, remove, search, complete,
    and manage tasks efficiently.
    """

    def __init__(self):
        """Initialize an empty task manager with a counter for unique task IDs."""
        self.tasks = {}  # Dictionary to store tasks with ID as key
        self.next_id = 1  # Counter for generating unique task IDs

    def add(self, task_name: str, task_description: str) -> int:
        """
        Add a new task to the task manager.
        
        Args:
            task_name (str): The name of the task.
            task_description (str): The description of the task.
            
        Returns:
            int: The unique ID of the newly added task.
            
        Raises:
            ValueError: If task_name or task_description is empty.
        """
        # Validate inputs
        if not task_name or not isinstance(task_name, str):
            raise ValueError("Task name cannot be empty and must be a string")
        if not task_description or not isinstance(task_description, str):
            raise ValueError("Task description cannot be empty and must be a string")
            
        # Create new task
        task_id = self.next_id
        self.tasks[task_id] = {
            "id": task_id,
            "task_name": task_name,
            "task_description": task_description,
            "is_finished": False
        }
        self.next_id += 1
        
        return task_id

    def remove(self, task_id: int) -> bool:
        """
        Remove a task by its ID.
        
        Args:
            task_id (int): The unique ID of the task to remove.
            
        Returns:
            bool: True if the task was successfully removed, False otherwise.
            
        Raises:
            ValueError: If task_id is not a positive integer.
        """
        # Validate task_id
        if not isinstance(task_id, int) or task_id <= 0:
            raise ValueError("Task ID must be a positive integer")
            
        # Remove the task if it exists
        if task_id in self.tasks:
            del self.tasks[task_id]
            return True
        return False

    def search(self, task_term: str) -> list[dict]:
        """
        Search for tasks containing the specified term in name or description.
        
        Args:
            task_term (str): The term to search for in task names and descriptions.
            
        Returns:
            list[dict]: A list of tasks that match the search criteria.
            
        Raises:
            ValueError: If task_term is empty or not a string.
        """
        # Validate input
        if not task_term or not isinstance(task_term, str):
            raise ValueError("Search term cannot be empty and must be a string")
            
        # Search for tasks
        search_term = task_term.lower()  # Case-insensitive search
        results = []
        
        for task in self.tasks.values():
            if (search_term in task["task_name"].lower() or 
                search_term in task["task_description"].lower()):
                results.append(task.copy())  # Return a copy to prevent external modification
                
        return results

    def finish(self, task_id: int) -> bool:
        """
        Mark a task as completed.
        
        Args:
            task_id (int): The unique ID of the task to mark as completed.
            
        Returns:
            bool: True if the task was successfully marked as completed, False otherwise.
            
        Raises:
            ValueError: If task_id is not a positive integer.
        """
        # Validate task_id
        if not isinstance(task_id, int) or task_id <= 0:
            raise ValueError("Task ID must be a positive integer")
            
        # Mark the task as completed if it exists
        if task_id in self.tasks:
            # Only update if not already finished
            if not self.tasks[task_id]["is_finished"]:
                self.tasks[task_id]["is_finished"] = True
                return True
            return False  # Task was already finished
        return False  # Task does not exist

    def get_all(self) -> list[dict]:
        """
        Get all tasks.
        
        Returns:
            list[dict]: A list containing all tasks.
        """
        # Return copies of tasks to prevent external modification
        return [task.copy() for task in self.tasks.values()]

    def clear_all(self) -> bool:
        """
        Remove all tasks.
        
        Returns:
            bool: True if all tasks were successfully removed.
        """
        self.tasks.clear()
        return True

    def get_task_by_id(self, task_id: int) -> dict:
        """
        Get a specific task by its ID.
        
        Args:
            task_id (int): The unique ID of the task to retrieve.
            
        Returns:
            dict: The task information if found.
            
        Raises:
            ValueError: If task_id is not a positive integer.
            KeyError: If the task with the specified ID does not exist.
        """
        # Validate task_id
        if not isinstance(task_id, int) or task_id <= 0:
            raise ValueError("Task ID must be a positive integer")
            
        # Get the task if it exists
        if task_id in self.tasks:
            return self.tasks[task_id].copy()  # Return a copy to prevent external modification
        raise KeyError(f"Task with ID {task_id} not found")
