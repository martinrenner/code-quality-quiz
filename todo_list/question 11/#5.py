class TaskManager:
    def __init__(self):
        """Initialize the TaskManager with an empty task list and a task ID counter."""
        self.tasks = []
        self.next_id = 1

    def add(self, task_name: str, task_description: str) -> int:
        """
        Adds a task and returns its unique ID.

        :param task_name: Name of the task
        :param task_description: Description of the task
        :return: Unique ID of the task
        """
        if not task_name or not task_description:
            raise ValueError("Task name and description cannot be empty.")

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
        Removes a task by ID and returns success status.

        :param task_id: ID of the task to remove
        :return: True if task was removed successfully, False otherwise
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
        Searches tasks by name or description and returns matching results.

        :param task_term: Term to search in task name or description
        :return: List of matching tasks
        """
        if not task_term:
            raise ValueError("Search term cannot be empty.")

        return [task for task in self.tasks if task_term in task['task_name'] or task_term in task['task_description']]

    def finish(self, task_id: int) -> bool:
        """
        Marks a task as completed.

        :param task_id: ID of the task to mark as completed
        :return: True if task was marked as completed, False otherwise
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

        :return: List of all tasks
        """
        return self.tasks

    def clear_all(self) -> bool:
        """
        Deletes all tasks and returns success status.

        :return: True if all tasks were deleted successfully
        """
        self.tasks.clear()
        self.next_id = 1
        return True

# Example usage
if __name__ == "__main__":
    tm = TaskManager()
    tm.add("Buy groceries", "Milk, Bread, Eggs")
    tm.add("Read book", "Finish 'Python Programming'")
    print(tm.get_all())
    tm.finish(1)
    print(tm.get_all())
    tm.remove(1)
    print(tm.get_all())
    print(tm.search("book"))
    tm.clear_all()
    print(tm.get_all())
