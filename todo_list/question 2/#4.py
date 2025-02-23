
class TaskManager:
    """
    A class to manage a todo list with functionalities to add, remove, search, finish, and list tasks.
    
    The class supports CRUD operations on tasks, stored in an in-memory dictionary for quick access.
    """

    def __init__(self):
        """
        Initializes the TaskManager with an empty task dictionary.
        """
        self.tasks = {}
        self.next_id = 1

    def add(self, task_name: str, task_description: str) -> int:
        """
        Adds a new task to the todo list.

        :param task_name: The name of the task.
        :param task_description: A description of the task.
        :return: The unique ID of the newly added task.
        :raises ValueError: If task name or description is empty.
        """
        if not task_name.strip() or not task_description.strip():
            raise ValueError("Task name and description cannot be empty.")
        
        task_id = self.next_id
        self.tasks[task_id] = {
            "id": task_id,
            "name": task_name.strip(),
            "description": task_description.strip(),
            "is_finished": False
        }
        self.next_id += 1
        return task_id

    def remove(self, task_id: int) -> bool:
        """
        Removes a task from the todo list by its ID.

        :param task_id: The ID of the task to be removed.
        :return: True if the task was successfully removed, False otherwise.
        :raises ValueError: If task_id is non-positive.
        """
        if task_id <= 0:
            raise ValueError("Task ID must be a positive integer.")
        
        if task_id in self.tasks:
            del self.tasks[task_id]
            return True
        return False

    def search(self, task_term: str) -> list[dict]:
        """
        Searches for tasks by name or description.

        :param task_term: The search term.
        :return: A list of task dictionaries that match the search term.
        :raises ValueError: If the search term is empty.
        """
        if not task_term.strip():
            raise ValueError("Search term cannot be empty.")
        
        task_term = task_term.lower()
        return [
            {
                "id": task["id"],
                "name": task["name"],
                "description": task["description"],
                "is_finished": task["is_finished"]
            }
            for task in self.tasks.values()
            if task_term in task["name"].lower() or task_term in task["description"].lower()
        ]

    def finish(self, task_id: int) -> bool:
        """
        Marks a task as completed.

        :param task_id: The ID of the task to be completed.
        :return: True if the task was successfully marked as completed, False otherwise.
        :raises ValueError: If task_id is non-positive.
        """
        if task_id <= 0:
            raise ValueError("Task ID must be a positive integer.")
        
        if task_id in self.tasks:
            self.tasks[task_id]["is_finished"] = True
            return True
        return False

    def get_all(self) -> list[dict]:
        """
        Retrieves all tasks in the todo list.

        :return: A list of all task dictionaries.
        """
        return [
            {
                "id": task["id"],
                "name": task["name"],
                "description": task["description"],
                "is_finished": task["is_finished"]
            }
            for task in self.tasks.values()
        ]

    def clear_all(self) -> bool:
        """
        Deletes all tasks from the todo list.

        :return: True if all tasks were successfully deleted.
        """
        self.tasks.clear()
        self.next_id = 1
        return True
