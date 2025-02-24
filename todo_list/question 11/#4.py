class TaskManager:
    def __init__(self):
        """
        Initializes the TaskManager with an empty task dictionary and a counter for unique IDs.
        """
        self.tasks = {}
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
            ValueError: If task_name or task_description is an empty string.
        """
        if not task_name or not task_description:
            raise ValueError("Task name and description cannot be empty.")

        task_id = self.next_id
        self.tasks[task_id] = {
            'id': task_id,
            'task_name': task_name,
            'task_description': task_description,
            'is_finished': False
        }
        self.next_id += 1
        return task_id

    def remove(self, task_id: int) -> bool:
        """
        Removes a task by ID and returns success status.

        Args:
            task_id (int): The unique ID of the task to be removed.

        Returns:
            bool: True if the task was successfully removed, False otherwise.

        Raises:
            ValueError: If task_id is negative or non-existent.
        """
        if task_id < 0 or task_id not in self.tasks:
            raise ValueError("Invalid task ID.")

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
        matching_tasks = [
            task for task in self.tasks.values()
            if task_term.lower() in task['task_name'].lower() or task_term.lower() in task['task_description'].lower()
        ]
        return matching_tasks

    def finish(self, task_id: int) -> bool:
        """
        Marks a task as completed.

        Args:
            task_id (int): The unique ID of the task to be marked as finished.

        Returns:
            bool: True if the task was successfully marked as finished, False otherwise.

        Raises:
            ValueError: If task_id is negative or non-existent.
        """
        if task_id < 0 or task_id not in self.tasks:
            raise ValueError("Invalid task ID.")

        if task_id in self.tasks:
            self.tasks[task_id]['is_finished'] = True
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
            bool: True if all tasks were successfully deleted, False otherwise.
        """
        self.tasks.clear()
        self.next_id = 1
        return True


if __name__ == "__main__":
    manager = TaskManager()

    # Add tasks
    task_id1 = manager.add("Task 1", "Description 1")
    task_id2 = manager.add("Task 2", "Description 2")

    # Get all tasks
    print("All tasks:", manager.get_all())

    # Search tasks
    print("Search 'Task 1':", manager.search("Task 1"))

    # Finish a task
    print("Finish task_id1:", manager.finish(task_id1))

    # Remove a task
    print("Remove task_id1:", manager.remove(task_id1))

    # Get all tasks after removal
    print("All tasks after removal:", manager.get_all())

    # Clear all tasks
    print("Clear all tasks:", manager.clear_all())
    print("All tasks after clear:", manager.get_all())
