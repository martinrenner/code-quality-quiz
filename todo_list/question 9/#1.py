
import uuid

class TaskManager:
    """
    A class to manage a todo list of tasks.

    This class provides methods to add, remove, search, finish, get_all, and clear_all tasks.
    Tasks are stored in memory and each task has a unique ID, name, description, and completion status.
    """

    def __init__(self):
        """
        Initialize the TaskManager with an empty list of tasks.
        """
        self.tasks = {}

    def add(self, task_name: str, task_description: str) -> int:
        """
        Add a new task to the todo list.

        Args:
            task_name (str): The name of the task.
            task_description (str): The description of the task.

        Returns:
            int: The unique ID of the newly added task.

        Raises:
            ValueError: If task_name or task_description is empty.
        """
        if not task_name.strip() or not task_description.strip():
            raise ValueError("Task name and description cannot be empty.")

        task_id = uuid.uuid4().int & (1<<31)-1  # Generate a unique 32-bit integer ID
        self.tasks[task_id] = {
            'id': task_id,
            'task_name': task_name.strip(),
            'task_description': task_description.strip(),
            'is_finished': False
        }
        return task_id

    def remove(self, task_id: int) -> bool:
        """
        Remove a task from the todo list by its ID.

        Args:
            task_id (int): The ID of the task to be removed.

        Returns:
            bool: True if the task was successfully removed, False otherwise.
        """
        if task_id in self.tasks:
            del self.tasks[task_id]
            return True
        return False

    def search(self, task_term: str) -> list[dict]:
        """
        Search for tasks by name or description.

        Args:
            task_term (str): The term to search for in task names and descriptions.

        Returns:
            list[dict]: A list of tasks that match the search term.
        """
        if not task_term.strip():
            return []

        search_term = task_term.lower()
        results = []
        for task in self.tasks.values():
            if search_term in task['task_name'].lower() or search_term in task['task_description'].lower():
                results.append(task)
        return results

    def finish(self, task_id: int) -> bool:
        """
        Mark a task as completed.

        Args:
            task_id (int): The ID of the task to be marked as completed.

        Returns:
            bool: True if the task was successfully marked as completed, False otherwise.
        """
        if task_id in self.tasks:
            self.tasks[task_id]['is_finished'] = True
            return True
        return False

    def get_all(self) -> list[dict]:
        """
        Retrieve all tasks in the todo list.

        Returns:
            list[dict]: A list of all tasks with their details.
        """
        return list(self.tasks.values())

    def clear_all(self) -> bool:
        """
        Delete all tasks from the todo list.

        Returns:
            bool: True if all tasks were successfully deleted, False otherwise.
        """
        self.tasks.clear()
        return True


# Create a TaskManager instance
todo_list = TaskManager()

# Add a task
task_id = todo_list.add("Buy groceries", "Need to buy milk, eggs, and bread")
print(f"Added task with ID: {task_id}")

# Get all tasks
all_tasks = todo_list.get_all()
print("All tasks:", all_tasks)

# Search for tasks
search_results = todo_list.search("groceries")
print("Search results:", search_results)

# Mark a task as completed
success = todo_list.finish(task_id)
print(f"Task marked as completed: {success}")

# Remove a task
removed = todo_list.remove(task_id)
print(f"Task removed: {removed}")

# Clear all tasks
cleared = todo_list.clear_all()
print(f"All tasks cleared: {cleared}")
