
class Task:
    def __init__(self, task_id: int, name: str, description: str, is_finished: bool = False):
        self.task_id = task_id
        self.name = name
        self.description = description
        self.is_finished = is_finished

    def __repr__(self):
        return f"Task(id={self.task_id}, name='{self.name}', description='{self.description}', is_finished={self.is_finished})"


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
        :raises ValueError: If task_name or task_description is empty.
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
        :return: True if the task was successfully removed, otherwise False.
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
        :return: A list of dictionaries containing matching tasks.
        """
        results = []
        for task in self.tasks:
            if task_term.lower() in task.name.lower() or task_term.lower() in task.description.lower():
                results.append(self._task_to_dict(task))
        return results

    def finish(self, task_id: int) -> bool:
        """
        Marks a task as completed.

        :param task_id: The ID of the task to mark as completed.
        :return: True if the task was successfully marked as completed, otherwise False.
        """
        for task in self.tasks:
            if task.task_id == task_id:
                task.is_finished = True
                return True
        return False

    def get_all(self) -> list[dict]:
        """
        Retrieves all tasks with their details.

        :return: A list of dictionaries containing all tasks.
        """
        return [self._task_to_dict(task) for task in self.tasks]

    def clear_all(self) -> bool:
        """
        Deletes all tasks and returns success status.

        :return: True if all tasks were successfully deleted, otherwise False.
        """
        self.tasks.clear()
        return True

    @staticmethod
    def _task_to_dict(task: Task) -> dict:
        return {
            "id": task.task_id,
            "name": task.name,
            "description": task.description,
            "is_finished": task.is_finished
        }
