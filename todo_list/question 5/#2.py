
class Task:
    """Represents a task in the to-do list."""
    def __init__(self, task_id, name, description, is_finished=False):
        self.id = task_id
        self.name = name
        self.description = description
        self.is_finished = is_finished

    def to_dict(self):
        """Returns the task as a dictionary."""
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'is_finished': self.is_finished
        }


class TaskManager:
    """Manages tasks in the to-do list."""
    def __init__(self):
        self.tasks = []
        self.next_id = 1

    def add(self, task_name, task_description):
        """Adds a task and returns its unique ID."""
        if not task_name:
            raise ValueError("Task name cannot be empty.")
        task = Task(self.next_id, task_name, task_description)
        self.tasks.append(task)
        self.next_id += 1
        return task.id

    def remove(self, task_id):
        """Removes a task by ID and returns success status."""
        task = self._find_task_by_id(task_id)
        if task:
            self.tasks.remove(task)
            return True
        return False

    def search(self, task_term):
        """Searches tasks by name or description and returns matching results."""
        if not task_term:
            raise ValueError("Search term cannot be empty.")
        matching_tasks = [task.to_dict() for task in self.tasks
                          if task_term.lower() in task.name.lower()
                          or task_term.lower() in task.description.lower()]
        return matching_tasks

    def finish(self, task_id):
        """Marks a task as completed."""
        task = self._find_task_by_id(task_id)
        if task:
            task.is_finished = True
            return True
        return False

    def get_all(self):
        """Retrieves all tasks with their details."""
        return [task.to_dict() for task in self.tasks]

    def clear_all(self):
        """Deletes all tasks and returns success status."""
        self.tasks.clear()
        self.next_id = 1
        return True

    def _find_task_by_id(self, task_id):
        """Finds a task by its ID."""
        for task in self.tasks:
            if task.id == task_id:
                return task
        return None
