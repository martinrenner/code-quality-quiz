
from typing import List, Dict

class TaskManager:
    def __init__(self):
        self.tasks: List[Dict] = []
        self.next_id: int = 1

    def add(self, task_name: str, task_description: str) -> int:
        """
        Adds a task to the todo list and returns its unique ID.

        :param task_name: The name of the task.
        :param task_description: The description of the task.
        :return: The unique ID of the added task.
        :raises ValueError: If task_name or task_description is empty.
        """
        if not task_name or not task_description:
            raise ValueError("Task name and description cannot be empty.")

        task_id = self.next_id
        self.tasks.append({
            "id": task_id,
            "name": task_name,
            "description": task_description,
            "is_finished": False
        })
        self.next_id += 1
        return task_id

    def remove(self, task_id: int) -> bool:
        """
        Removes a task from the todo list by its ID.

        :param task_id: The ID of the task to remove.
        :return: True if the task was successfully removed, False otherwise.
        """
        for task in self.tasks:
            if task["id"] == task_id:
                self.tasks.remove(task)
                return True
        return False

    def search(self, task_term: str) -> List[Dict]:
        """
        Searches tasks by name or description and returns matching results.

        :param task_term: The search term to match against task names or descriptions.
        :return: A list of tasks that match the search term.
        """
        return [task for task in self.tasks if task_term.lower() in task["name"].lower() or task_term.lower() in task["description"].lower()]

    def finish(self, task_id: int) -> bool:
        """
        Marks a task as completed.

        :param task_id: The ID of the task to mark as completed.
        :return: True if the task was successfully marked as completed, False otherwise.
        """
        for task in self.tasks:
            if task["id"] == task_id:
                task["is_finished"] = True
                return True
        return False

    def get_all(self) -> List[Dict]:
        """
        Retrieves all tasks with their details.

        :return: A list of all tasks.
        """
        return self.tasks

    def clear_all(self) -> bool:
        """
        Deletes all tasks from the todo list.

        :return: True if all tasks were successfully deleted, False otherwise.
        """
        self.tasks.clear()
        self.next_id = 1
        return True
