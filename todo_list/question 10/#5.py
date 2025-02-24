from typing import List, Dict, Union

class TaskManager:
    """
    A class to manage a to-do list with tasks.

    This class provides methods to add, remove, search, finish, and retrieve tasks.
    It uses an in-memory data structure for storage and ensures efficient operations.
    """

    def __init__(self):
        """
        Initialize the TaskManager with an empty task list and a counter for task IDs.
        """
        self._tasks: Dict[int, Dict[str, Union[str, bool]]] = {}
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
        if not task_name.strip() or not task_description.strip():
            raise ValueError("Task name and description cannot be empty.")

        task_id = self._next_id
        self._tasks[task_id] = {
            "name": task_name.strip(),
            "description": task_description.strip(),
            "is_finished": False
        }
        self._next_id += 1

        return task_id

    def remove(self, task_id: int) -> bool:
        """
        Remove a task from the to-do list by its ID.

        Args:
            task_id (int): The ID of the task to be removed.

        Returns:
            bool: True if the task was successfully removed, False otherwise.
        """
        if task_id < 1 or task_id not in self._tasks:
            return False

        del self._tasks[task_id]
        return True

    def search(self, task_term: str) -> List[Dict[str, Union[int, str, bool]]]:
        """
        Search for tasks by name or description.

        Args:
            task_term (str): The term to search for in task names and descriptions.

        Returns:
            List[Dict[str, Union[int, str, bool]]]: A list of tasks matching the search term.
        """
        if not task_term.strip():
            return []

        task_term = task_term.lower()
        results = []

        for task_id, task in self._tasks.items():
            if task_term in task["name"].lower() or task_term in task["description"].lower():
                results.append({
                    "id": task_id,
                    "task_name": task["name"],
                    "task_description": task["description"],
                    "is_finished": task["is_finished"]
                })

        return results

    def finish(self, task_id: int) -> bool:
        """
        Mark a task as completed.

        Args:
            task_id (int): The ID of the task to be marked as completed.

        Returns:
            bool: True if the task was successfully marked as completed, False otherwise.
        """
        if task_id < 1 or task_id not in self._tasks:
            return False

        self._tasks[task_id]["is_finished"] = True
        return True

    def get_all(self) -> List[Dict[str, Union[int, str, bool]]]:
        """
        Retrieve all tasks from the to-do list.

        Returns:
            List[Dict[str, Union[int, str, bool]]]: A list of all tasks.
        """
        return [
            {
                "id": task_id,
                "task_name": task["name"],
                "task_description": task["description"],
                "is_finished": task["is_finished"]
            }
            for task_id, task in self._tasks.items()
        ]

    def clear_all(self) -> bool:
        """
        Clear all tasks from the to-do list.

        Returns:
            bool: True if all tasks were successfully cleared, False otherwise.
        """
        self._tasks.clear()
        self._next_id = 1
        return True
