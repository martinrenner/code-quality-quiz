class TaskManager:
    def __init__(self):
        """Initializes the TaskManager with an empty task dictionary."""
        self.tasks = {}
        self.next_id = 1

    def add(self, task_name: str, task_description: str) -> int:
        """
        Adds a task and returns its unique ID.

        Args:
            task_name (str): The name of the task.
            task_description (str): The description of the task.

        Returns:
            int: The unique ID of the newly added task.
        """
        if not task_name or not task_description:
            raise ValueError("Task name and description must not be empty.")

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
        Removes a task by ID and returns success status.

        Args:
            task_id (int): The ID of the task to remove.

        Returns:
            bool: True if the task was removed, False otherwise.
        """
        if task_id <= 0:
            raise ValueError("Task ID must be a positive integer.")

        if task_id in self.tasks:
            del self.tasks[task_id]
            return True
        return False

    def search(self, task_term: str) -> list[dict]:
        """
        Searches tasks by name or description and returns matching results.

        Args:
            task_term (str): The term to search for in task names or descriptions.

        Returns:
            list[dict]: A list of tasks that match the search term.
        """
        if not task_term:
            raise ValueError("Search term must not be empty.")

        matching_tasks = [
            task for task in self.tasks.values()
            if task_term.lower() in task["task_name"].lower() or task_term.lower() in task["task_description"].lower()
        ]
        return matching_tasks

    def finish(self, task_id: int) -> bool:
        """
        Marks a task as completed.

        Args:
            task_id (int): The ID of the task to mark as completed.

        Returns:
            bool: True if the task was marked as completed, False otherwise.
        """
        if task_id <= 0:
            raise ValueError("Task ID must be a positive integer.")

        if task_id in self.tasks:
            self.tasks[task_id]["is_finished"] = True
            return True
        return False

    def get_all(self) -> list[dict]:
        """
        Retrieves all tasks with their details.

        Returns:
            list[dict]: A list of all tasks.
        """
        return list(self.tasks.values())

    def clear_all(self) -> bool:
        """
        Deletes all tasks and returns success status.

        Returns:
            bool: True if all tasks were deleted, False otherwise.
        """
        self.tasks.clear()
        self.next_id = 1
        return True

# Example usage:
if __name__ == "__main__":
    tm = TaskManager()
    tm.add("Buy groceries", "Milk, Bread, Eggs")
    tm.add("Finish project", "Complete the final report")
    print(tm.get_all())
    tm.finish(1)
    print(tm.get_all())
    tm.remove(2)
    print(tm.get_all())
    print(tm.search("project"))
    tm.clear_all()
    print(tm.get_all())
