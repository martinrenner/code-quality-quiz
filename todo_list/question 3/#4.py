
class TaskManager:
    """
    A class to manage a list of tasks in memory.

    This class provides methods to add, remove, search, mark as finished,
    retrieve, and clear all tasks in the todo list.
    """

    def __init__(self):
        """Initialize an empty task list."""
        self.tasks = {}
        self.next_id = 1

    def add(self, task_name: str, task_description: str) -> int:
        """
        Add a new task to the list.

        Args:
            task_name (str): The name of the task.
            task_description (str): The description of the task.

        Returns:
            int: The unique ID of the added task.

        Raises:
            ValueError: If task_name or task_description is empty.
        """
        if not task_name.strip() or not task_description.strip():
            raise ValueError("Task name and description cannot be empty.")

        task_id = self.next_id
        self.tasks[task_id] = {
            "id": task_id,
            "task_name": task_name.strip(),
            "task_description": task_description.strip(),
            "is_finished": False
        }
        self.next_id += 1
        return task_id

    def remove(self, task_id: int) -> bool:
        """
        Remove a task from the list by its ID.

        Args:
            task_id (int): The ID of the task to remove.

        Returns:
            bool: True if the task was successfully removed, False otherwise.
        """
        if task_id < 1 or task_id not in self.tasks:
            return False
        del self.tasks[task_id]
        return True

    def search(self, task_term: str) -> list[dict]:
        """
        Search for tasks by name or description.

        Args:
            task_term (str): The search term to look for in task names and descriptions.

        Returns:
            list[dict]: A list of tasks matching the search term.
        """
        task_term = task_term.lower()
        results = []
        for task in self.tasks.values():
            if task_term in task["task_name"].lower() or task_term in task["task_description"].lower():
                results.append(task)
        return results

    def finish(self, task_id: int) -> bool:
        """
        Mark a task as finished.

        Args:
            task_id (int): The ID of the task to mark as finished.

        Returns:
            bool: True if the task was successfully marked as finished, False otherwise.
        """
        if task_id < 1 or task_id not in self.tasks:
            return False
        self.tasks[task_id]["is_finished"] = True
        return True

    def get_all(self) -> list[dict]:
        """
        Retrieve all tasks in the list.

        Returns:
            list[dict]: A list of all tasks with their details.
        """
        return list(self.tasks.values())

    def clear_all(self) -> bool:
        """
        Clear all tasks from the list.

        Returns:
            bool: True if all tasks were successfully cleared, False otherwise.
        """
        self.tasks.clear()
        self.next_id = 1
        return True


# Example usage
task_manager = TaskManager()

# Add a task
task_id = task_manager.add("Buy groceries", "Need to buy milk, eggs, and bread")
print(f"Added task with ID: {task_id}")

# Get all tasks
all_tasks = task_manager.get_all()
print("All tasks:", all_tasks)

# Search for tasks
search_results = task_manager.search("milk")
print("Search results:", search_results)

# Mark a task as finished
success = task_manager.finish(task_id)
print(f"Task marked as finished: {success}")

# Remove a task
removed = task_manager.remove(task_id)
print(f"Task removed: {removed}")

# Clear all tasks
cleared = task_manager.clear_all()
print(f"All tasks cleared: {cleared}")
