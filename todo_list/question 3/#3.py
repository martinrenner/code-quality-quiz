class TaskManager:
    """
    Manages a to-do list with add, remove, search, finish, get_all, and clear_all functionalities.
    Stores tasks in-memory using a dictionary for efficient lookups.
    """

    def __init__(self):
        self.tasks = {}  # {task_id: [task_id, task_name, task_description, is_finished]}
        self.next_id = 1

    def add(self, task_name: str, task_description: str) -> int:
        """Adds a task and returns its unique ID.

        Args:
            task_name: The name of the task.
            task_description: The description of the task.

        Returns:
            The unique ID of the newly added task.
        Raises:
            ValueError: if task name or description are empty.
        """
        if not task_name or not task_description:
            raise ValueError("Task name and description cannot be empty.")

        task_id = self.next_id
        self.tasks[task_id] = [task_id, task_name, task_description, False]
        self.next_id += 1
        return task_id

    def remove(self, task_id: int) -> bool:
        """Removes a task by ID.

        Args:
            task_id: The ID of the task to remove.

        Returns:
            True if the task was removed successfully, False otherwise.
        """
        if not isinstance(task_id, int) or task_id <= 0:
            raise ValueError("Task ID must be a positive integer.")
        if task_id in self.tasks:
            del self.tasks[task_id]
            return True
        return False

    def search(self, task_term: str) -> list[list]:
        """Searches tasks by name or description.

        Args:
            task_term: The term to search for in task names and descriptions.

        Returns:
            A list of matching tasks, each task details: [id, task_name, task_description, is_finished].
              Returns an empty list if no matches are found.
        """

        if not task_term:
            raise ValueError("Search term cannot be empty.")

        results = []
        for task_details in self.tasks.values():
            if task_term.lower() in task_details[1].lower() or task_term.lower() in task_details[2].lower():
                results.append(task_details)
        return results

    def finish(self, task_id: int) -> bool:
        """Marks a task as completed.

        Args:
            task_id: The ID of the task to finish.

        Returns:
            True if the task was found and marked as finished, False otherwise.
        """
        if not isinstance(task_id, int) or task_id <= 0:
            raise ValueError("Task ID must be a positive integer.")

        if task_id in self.tasks:
            self.tasks[task_id][3] = True
            return True
        return False

    def get_all(self) -> list[list]:
        """Retrieves all tasks.

        Returns:
            A list of all tasks, each task details: [id, task_name, task_description, is_finished].
        """
        return list(self.tasks.values())

    def clear_all(self) -> bool:
        """Deletes all tasks.

        Returns:
            Always returns True, indicating successful clearing.
        """
        self.tasks.clear()
        self.next_id = 1  # Reset the ID counter
        return True


def main():
    """Main function to run the console-based to-do list application."""

    task_manager = TaskManager()

    while True:
        print("\nChoose an action:")
        print("1. Add task")
        print("2. Remove task")
        print("3. Search tasks")
        print("4. Finish task")
        print("5. List all tasks")
        print("6. Clear all tasks")
        print("7. Exit")

        choice = input("> ")

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
                search_term = input("Enter search term: ")
                results = task_manager.search(search_term)
                if results:
                    print("Search Results:")
                    for task_details in results:
                        print(
                            f"  ID: {task_details[0]}, Name: {task_details[1]}, Description: {task_details[2]}, Finished: {task_details[3]}")
                else:
                    print("No tasks found matching your search term.")

            elif choice == "4":
                task_id = int(input("Enter task ID to mark as finished: "))
                if task_manager.finish(task_id):
                    print("Task marked as finished.")
                else:
                    print("Task not found.")

            elif choice == "5":
                all_tasks = task_manager.get_all()
                if all_tasks:
                    print("All Tasks:")
                    for task_details in all_tasks:
                         print(
                            f"  ID: {task_details[0]}, Name: {task_details[1]}, Description: {task_details[2]}, Finished: {task_details[3]}")
                else:
                    print("No tasks in the list.")

            elif choice == "6":
                task_manager.clear_all()
                print("All tasks cleared.")

            elif choice == "7":
                print("Exiting.")
                break

            else:
                print("Invalid choice. Please try again.")

        except ValueError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()

