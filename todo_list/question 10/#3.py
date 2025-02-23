
class TaskManager:
    def __init__(self):
        """
        Initializes the TaskManager with an empty task list and a task ID counter.
        """
        self.tasks = []
        self.next_id = 1

    def add(self, task_name: str, task_description: str) -> int:
        """
        Adds a task to the task list and returns its unique ID.

        Args:
            task_name (str): The name of the task.
            task_description (str): The description of the task.

        Returns:
            int: The unique ID of the added task.
        """
        if not task_name or not task_description:
            raise ValueError("Task name and description must not be empty.")

        task = {
            'id': self.next_id,
            'task_name': task_name,
            'task_description': task_description,
            'is_finished': False
        }
        self.tasks.append(task)
        self.next_id += 1
        return task['id']

    def remove(self, task_id: int) -> bool:
        """
        Removes a task from the task list by its ID.

        Args:
            task_id (int): The ID of the task to remove.

        Returns:
            bool: True if the task was successfully removed, False otherwise.
        """
        if task_id <= 0:
            raise ValueError("Task ID must be a positive integer.")

        for task in self.tasks:
            if task['id'] == task_id:
                self.tasks.remove(task)
                return True
        return False

    def search(self, task_term: str) -> list[dict]:
        """
        Searches for tasks containing the task_term in their name or description.

        Args:
            task_term (str): The term to search for.

        Returns:
            list[dict]: A list of tasks that match the search term.
        """
        if not task_term:
            raise ValueError("Search term must not be empty.")

        matching_tasks = [task for task in self.tasks if task_term.lower() in task['task_name'].lower() or task_term.lower() in task['task_description'].lower()]
        return matching_tasks

    def finish(self, task_id: int) -> bool:
        """
        Marks a task as completed.

        Args:
            task_id (int): The ID of the task to mark as completed.

        Returns:
            bool: True if the task was successfully marked as completed, False otherwise.
        """
        if task_id <= 0:
            raise ValueError("Task ID must be a positive integer.")

        for task in self.tasks:
            if task['id'] == task_id:
                task['is_finished'] = True
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
        Deletes all tasks.

        Returns:
            bool: True if all tasks were successfully deleted, False otherwise.
        """
        self.tasks = []
        self.next_id = 1
        return True

# Example usage:
if __name__ == "__main__":
    task_manager = TaskManager()

    # Add tasks
    task_manager.add("Buy groceries", "Milk, Bread, Eggs")
    task_manager.add("Read book", "Finish 'The Great Gatsby'")

    # Get all tasks
    print("All tasks:", task_manager.get_all())

    # Search tasks
    print("Search results for 'book':", task_manager.search("book"))

    # Finish a task
    task_manager.finish(1)

    # Remove a task
    task_manager.remove(2)

    # Clear all tasks
    task_manager.clear_all()
    print("All tasks after clear:", task_manager.get_all())
