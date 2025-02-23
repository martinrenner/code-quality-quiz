
class TaskManager:
    """
    A class for managing a console-based todo list.
    
    Implements functionalities such as adding, removing, searching, marking as finished,
    retrieving all tasks, and clearing all tasks. Tasks are stored in-memory using a dictionary
    for efficient lookup by unique task ID.
    """

    def __init__(self):
        """
        Initializes the TaskManager instance with an empty task dictionary and a unique ID counter.
        """
        self.tasks = {}  # Stores tasks with their unique IDs as keys.
        self._next_id = 1  # Counter to assign unique task IDs.

    def add(self, task_name: str, task_description: str) -> int:
        """
        Adds a new task to the todo list.
        
        :param task_name: The name of the task. Must be a non-empty string.
        :param task_description: The description of the task. Must be a non-empty string.
        :return: The unique ID assigned to the newly added task.
        :raises ValueError: If task_name or task_description is empty or only whitespace.
        """
        if not isinstance(task_name, str) or not task_name.strip():
            raise ValueError("Task name cannot be empty.")
        if not isinstance(task_description, str) or not task_description.strip():
            raise ValueError("Task description cannot be empty.")

        task_id = self._next_id
        self.tasks[task_id] = {
            "id": task_id,
            "task_name": task_name.strip(),
            "task_description": task_description.strip(),
            "is_finished": False
        }
        self._next_id += 1
        return task_id

    def remove(self, task_id: int) -> bool:
        """
        Removes a task identified by its task_id.
        
        :param task_id: The unique ID of the task to remove.
        :return: True if the task was successfully removed, False if the task ID is invalid or not found.
        """
        if not isinstance(task_id, int) or task_id <= 0:
            return False
        if task_id in self.tasks:
            del self.tasks[task_id]
            return True
        return False

    def search(self, task_term: str) -> list:
        """
        Searches for tasks that contain the given search term in their name or description.
        The search is case-insensitive.
        
        :param task_term: The term to search for within task names and descriptions.
        :return: A list of tasks (as dictionaries) that match the search term.
        """
        if not isinstance(task_term, str) or not task_term.strip():
            # Return an empty list if search term is empty.
            return []
        term_lower = task_term.lower()
        return [task for task in self.tasks.values()
                if term_lower in task["task_name"].lower() or term_lower in task["task_description"].lower()]

    def finish(self, task_id: int) -> bool:
        """
        Marks a task as finished based on its task ID.
        
        :param task_id: The unique ID of the task to mark as finished.
        :return: True if the task was successfully marked as finished, False if the task ID is invalid or not found.
        """
        if not isinstance(task_id, int) or task_id <= 0:
            return False
        if task_id in self.tasks:
            self.tasks[task_id]["is_finished"] = True
            return True
        return False

    def get_all(self) -> list:
        """
        Retrieves all tasks in the todo list.
        
        :return: A list of all tasks with details in the format:
                 (id, task_name, task_description, is_finished)
        """
        return list(self.tasks.values())

    def clear_all(self) -> bool:
        """
        Clears all tasks from the todo list.
        
        :return: True after all tasks have been successfully cleared.
        """
        self.tasks.clear()
        return True


def display_tasks(tasks: list) -> None:
    """
    Helper function to print tasks in the specified tuple format:
    (id, task_name, task_description, is_finished)
    
    :param tasks: A list of task dictionaries.
    """
    if not tasks:
        print("No tasks found.")
        return
    for task in tasks:
        print(f"({task['id']}, {task['task_name']}, {task['task_description']}, {task['is_finished']})")


def main():
    """
    Main function to run the console-based todo list application.
    
    Provides a simple text menu interface to interact with the TaskManager.
    """
    task_manager = TaskManager()
    menu = """
    Please choose an option:
    1. Add Task
    2. Remove Task
    3. Search Tasks
    4. Mark Task as Finished
    5. Get All Tasks
    6. Clear All Tasks
    7. Exit
    """

    while True:
        print(menu)
        choice = input("Enter your choice (1-7): ").strip()

        if choice == "1":
            # Add Task
            try:
                name = input("Enter task name: ").strip()
                description = input("Enter task description: ").strip()
                task_id = task_manager.add(name, description)
                print(f"Task added with ID: {task_id}")
            except ValueError as ve:
                print(f"Error: {ve}")

        elif choice == "2":
            # Remove Task
            task_id_input = input("Enter task ID to remove: ").strip()
            if not task_id_input.isdigit():
                print("Invalid task ID. Please enter a positive integer.")
                continue
            task_id = int(task_id_input)
            if task_manager.remove(task_id):
                print(f"Task {task_id} removed successfully.")
            else:
                print(f"Task {task_id} not found.")

        elif choice == "3":
            # Search Tasks
            term = input("Enter search term: ").strip()
            results = task_manager.search(term)
            if results:
                print("Search results:")
                display_tasks(results)
            else:
                print("No matching tasks found.")

        elif choice == "4":
            # Mark Task as Finished
            task_id_input = input("Enter task ID to mark as finished: ").strip()
            if not task_id_input.isdigit():
                print("Invalid task ID. Please enter a positive integer.")
                continue
            task_id = int(task_id_input)
            if task_manager.finish(task_id):
                print(f"Task {task_id} marked as finished.")
            else:
                print(f"Task {task_id} not found.")

        elif choice == "5":
            # Get All Tasks
            tasks = task_manager.get_all()
            print("All Tasks:")
            display_tasks(tasks)

        elif choice == "6":
            # Clear All Tasks
            confirm = input("Are you sure you want to clear all tasks? (yes/no): ").strip().lower()
            if confirm == "yes":
                task_manager.clear_all()
                print("All tasks cleared.")
            else:
                print("Clear operation cancelled.")

        elif choice == "7":
            # Exit
            print("Exiting Todo List Application. Goodbye!")
            break

        else:
            print("Invalid choice. Please choose a valid option (1-7).")


if __name__ == "__main__":
    main()
