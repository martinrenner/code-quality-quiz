
class TaskManager:
    def __init__(self):
        """Initialize the TaskManager with an empty task list and a task ID counter."""
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
            raise ValueError("Task name and description cannot be empty.")

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
            bool: True if the task was successfully removed, False otherwise.
        """
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
            raise ValueError("Search term cannot be empty.")

        return [task for task in self.tasks.values() if task_term in task["task_name"] or task_term in task["task_description"]]

    def finish(self, task_id: int) -> bool:
        """
        Marks a task as completed.

        Args:
            task_id (int): The ID of the task to mark as completed.

        Returns:
            bool: True if the task was successfully marked as completed, False otherwise.
        """
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
            bool: True if all tasks were successfully deleted, False otherwise.
        """
        self.tasks.clear()
        self.next_id = 1
        return True

# Example usage:
if __name__ == "__main__":
    task_manager = TaskManager()

    # Add tasks
    task_id1 = task_manager.add("Buy groceries", "Milk, Bread, Eggs")
    task_id2 = task_manager.add("Read book", "Finish reading 'Python Cookbook'")

    # Get all tasks
    print(task_manager.get_all())

    # Search tasks
    print(task_manager.search("book"))

    # Finish a task
    task_manager.finish(task_id1)

    # Remove a task
    task_manager.remove(task_id2)

    # Get all tasks again
    print(task_manager.get_all())

    # Clear all tasks
    task_manager.clear_all()
    print(task_manager.get_all())
