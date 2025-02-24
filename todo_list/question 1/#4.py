from typing import List, Dict, Union

class TaskManager:
    def __init__(self):
        self.tasks: Dict[int, Dict[str, Union[str, bool]]] = {}
        self.last_id: int = 0

    def add(self, task_name: str, task_description: str) -> int:
        """
        Adds a new task to the task list.

        Args:
            task_name (str): The name of the task.
            task_description (str): The description of the task.

        Returns:
            int: The unique ID of the newly added task.

        Raises:
            ValueError: If task_name or task_description are empty.
        """
        if not task_name.strip() or not task_description.strip():
            raise ValueError("Task name and description cannot be empty.")

        self.last_id += 1
        self.tasks[self.last_id] = {
            "name": task_name.strip(),
            "description": task_description.strip(),
            "is_finished": False
        }
        return self.last_id

    def remove(self, task_id: int) -> bool:
        """
        Removes a task from the task list by its ID.

        Args:
            task_id (int): The ID of the task to be removed.

        Returns:
            bool: True if the task was successfully removed, False otherwise.
        """
        if task_id <= 0:
            return False

        if task_id in self.tasks:
            del self.tasks[task_id]
            return True
        return False

    def search(self, task_term: str) -> List[Dict[str, Union[int, str, bool]]]:
        """
        Searches for tasks that match the provided term in either the name or description.

        Args:
            task_term (str): The search term.

        Returns:
            List[Dict[str, Union[int, str, bool]]]: A list of matching tasks.
        """
        if not task_term.strip():
            return []

        task_term = task_term.lower()
        result = []
        for task_id, task in self.tasks.items():
            if task_term in task["name"].lower() or task_term in task["description"].lower():
                result.append({
                    "id": task_id,
                    "name": task["name"],
                    "description": task["description"],
                    "is_finished": task["is_finished"]
                })
        return result

    def finish(self, task_id: int) -> bool:
        """
        Marks a task as completed.

        Args:
            task_id (int): The ID of the task to be marked as completed.

        Returns:
            bool: True if the task was successfully marked as completed, False otherwise.
        """
        if task_id <= 0:
            return False

        if task_id in self.tasks:
            self.tasks[task_id]["is_finished"] = True
            return True
        return False

    def get_all(self) -> List[Dict[str, Union[int, str, bool]]]:
        """
        Retrieves all tasks with their details.

        Returns:
            List[Dict[str, Union[int, str, bool]]]: A list of all tasks.
        """
        return [
            {
                "id": task_id,
                "name": task["name"],
                "description": task["description"],
                "is_finished": task["is_finished"]
            }
            for task_id, task in self.tasks.items()
        ]

    def clear_all(self) -> bool:
        """
        Clears all tasks from the task list.

        Returns:
            bool: True if all tasks were successfully cleared, False otherwise.
        """
        self.tasks.clear()
        self.last_id = 0
        return True
