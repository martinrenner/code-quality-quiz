
from typing import List, Dict, Optional

class TaskManager:
    """
    A class to manage a todo list with various operations.
    
    This class implements functionality to add, remove, search, finish, 
    get, and clear tasks in a todo list.
    """

    def __init__(self):
        """
        Initialize the TaskManager with an empty todo list.
        """
        self.tasks: List[Dict[str, any]] = []
        self.task_id_counter: int = 1

    def add(self, task_name: str, task_description: str) -> int:
        """
        Add a new task to the todo list.

        :param task_name: The name of the task.
        :param task_description: A description of the task.
        :return: The unique ID assigned to the new task.
        :raises ValueError: If task_name or task_description is empty.
        """
        if not task_name.strip() or not task_description.strip():
            raise ValueError("Task name and description cannot be empty.")

        task = {
            "id": self.task_id_counter,
            "name": task_name.strip(),
            "description": task_description.strip(),
            "is_finished": False
        }
        self.tasks.append(task)
        self.task_id_counter += 1
        return task["id"]

    def remove(self, task_id: int) -> bool:
        """
        Remove a task from the todo list by its ID.

        :param task_id: The ID of the task to remove.
        :return: True if the task was successfully removed, False otherwise.
        """
        for task in self.tasks:
            if task["id"] == task_id:
                self.tasks.remove(task)
                return True
        return False

    def search(self, task_term: str) -> List[Dict[str, any]]:
        """
        Search for tasks by name or description.

        :param task_term: The search term to look for in task names and descriptions.
        :return: A list of tasks that match the search term.
        """
        task_term = task_term.lower().strip()
        if not task_term:
            return []

        results = []
        for task in self.tasks:
            if task_term in task["name"].lower() or task_term in task["description"].lower():
                results.append(self._format_task(task))
        return results

    def finish(self, task_id: int) -> bool:
        """
        Mark a task as completed.

        :param task_id: The ID of the task to mark as completed.
        :return: True if the task was successfully marked as completed, False otherwise.
        """
        for task in self.tasks:
            if task["id"] == task_id:
                task["is_finished"] = True
                return True
        return False

    def get_all(self) -> List[Dict[str, any]]:
        """
        Retrieve all tasks from the todo list.

        :return: A list of all tasks in the todo list.
        """
        return [self._format_task(task) for task in self.tasks]

    def clear_all(self) -> bool:
        """
        Remove all tasks from the todo list.

        :return: True if all tasks were successfully removed, False otherwise.
        """
        self.tasks.clear()
        return True

    def _format_task(self, task: Dict[str, any]) -> Dict[str, any]:
        """
        Format a task dictionary for output.

        :param task: The task dictionary to format.
        :return: A formatted task dictionary.
        """
        return {
            "id": task["id"],
            "name": task["name"],
            "description": task["description"],
            "is_finished": task["is_finished"]
        }
