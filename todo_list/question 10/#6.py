class TaskManager:
    """
    A class that manages a to-do list application with various operations on tasks.

    The class supports adding, removing, searching, completing tasks, and displaying
    the entire list of tasks. It utilizes a dictionary for efficient storage and access.

    Attributes:
        _tasks (dict): A dictionary that stores tasks using their ID as the key.
        _next_id (int): The next available unique ID for adding new tasks.
    """

    def __init__(self):
        """Initialize the TaskManager with an empty task list and a starting ID."""
        self._tasks = {}
        self._next_id = 1

    def add(self, task_name: str, task_description: str) -> int:
        """
        Add a new task to the list and assign it a unique ID.

        Args:
            task_name (str): The name of the task.
            task_description (str): A description of the task.

        Returns:
            int: The unique ID assigned to the new task.

        Raises:
            ValueError: If the task name or description is empty or only contains whitespace.
        """
        if not task_name.strip() or not task_description.strip():
            raise ValueError("Task name and description cannot be empty or just whitespace.")

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
        Remove a task from the list based on its ID.

        Args:
            task_id (int): The ID of the task to be removed.

        Returns:
            bool: True if the task was successfully removed, False otherwise.
        """
        if task_id < 1 or task_id not in self._tasks:
            return False
        del self._tasks[task_id]
        return True

    def search(self, task_term: str) -> list[dict]:
        """
        Search for tasks based on a term provided.

        Args:
            task_term (str): The term to search within task names and descriptions.

        Returns:
            list[dict]: A list of dictionaries containing tasks that match the search term.
        """
        task_term = task_term.lower()
        return [
            {
                "id": task["id"],
                "task_name": task["task_name"],
                "task_description": task["task_description"],
                "is_finished": task["is_finished"]
            }
            for task in self._tasks.values()
            if task_term in task["task_name"].lower() or task_term in task["task_description"].lower()
        ]

    def finish(self, task_id: int) -> bool:
        """
        Mark a task as completed.

        Args:
            task_id (int): The ID of the task to be marked as completed.

        Returns:
            bool: True if the task was successfully marked as completed, False otherwise.
        """
        if task_id not in self._tasks:
            return False
        self._tasks[task_id]["is_finished"] = True
        return True

    def get_all(self) -> list[dict]:
        """
        Retrieve all tasks from the list.

        Returns:
            list[dict]: A list of dictionaries containing all tasks and their details.
        """
        return [
            {
                "id": task["id"],
                "task_name": task["task_name"],
                "task_description": task["task_description"],
                "is_finished": task["is_finished"]
            }
            for task in self._tasks.values()
        ]

    def clear_all(self) -> bool:
        """
        Clear all tasks from the list.

        Returns:
            bool: True indicating that all tasks have been removed.
        """
        self._tasks.clear()
        self._next_id = 1
        return True

# Example usage:
if __name__ == "__main__":
    manager = TaskManager()
    task_id = manager.add("Buy groceries", "Need to buy milk, eggs, and bread.")
    print(f"Added task with ID: {task_id}")
    print(f"All tasks: {manager.get_all()}")
    print(f"Search result for 'milk': {manager.search('milk')}")
    manager.finish(task_id)
    print(f"Completed task {task_id}: {manager.get_all()}")
    manager.remove(task_id)
    print(f"After removing task {task_id}: {manager.get_all()}")
    manager.clear_all()
    print(f"After clearing all: {manager.get_all()}")
