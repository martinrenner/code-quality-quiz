from typing import List, Dict, Optional

class TaskManager:
    """
    A class that manages a todo list, implementing functionalities to add, remove, search, 
    finish, retrieve, and clear all tasks in accordance with ISO/IEC 25010 standards.
    Tasks are stored in-memory for simplicity and efficiency.
    """

    def __init__(self):
        """Initialize the TaskManager with an empty list of tasks."""
        self.tasks: List[Dict[str, any]] = []
        self.next_id: int = 1

    def add(self, task_name: str, task_description: str) -> int:
        """
        Add a new task to the todo list.

        Args:
            task_name (str): The name of the task.
            task_description (str): The description of the task.

        Returns:
            int: The unique ID of the newly added task.

        Raises:
            ValueError: If task_name or task_description is empty.
        """
        if not task_name or not task_description:
            raise ValueError("Both task name and description must be non-empty.")
        
        task = {
            "id": self.next_id,
            "task_name": task_name,
            "task_description": task_description,
            "is_finished": False
        }
        self.tasks.append(task)
        self.next_id += 1
        return task["id"]

    def remove(self, task_id: int) -> bool:
        """
        Remove a task from the todo list by its ID.

        Args:
            task_id (int): The ID of the task to be removed.

        Returns:
            bool: True if a task was removed, False otherwise.

        Raises:
            ValueError: If task_id is non-positive.
        """
        if task_id <= 0:
            raise ValueError("Task ID must be a positive integer.")
        
        for task in self.tasks:
            if task["id"] == task_id:
                self.tasks.remove(task)
                return True
        return False

    def search(self, task_term: str) -> List[Dict[str, any]]:
        """
        Search for tasks in the todo list by name or description.

        Args:
            task_term (str): The term to search within task names or descriptions.

        Returns:
            List[Dict[str, any]]: A list of tasks that match the search term.

        Raises:
            ValueError: If task_term is empty.
        """
        if not task_term:
            raise ValueError("Search term cannot be empty.")

        results = []
        for task in self.tasks:
            if task_term.lower() in task["task_name"].lower() or task_term.lower() in task["task_description"].lower():
                results.append(task)
        return results

    def finish(self, task_id: int) -> bool:
        """
        Mark a task as completed in the todo list.

        Args:
            task_id (int): The ID of the task to be marked as completed.

        Returns:
            bool: True if a task was marked as completed, False otherwise.

        Raises:
            ValueError: If task_id is non-positive.
        """
        if task_id <= 0:
            raise ValueError("Task ID must be a positive integer.")
        
        for task in self.tasks:
            if task["id"] == task_id:
                task["is_finished"] = True
                return True
        return False

    def get_all(self) -> List[Dict[str, any]]:
        """
        Retrieve all tasks from the todo list.

        Returns:
            List[Dict[str, any]]: A list containing all tasks in the todo list.
        """
        return self.tasks.copy()

    def clear_all(self) -> bool:
        """
        Clear all tasks from the todo list.

        Returns:
            bool: True if all tasks were successfully cleared, False otherwise.
        """
        self.tasks.clear()
        return True


# Example usage of TaskManager:
# manager = TaskManager()
# new_task_id = manager.add("Buy groceries", "Need to buy bread and vegetables")
# print(manager.get_all())
# manager.finish(new_task_id)
# print(manager.get_all())
# manager.remove(new_task_id)
# print(manager.get_all())
# search_results = manager.search("bread")
# print(search_results)
# manager.clear_all()
# print(manager.get_all())
