
class TaskManager:
    def __init__(self):
        self.tasks = []
        self.task_id_counter = 0

    def add(self, task_name: str, task_description: str) -> int:
        """
        Adds a task to the todo list and returns its unique ID.

        Args:
            task_name (str): The name of the task.
            task_description (str): The description of the task.

        Returns:
            int: The unique ID of the added task.

        Raises:
            ValueError: If task_name or task_description is empty.
        """
        if not task_name or not task_description:
            raise ValueError("Task name and description cannot be empty.")

        task_id = self.task_id_counter
        self.task_id_counter += 1
        task = {
            "id": task_id,
            "name": task_name,
            "description": task_description,
            "is_finished": False
        }
        self.tasks.append(task)
        return task_id

    def remove(self, task_id: int) -> bool:
        """
        Removes a task from the todo list by its ID and returns success status.

        Args:
            task_id (int): The ID of the task to remove.

        Returns:
            bool: True if the task was successfully removed, False otherwise.
        """
        for task in self.tasks:
            if task["id"] == task_id:
                self.tasks.remove(task)
                return True
        return False

    def search(self, task_term: str) -> list[dict]:
        """
        Searches tasks by name or description and returns matching results.

        Args:
            task_term (str): The search term to match against task names or descriptions.

        Returns:
            list[dict]: A list of tasks that match the search term.
        """
        matching_tasks = []
        for task in self.tasks:
            if task_term.lower() in task["name"].lower() or task_term.lower() in task["description"].lower():
                matching_tasks.append(task)
        return matching_tasks

    def finish(self, task_id: int) -> bool:
        """
        Marks a task as completed by its ID.

        Args:
            task_id (int): The ID of the task to mark as completed.

        Returns:
            bool: True if the task was successfully marked as completed, False otherwise.
        """
        for task in self.tasks:
            if task["id"] == task_id:
                task["is_finished"] = True
                return True
        return False

    def get_all(self) -> list[dict]:
        """
        Retrieves all tasks with their details.

        Returns:
            list[dict]: A list of all tasks with their details.
        """
        return self.tasks

    def clear_all(self) -> bool:
        """
        Deletes all tasks from the todo list and returns success status.

        Returns:
            bool: True if all tasks were successfully deleted, False otherwise.
        """
        self.tasks = []
        return True
