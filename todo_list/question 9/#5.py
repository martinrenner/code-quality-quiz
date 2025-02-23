
from typing import List, Dict, Optional

class TaskManager:
    """
    A class to manage tasks in a to-do list application.

    This class provides methods to add, remove, search, finish, get all tasks,
    and clear all tasks. It uses in-memory storage for efficiency and
    implements validation and error handling for robustness.
    """

    def __init__(self):
        """
        Initialize the TaskManager with an empty list of tasks.
        """
        self._tasks: List[Dict[str, any]] = []
        self._next_id: int = 1

    def add(self, task_name: str, task_description: str) -> int:
        """
        Add a new task to the to-do list.

        Args:
            task_name (str): The name of the task.
            task_description (str): A description of the task.

        Returns:
            int: The unique ID of the newly added task.

        Raises:
            ValueError: If task_name or task_description is empty.
        """
        if not task_name or not task_description:
            raise ValueError("Task name and description cannot be empty.")

        task_id = self._next_id
        self._tasks.append({
            "id": task_id,
            "name": task_name,
            "description": task_description,
            "is_finished": False
        })
        self._next_id += 1
        return task_id

    def remove(self, task_id: int) -> bool:
        """
        Remove a task from the to-do list by its ID.

        Args:
            task_id (int): The ID of the task to remove.

        Returns:
            bool: True if the task was successfully removed, False otherwise.
        """
        if task_id < 1:
            return False

        for index, task in enumerate(self._tasks):
            if task["id"] == task_id:
                del self._tasks[index]
                return True
        return False

    def search(self, task_term: str) -> List[Dict[str, any]]:
        """
        Search for tasks by name or description.

        Args:
            task_term (str): The term to search for in task names and descriptions.

        Returns:
            List[Dict[str, any]]: A list of tasks matching the search term.
        """
        if not task_term:
            return []

        return [
            task for task in self._tasks
            if task_term.lower() in task["name"].lower() or task_term.lower() in task["description"].lower()
        ]

    def finish(self, task_id: int) -> bool:
        """
        Mark a task as completed.

        Args:
            task_id (int): The ID of the task to mark as completed.

        Returns:
            bool: True if the task was successfully marked as completed, False otherwise.
        """
        if task_id < 1:
            return False

        for task in self._tasks:
            if task["id"] == task_id:
                task["is_finished"] = True
                return True
        return False

    def get_all(self) -> List[Dict[str, any]]:
        """
        Retrieve all tasks.

        Returns:
            List[Dict[str, any]]: A list of all tasks.
        """
        return self._tasks.copy()

    def clear_all(self) -> bool:
        """
        Clear all tasks from the to-do list.

        Returns:
            bool: True if all tasks were successfully cleared, False otherwise.
        """
        self._tasks.clear()
        self._next_id = 1
        return True


# Example usage
if __name__ == "__main__":
    manager = TaskManager()

    # Add tasks
    task1_id = manager.add("Buy groceries", "Milk, eggs, bread")
    task2_id = manager.add("Finish report", "Complete the project report")

    # Get all tasks
    print("All tasks:")
    for task in manager.get_all():
        print(f"{task['id']}: {task['name']} - {task['description']} (Completed: {task['is_finished']})")

    # Search for tasks
    search_results = manager.search("report")
    print("\nSearch results for 'report':")
    for task in search_results:
        print(f"{task['id']}: {task['name']} - {task['description']} (Completed: {task['is_finished']})")

    # Finish a task
    manager.finish(task1_id)

    # Remove a task
    removed = manager.remove(task2_id)
    print(f"\nTask {task2_id} removed: {removed}")

    # Clear all tasks
    cleared = manager.clear_all()
    print(f"\nAll tasks cleared: {cleared}")

    # Check if all tasks are cleared
    print("Tasks after clearing:")
    for task in manager.get_all():
        print(task)
