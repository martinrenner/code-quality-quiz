
class TaskManager:
    def __init__(self):
        """
        Initializes the TaskManager with an empty task list.
        """
        self.tasks = []
        self.next_id = 1

    def add(self, task_name: str, task_description: str) -> int:
        """
        Adds a task to the list and returns its unique ID.

        :param task_name: The name of the task.
        :param task_description: The description of the task.
        :return: The unique ID of the task.
        :raises ValueError: If task_name or task_description is empty.
        """
        if not task_name or not task_description:
            raise ValueError("Task name and description must not be empty.")

        task_id = self.next_id
        self.next_id += 1
        task = {
            'id': task_id,
            'task_name': task_name,
            'task_description': task_description,
            'is_finished': False
        }
        self.tasks.append(task)
        return task_id

    def remove(self, task_id: int) -> bool:
        """
        Removes a task by its unique ID.

        :param task_id: The unique ID of the task to remove.
        :return: True if the task was successfully removed, False otherwise.
        :raises ValueError: If task_id is non-positive.
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

        :param task_term: The term to search for in task names or descriptions.
        :return: A list of tasks that match the search term.
        """
        matching_tasks = [task for task in self.tasks if task_term in task['task_name'] or task_term in task['task_description']]
        return matching_tasks

    def finish(self, task_id: int) -> bool:
        """
        Marks a task as completed.

        :param task_id: The unique ID of the task to mark as completed.
        :return: True if the task was successfully marked as completed, False otherwise.
        :raises ValueError: If task_id is non-positive.
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

        :return: A list of all tasks.
        """
        return self.tasks

    def clear_all(self) -> bool:
        """
        Deletes all tasks.

        :return: True if all tasks were successfully deleted.
        """
        self.tasks = []
        self.next_id = 1
        return True

# Example usage
if __name__ == "__main__":
    manager = TaskManager()
    print(manager.add("Buy groceries", "Milk, Bread, Eggs"))
    print(manager.add("Read book", "Finish reading 'Python Programming'"))
    print(manager.get_all())
    print(manager.finish(1))
    print(manager.get_all())
    print(manager.search("Read"))
    print(manager.remove(2))
    print(manager.get_all())
    print(manager.clear_all())
    print(manager.get_all())
