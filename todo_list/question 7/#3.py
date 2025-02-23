
class Task:
    def __init__(self, task_id, task_name, task_description, is_finished=False):
        self.task_id = task_id
        self.task_name = task_name
        self.task_description = task_description
        self.is_finished = is_finished

    def to_dict(self):
        return {
            "id": self.task_id,
            "task_name": self.task_name,
            "task_description": self.task_description,
            "is_finished": self.is_finished
        }


class TaskManager:
    def __init__(self):
        self.tasks = []
        self.next_id = 1

    def add(self, task_name: str, task_description: str) -> int:
        """
        Adds a task and returns its unique ID.
        :param task_name: The name of the task.
        :param task_description: The description of the task.
        :return: The unique ID of the added task.
        """
        if not task_name or not task_description:
            raise ValueError("Task name and description cannot be empty.")

        task_id = self.next_id
        self.tasks.append(Task(task_id, task_name, task_description))
        self.next_id += 1
        return task_id

    def remove(self, task_id: int) -> bool:
        """
        Removes a task by ID and returns success status.
        :param task_id: The ID of the task to remove.
        :return: True if the task was successfully removed, False otherwise.
        """
        for task in self.tasks:
            if task.task_id == task_id:
                self.tasks.remove(task)
                return True
        return False

    def search(self, task_term: str) -> list[dict]:
        """
        Searches tasks by name or description and returns matching results.
        :param task_term: The search term to match against task names or descriptions.
        :return: A list of matching tasks as dictionaries.
        """
        if not task_term:
            raise ValueError("Search term cannot be empty.")

        matching_tasks = []
        for task in self.tasks:
            if task_term.lower() in task.task_name.lower() or task_term.lower() in task.task_description.lower():
                matching_tasks.append(task.to_dict())
        return matching_tasks

    def finish(self, task_id: int) -> bool:
        """
        Marks a task as completed.
        :param task_id: The ID of the task to mark as completed.
        :return: True if the task was successfully marked as completed, False otherwise.
        """
        for task in self.tasks:
            if task.task_id == task_id:
                task.is_finished = True
                return True
        return False

    def get_all(self) -> list[dict]:
        """
        Retrieves all tasks with their details.
        :return: A list of all tasks as dictionaries.
        """
        return [task.to_dict() for task in self.tasks]

    def clear_all(self) -> bool:
        """
        Deletes all tasks and returns success status.
        :return: True if all tasks were successfully deleted, False otherwise.
        """
        self.tasks.clear()
        self.next_id = 1
        return True
