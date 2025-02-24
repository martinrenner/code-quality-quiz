from typing import List, Dict, Union

class TaskManager:
    def __init__(self):
        """
        Initializes a TaskManager with an empty list of tasks stored in memory.
        """
        self.tasks = []
        self.next_id = 1  # Unique identifier for each task starting from 1

    def _validate_id(self, task_id: int) -> None:
        """
        Validates that the provided task ID is valid and exists in the list.

        Args:
            task_id (int): The ID of the task to validate.

        Raises:
            ValueError: If the ID is invalid or does not exist.
        """
        if not isinstance(task_id, int) or task_id < 1:
            raise ValueError("Invalid task ID. ID must be a positive integer.")
        if task_id >= self.next_id or self.tasks[task_id - 1] is None:
            raise ValueError("Task with the given ID does not exist.")

    def _validate_strings(self, *args: str) -> None:
        """
        Validates that the input strings are not empty.

        Args:
            *args: Variable number of strings to validate.

        Raises:
            ValueError: If any of the strings are empty.
        """
        for arg in args:
            if not arg.strip():
                raise ValueError("String input cannot be empty.")

    def add(self, task_name: str, task_description: str) -> int:
        """
        Adds a new task to the list and returns its unique ID.

        Args:
            task_name (str): The name of the task.
            task_description (str): A detailed description of the task.

        Returns:
            int: The unique ID of the newly added task.

        Raises:
            ValueError: If task_name or task_description is empty.
        """
        self._validate_strings(task_name, task_description)
        task_id = self.next_id
        self.tasks.append({
            "id": task_id,
            "task_name": task_name.strip(),
            "task_description": task_description.strip(),
            "is_finished": False
        })
        self.next_id += 1
        return task_id

    def remove(self, task_id: int) -> bool:
        """
        Removes a task by its ID and returns the success status.

        Args:
            task_id (int): The ID of the task to remove.

        Returns:
            bool: True if the task was successfully removed, False otherwise.

        Raises:
            ValueError: If the task_id is invalid or does not exist.
        """
        self._validate_id(task_id)
        self.tasks[task_id - 1] = None
        return True

    def search(self, task_term: str) -> List[Dict[str, Union[int, str, bool]]]:
        """
        Searches tasks by name or description and returns matching results.

        Args:
            task_term (str): A term to search within the task name and description.

        Returns:
            List[Dict[str, Union[int, str, bool]]]: A list of tasks that match the search term.

        Raises:
            ValueError: If the task_term is empty.
        """
        self._validate_strings(task_term)
        task_term = task_term.lower()
        results = []
        for task in self.tasks:
            if task is None:
                continue
            if task_term in task["task_name"].lower() or task_term in task["task_description"].lower():
                results.append({
                    "id": task["id"],
                    "task_name": task["task_name"],
                    "task_description": task["task_description"],
                    "is_finished": task["is_finished"]
                })
        return results

    def finish(self, task_id: int) -> bool:
        """
        Marks a task as completed and returns the success status.

        Args:
            task_id (int): The ID of the task to mark as completed.

        Returns:
            bool: True if the task was successfully marked as completed, False otherwise.

        Raises:
            ValueError: If the task_id is invalid or does not exist.
        """
        self._validate_id(task_id)
        self.tasks[task_id - 1]["is_finished"] = True
        return True

    def get_all(self) -> List[Dict[str, Union[int, str, bool]]]:
        """
        Retrieves all tasks with their details.

        Returns:
            List[Dict[str, Union[int, str, bool]]]: A list containing all tasks and their information.
        """
        return [task for task in self.tasks if task is not None]

    def clear_all(self) -> bool:
        """
        Deletes all tasks and returns the success status.

        Returns:
            bool: True if all tasks were successfully cleared, False otherwise.
        """
        self.tasks = []
        self.next_id = 1
        return True
