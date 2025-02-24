class TaskManager:
    """
    Manages a to-do list with functionalities to add, remove, search,
    finish, get all, and clear all tasks.  Implements ISO/IEC 25010
    quality characteristics.

    Attributes:
        tasks (dict):  A dictionary storing tasks.  Keys are task IDs (int),
                      and values are dictionaries containing task details.
        next_id (int):  The next available ID for a new task.
    """

    def __init__(self):
        """
        Initializes an empty task list and sets the starting task ID.
        """
        self.tasks = {}
        self.next_id = 1

    def add(self, task_name: str, task_description: str) -> int:
        """
        Adds a new task to the to-do list.

        Args:
            task_name (str): The name of the task.
            task_description (str): The description of the task.

        Returns:
            int: The unique ID assigned to the newly added task.

        Raises:
            ValueError: If task_name or task_description is empty.
        """
        if not task_name.strip():
            raise ValueError("Task name cannot be empty.")
        if not task_description.strip():
            raise ValueError("Task description cannot be empty.")

        task_id = self.next_id
        self.tasks[task_id] = {
            'id': task_id,
            'name': task_name,
            'description': task_description,
            'is_finished': False
        }
        self.next_id += 1
        return task_id

    def remove(self, task_id: int) -> bool:
        """
        Removes a task from the to-do list by its ID.

        Args:
            task_id (int): The ID of the task to be removed.

        Returns:
            bool: True if the task was successfully removed, False otherwise.

        Raises:
            TypeError: If task_id is not an integer.
            ValueError: If task_id is not positive
        """
        if not isinstance(task_id, int):
            raise TypeError("Task ID must be an integer.")
        if task_id <= 0:
            raise ValueError("Task ID must be a positive integer.")

        if task_id in self.tasks:
            del self.tasks[task_id]
            return True
        else:
            return False

    def search(self, task_term: str) -> list[dict]:
        """
        Searches for tasks by name or description.

        Args:
            task_term (str): The search term (can be part of a name or description).

        Returns:
            list[dict]: A list of tasks (dictionaries) that match the search term.
                         Returns an empty list if no matches are found.
        Raises:
            ValueError: If task_term is empty.
        """
        if not task_term.strip():
            raise ValueError("Search term cannot be empty.")

        results = []
        for task in self.tasks.values():
            if task_term.lower() in task['name'].lower() or task_term.lower() in task['description'].lower():
                results.append(task)
        return results

    def finish(self, task_id: int) -> bool:
        """
        Marks a task as completed.

        Args:
            task_id (int): The ID of the task to be finished.

        Returns:
            bool: True if the task was found and marked as finished,
                  False otherwise.

        Raises:
            TypeError: If task_id is not an integer.
            ValueError: If task_id is not positive
        """
        if not isinstance(task_id, int):
            raise TypeError("Task ID must be an integer.")
        if task_id <= 0:
            raise ValueError("Task ID must be a positive integer.")


        if task_id in self.tasks:
            self.tasks[task_id]['is_finished'] = True
            return True
        else:
            return False

    def get_all(self) -> list[dict]:
        """
        Retrieves all tasks in the to-do list.

        Returns:
            list[dict]: A list of all tasks (dictionaries),
                        or an empty list if there are no tasks.
        """
        return list(self.tasks.values())

    def clear_all(self) -> bool:
        """
        Deletes all tasks from the to-do list.

        Returns:
            bool: True, indicating that list was cleared successfully.
        """
        self.tasks.clear()
        return True



def main():
    """
    Main function to run the console-based to-do list application.
    Provides a simple text-based interface for user interaction.
    """
    task_manager = TaskManager()

    while True:
        print("\nTo-Do List Menu:")
        print("1. Add Task")
        print("2. Remove Task")
        print("3. Search Tasks")
        print("4. Finish Task")
        print("5. Get All Tasks")
        print("6. Clear All Tasks")
        print("7. Exit")

        choice = input("Enter your choice: ")

        try:
            if choice == '1':
                name = input("Enter task name: ")
                description = input("Enter task description: ")
                task_id = task_manager.add(name, description)
                print(f"Task added with ID: {task_id}")

            elif choice == '2':
                task_id = int(input("Enter task ID to remove: "))
                if task_manager.remove(task_id):
                    print("Task removed successfully.")
                else:
                    print("Task not found.")

            elif choice == '3':
                term = input("Enter search term: ")
                results = task_manager.search(term)
                if results:
                    print("Search Results:")
                    for task in results:
                        print(task)
                else:
                    print("No tasks found matching the search term.")

            elif choice == '4':
                task_id = int(input("Enter task ID to mark as finished: "))
                if task_manager.finish(task_id):
                    print("Task marked as finished.")
                else:
                    print("Task not found.")

            elif choice == '5':
                tasks = task_manager.get_all()
                if tasks:
                    print("All Tasks:")
                    for task in tasks:
                        print(task)
                else:
                    print("No tasks in the list.")

            elif choice == '6':
                task_manager.clear_all()
                print("All tasks cleared.")

            elif choice == '7':
                print("Exiting...")
                break

            else:
                print("Invalid choice. Please try again.")

        except ValueError as e:
            print(f"Error: {e}")
        except TypeError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
