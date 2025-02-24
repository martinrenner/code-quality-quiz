class TaskManager:
    def __init__(self):
        """
        Initializes the TaskManager with an empty task list.
        """
        self.tasks = []
        self.next_id = 1

    def add(self, task_name: str, task_description: str) -> int:
        """
        Adds a task and returns its unique ID.

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
        Removes a task by ID and returns success status.

        Args:
            task_id (int): The ID of the task to remove.

        Returns:
            bool: True if the task was removed successfully, False otherwise.

        Raises:
            ValueError: If task_id is negative.
        """
        if task_id < 0:
            raise ValueError("Task ID cannot be negative.")

        for task in self.tasks:
            if task["id"] == task_id:
                self.tasks.remove(task)
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
        return [task for task in self.tasks if task_term in task["task_name"] or task_term in task["task_description"]]

    def finish(self, task_id: int) -> bool:
        """
        Marks a task as completed.

        Args:
            task_id (int): The ID of the task to mark as completed.

        Returns:
            bool: True if the task was marked as completed successfully, False otherwise.

        Raises:
            ValueError: If task_id is negative.
        """
        if task_id < 0:
            raise ValueError("Task ID cannot be negative.")

        for task in self.tasks:
            if task["id"] == task_id:
                task["is_finished"] = True
                return True
        return False

    def get_all(self) -> list[dict]:
        """
        Retrieves all tasks with their details.

        Returns:
            list[dict]: A list of all tasks.
        """
        return self.tasks

    def clear_all(self) -> bool:
        """
        Deletes all tasks and returns success status.

        Returns:
            bool: True if all tasks were deleted successfully.
        """
        self.tasks = []
        self.next_id = 1
        return True

# Example usage
if __name__ == "__main__":
    manager = TaskManager()
    manager.add("Buy groceries", "Milk, Bread, Eggs")
    manager.add("Pay bills", "Electricity, Water, Internet")
    print(manager.get_all())
    manager.finish(1)
    print(manager.get_all())
    manager.remove(2)
    print(manager.get_all())
    print(manager.search("groceries"))
    manager.clear_all()
    print(manager.get_all())
