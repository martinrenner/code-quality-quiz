
class TaskManager:
    """
    Manages a to-do list with functionalities to add, remove, search,
    finish, retrieve, and clear tasks.  This class emphasizes efficiency,
    maintainability, and robust error handling.
    """

    def __init__(self):
        """
        Initializes the TaskManager with an empty task list and a counter for
        generating unique task IDs.
        """
        self.tasks = {}  # Use a dictionary for efficient lookups by ID.
        self.next_id = 1  # Counter for generating unique task IDs.

    def add(self, task_name: str, task_description: str) -> int:
        """
        Adds a new task to the to-do list.

        Args:
            task_name: The name of the task (must be non-empty).
            task_description: A description of the task.

        Returns:
            The unique ID of the newly added task.

        Raises:
            ValueError: If the task_name is empty.
        """
        if not task_name.strip():
            raise ValueError("Task name cannot be empty.")

        task_id = self.next_id
        self.tasks[task_id] = {
            "id": task_id,
            "name": task_name,
            "description": task_description,
            "is_finished": False,
        }
        self.next_id += 1
        return task_id

    def remove(self, task_id: int) -> bool:
        """
        Removes a task from the to-do list by its ID.

        Args:
            task_id: The ID of the task to remove.

        Returns:
            True if the task was successfully removed, False otherwise.

        Raises:
            TypeError: If task_id is not an integer.
            ValueError: If task_id is not positive.
        """
        if not isinstance(task_id, int):
            raise TypeError("Task ID must be an integer.")
        if task_id <= 0:
            raise ValueError("Task ID must be a positive integer.")

        if task_id in self.tasks:
            del self.tasks[task_id]
            return True
        else:
            return False  # Task not found.

    def search(self, task_term: str) -> list[dict]:
        """
        Searches for tasks by name or description.

        Args:
            task_term: The search term (can be part of the name or description).

        Returns:
            A list of matching tasks.  Returns an empty list if no matches
            are found.

        Raises:
            ValueError: If the task_term is empty.
        """
        if not task_term.strip():
            raise ValueError("Search term cannot be empty.")

        results = []
        for task in self.tasks.values():
            if task_term.lower() in task["name"].lower() or task_term.lower() in task[
                "description"
            ].lower():
                results.append(task)
        return results

    def finish(self, task_id: int) -> bool:
        """
        Marks a task as completed.

        Args:
            task_id: The ID of the task to finish.

        Returns:
            True if the task was successfully marked as finished,
            False otherwise (e.g., task not found).

        Raises:
            TypeError: If task_id is not an integer.
            ValueError: If task_id is not positive.

        """

        if not isinstance(task_id, int):
            raise TypeError("Task ID must be an integer.")
        if task_id <= 0:
            raise ValueError("Task ID must be a positive integer.")


        if task_id in self.tasks:
            self.tasks[task_id]["is_finished"] = True
            return True
        else:
            return False  # Task not found

    def get_all(self) -> list[dict]:
        """
        Retrieves all tasks in the to-do list.

        Returns:
            A list of all tasks, with each task represented as a dictionary.
            Returns an empty list if there are no tasks.
        """
        return list(self.tasks.values())

    def clear_all(self) -> bool:
        """
        Deletes all tasks from the to-do list.

        Returns:
            Always returns True, indicating successful deletion.
        """
        self.tasks.clear()  # Efficiently removes all items from the dictionary.
        return True


def main():
    """
    Main function to run the console-based to-do list application.
    Provides a simple command-line interface for interacting with the
    TaskManager.
    """

    task_manager = TaskManager()

    while True:
        print("\nTo-Do List Application")
        print("1. Add Task")
        print("2. Remove Task")
        print("3. Search Tasks")
        print("4. Finish Task")
        print("5. Get All Tasks")
        print("6. Clear All Tasks")
        print("7. Exit")

        choice = input("Enter your choice: ")

        try:
            if choice == "1":
                task_name = input("Enter task name: ")
                task_description = input("Enter task description: ")
                task_id = task_manager.add(task_name, task_description)
                print(f"Task added with ID: {task_id}")

            elif choice == "2":
                task_id = int(input("Enter task ID to remove: "))
                if task_manager.remove(task_id):
                    print("Task removed successfully.")
                else:
                    print("Task not found.")

            elif choice == "3":
                task_term = input("Enter search term: ")
                results = task_manager.search(task_term)
                if results:
                    print("Search Results:")
                    for task in results:
                        print(
                            f"  ID: {task['id']}, Name: {task['name']}, Description: {task['description']}, Finished: {task['is_finished']}"
                        )
                else:
                    print("No tasks found matching your search term.")

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
                print("Exiting application.")
                break

            else:
                print("Invalid choice. Please try again.")

        except ValueError as ve:
            print(f"Error: {ve}")
        except TypeError as te:
            print(f"Error: {te}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()

