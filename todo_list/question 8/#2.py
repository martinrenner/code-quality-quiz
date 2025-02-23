
class TaskManager:
    """
    Manages a to-do list with functionalities to add, remove, search,
    finish, retrieve, and clear tasks.  This class adheres to ISO/IEC 25010
    standards by focusing on maintainability, reliability, and usability.
    """

    def __init__(self):
        """
        Initializes the TaskManager with an empty task list and a task ID counter.
        """
        self.tasks = []  # In-memory storage for tasks
        self.next_task_id = 1  # Counter to ensure unique task IDs

    def add(self, task_name: str, task_description: str) -> int:
        """
        Adds a new task to the to-do list.

        Args:
            task_name (str): The name of the task.
            task_description (str): A description of the task.

        Returns:
            int: The unique ID assigned to the newly added task.

        Raises:
            ValueError: If task_name or task_description is empty.
        """
        if not task_name.strip():
            raise ValueError("Task name cannot be empty.")
        if not task_description.strip():
            raise ValueError("Task description cannot be empty.")

        task = {
            "id": self.next_task_id,
            "name": task_name,
            "description": task_description,
            "is_finished": False,
        }
        self.tasks.append(task)
        self.next_task_id += 1
        return task["id"]

    def remove(self, task_id: int) -> bool:
        """
        Removes a task from the to-do list by its ID.

        Args:
            task_id (int): The ID of the task to be removed.

        Returns:
            bool: True if the task was successfully removed, False otherwise.

        Raises:
            ValueError: If task_id is not a positive integer.
        """
        if not isinstance(task_id, int) or task_id <= 0:
            raise ValueError("Task ID must be a positive integer.")

        for i, task in enumerate(self.tasks):
            if task["id"] == task_id:
                del self.tasks[i]
                return True
        return False  # Task with given ID not found

    def search(self, task_term: str) -> list[dict]:
        """
        Searches for tasks by name or description.

        Args:
            task_term (str): The term to search for within task names and descriptions.

        Returns:
            list[dict]: A list of tasks that match the search term
                        (case-insensitive).  Returns an empty list if no
                        matches are found or if the search term is empty.
        """
        if not task_term.strip():
            return []  # Return empty list for empty search term

        results = []
        for task in self.tasks:
            if (
                task_term.lower() in task["name"].lower()
                or task_term.lower() in task["description"].lower()
            ):
                results.append(task)
        return results

    def finish(self, task_id: int) -> bool:
        """
        Marks a task as completed.

        Args:
            task_id (int): The ID of the task to be marked as finished.

        Returns:
            bool: True if the task was successfully marked as finished,
                  False otherwise.

        Raises:
            ValueError: If task_id is not a positive integer.
        """
        if not isinstance(task_id, int) or task_id <= 0:
            raise ValueError("Task ID must be a positive integer.")

        for task in self.tasks:
            if task["id"] == task_id:
                task["is_finished"] = True
                return True
        return False  # Task with given ID not found

    def get_all(self) -> list[dict]:
        """
        Retrieves all tasks in the to-do list.

        Returns:
            list[dict]: A list of all tasks, including their details (id, name,
            description, is_finished).  Returns an empty list if there are no tasks.
        """
        return self.tasks

    def clear_all(self) -> bool:
        """
        Deletes all tasks from the to-do list.

        Returns:
            bool: Always returns True, indicating that the list has been cleared.
        """
        self.tasks = []
        return True


def main():
    """
    Main function to demonstrate the TaskManager class through a console
    interface.
    """
    task_manager = TaskManager()

    while True:
        print("\nTodo List Menu:")
        print("1. Add Task")
        print("2. Remove Task")
        print("3. Search Tasks")
        print("4. Finish Task")
        print("5. View All Tasks")
        print("6. Clear All Tasks")
        print("7. Exit")

        choice = input("Enter your choice: ")

        try:
            if choice == "1":
                name = input("Enter task name: ")
                description = input("Enter task description: ")
                task_id = task_manager.add(name, description)
                print(f"Task added successfully with ID: {task_id}")

            elif choice == "2":
                task_id = int(input("Enter task ID to remove: "))
                if task_manager.remove(task_id):
                    print("Task removed successfully.")
                else:
                    print("Task not found.")

            elif choice == "3":
                term = input("Enter search term: ")
                results = task_manager.search(term)
                if results:
                    print("Search Results:")
                    for task in results:
                        print(
                            f"  ID: {task['id']}, Name: {task['name']}, Description: {task['description']}, Finished: {task['is_finished']}"
                        )
                else:
                    print("No tasks found matching the search term.")

            elif choice == "4":
                task_id = int(input("Enter task ID to mark as finished: "))
                if task_manager.finish(task_id):
                    print("Task marked as finished.")
                else:
                    print("Task not found.")

            elif choice == "5":
                tasks = task_manager.get_all()
                if tasks:
                    print("All Tasks:")
                    for task in tasks:
                        print(
                            f"  ID: {task['id']}, Name: {task['name']}, Description: {task['description']}, Finished: {task['is_finished']}"
                        )
                else:
                    print("No tasks in the list.")

            elif choice == "6":
                task_manager.clear_all()
                print("All tasks cleared.")

            elif choice == "7":
                print("Exiting...")
                break

            else:
                print("Invalid choice. Please try again.")

        except ValueError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()

