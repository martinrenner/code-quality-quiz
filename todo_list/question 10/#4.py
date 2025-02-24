class TaskManager:
    """
    A class to manage a todo list of tasks.

    This class implements a complete set of operations for managing tasks,
    including adding, removing, searching, completing, and retrieving tasks.
    """

    def __init__(self):
        """
        Initialize the TaskManager with an empty task list.
        """
        self._tasks = {}
        self._next_id = 1

    def add(self, task_name: str, task_description: str) -> int:
        """
        Add a new task to the task list.

        Args:
            task_name (str): The name of the task.
            task_description (str): A description of the task.

        Returns:
            int: The unique ID of the newly added task.

        Raises:
            ValueError: If the task name or description is empty.
        """
        if not task_name.strip() or not task_description.strip():
            raise ValueError("Task name and description cannot be empty.")

        task_id = self._next_id
        self._tasks[task_id] = {
            "id": task_id,
            "task_name": task_name.strip(),
            "task_description": task_description.strip(),
            "is_finished": False
        }
        self._next_id += 1
        return task_id

    def remove(self, task_id: int) -> bool:
        """
        Remove a task from the task list.

        Args:
            task_id (int): The ID of the task to remove.

        Returns:
            bool: True if the task was successfully removed, False otherwise.
        """
        if task_id < 1 or task_id not in self._tasks:
            return False
        del self._tasks[task_id]
        return True

    def search(self, task_term: str) -> list[dict]:
        """
        Search for tasks by name or description.

        Args:
            task_term (str): The search term to look for in task names and descriptions.

        Returns:
            list[dict]: A list of matching tasks, each represented as a dictionary.
        """
        if not task_term.strip():
            return []

        results = []
        for task in self._tasks.values():
            if task_term.lower() in task["task_name"].lower() or task_term.lower() in task["task_description"].lower():
                results.append({
                    "id": task["id"],
                    "task_name": task["task_name"],
                    "task_description": task["task_description"],
                    "is_finished": task["is_finished"]
                })
        return results

    def finish(self, task_id: int) -> bool:
        """
        Mark a task as completed.

        Args:
            task_id (int): The ID of the task to mark as completed.

        Returns:
            bool: True if the task was successfully marked as completed, False otherwise.
        """
        if task_id < 1 or task_id not in self._tasks:
            return False
        self._tasks[task_id]["is_finished"] = True
        return True

    def get_all(self) -> list[dict]:
        """
        Retrieve all tasks from the task list.

        Returns:
            list[dict]: A list of all tasks, each represented as a dictionary.
        """
        return [task for task in self._tasks.values()]

    def clear_all(self) -> bool:
        """
        Clear all tasks from the task list.

        Returns:
            bool: True if all tasks were successfully cleared, False otherwise.
        """
        self._tasks.clear()
        self._next_id = 1
        return True
