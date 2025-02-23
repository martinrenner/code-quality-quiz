
class TaskManager:
    """
    Manages a to-do list with add, remove, search, finish, get_all, and clear_all operations.
    """

    def __init__(self):
        """
        Initializes the TaskManager with an empty task list and sets the next available ID to 1.
        """
        self.tasks = {}  # Dictionary to store tasks: {id: {task_data}}
        self.next_id = 1

    def _validate_add_input(self, task_name: str, task_description: str) -> None:
        """
        Validate parameters of add method
        """
        if not isinstance(task_name, str) or not task_name:
            raise ValueError("Task name must be a non-empty string.")
        if not isinstance(task_description, str):
            raise ValueError("Task description must be a string.")
        if len(task_name) > 255:
            raise ValueError("Task name cannot exceed 255 characters.")
        if len(task_description) > 1024:
            raise ValueError("Task description cannot exceed 1024 characters.")

    def _validate_task_id(self, task_id: int) -> None:
        """Validates the task_id, raising an exception if invalid."""
        if not isinstance(task_id, int) or task_id <= 0:
            raise ValueError("Task ID must be a positive integer.")

    def add(self, task_name: str, task_description: str) -> int:
        """
        Adds a new task to the to-do list.

        Args:
            task_name: The name of the task (non-empty string).
            task_description: A description of the task.

        Returns:
            The unique ID assigned to the new task.

        Raises:
            ValueError: If the task name is empty or invalid.
        """

        self._validate_add_input(task_name, task_description)  # Perform input validations

        task_id = self.next_id
        self.tasks[task_id] = {
            "id": task_id,
            "task_name": task_name,
            "task_description": task_description,
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
            ValueError: If the task ID is invalid
        """

        self._validate_task_id(task_id)  # Perform task id validation

        if task_id in self.tasks:
            del self.tasks[task_id]
            return True
        else:
            return False

    def search(self, task_term: str) -> list[dict]:
        """
        Searches for tasks by name or description.

        Args:
            task_term: The search term (case-insensitive).

        Returns:
            A list of matching tasks (dictionaries).  Returns an empty list if no matches are found.
        """
        if not isinstance(task_term, str):
            raise ValueError("Search term must be a string.")

        results = []
        for task_id, task_data in self.tasks.items():
            if (
                task_term.lower() in task_data["task_name"].lower()
                or task_term.lower() in task_data["task_description"].lower()
            ):
                results.append(task_data)
        return results

    def finish(self, task_id: int) -> bool:
        """
        Marks a task as completed.

        Args:
            task_id: The ID of the task to finish.

        Returns:
            True if the task was successfully marked as finished, False otherwise.

        Raises:
            ValueError: If the task ID is invalid
        """

        self._validate_task_id(task_id)  # Perform task id validation

        if task_id in self.tasks:
            self.tasks[task_id]["is_finished"] = True
            return True
        else:
            return False

    def get_all(self) -> list[dict]:
        """
        Retrieves all tasks in the to-do list.

        Returns:
            A list of all tasks (dictionaries).
        """
        return list(self.tasks.values())

    def clear_all(self) -> bool:
        """
        Deletes all tasks from the to-do list.

        Returns:
            Always returns True, indicating success.
        """
        self.tasks.clear()
        self.next_id = 1  # Reset the ID counter
        return True


def main():
    """
    Main function to run the console-based to-do list application.
    """
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
                task_term = input("Enter search term: ")
                results = task_manager.search(task_term)
                if results:
                    print("Search results:")
                    for task in results:
                        print(task)
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
                    print("All tasks:")
                    for task in tasks:
                        print(task)
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


import unittest

class TestTaskManager(unittest.TestCase):

    def test_add_task(self):
        tm = TaskManager()
        task_id = tm.add("Test Task", "This is a test.")
        self.assertEqual(task_id, 1)
        self.assertEqual(len(tm.get_all()), 1)  # Check if task is added to the list

    def test_add_task_empty_name(self):
        tm = TaskManager()
        with self.assertRaises(ValueError):
            tm.add("", "Description")


    def test_remove_task(self):
        tm = TaskManager()
        task_id = tm.add("Test Task", "This is a test.")
        result = tm.remove(task_id)
        self.assertTrue(result)
        self.assertEqual(len(tm.get_all()), 0)

    def test_remove_nonexistent_task(self):
        tm = TaskManager()
        result = tm.remove(999)  # Non-existent ID
        self.assertFalse(result)

    def test_search_task(self):
        tm = TaskManager()
        tm.add("Grocery Shopping", "Buy milk and eggs.")
        tm.add("Book Flight", "Book flight to London.")
        results = tm.search("milk")
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0]["task_name"], "Grocery Shopping")

        results = tm.search("London")
        self.assertEqual(len(results), 1)

        results = tm.search("NonExistent")
        self.assertEqual(len(results), 0)

    def test_finish_task(self):
         tm = TaskManager()
         task_id = tm.add("Test Task", "This is a test.")
         result = tm.finish(task_id)
         self.assertTrue(result)
         self.assertTrue(tm.get_all()[0]["is_finished"])

    def test_finish_nonexistent_task(self):
        tm = TaskManager()
        result = tm.finish(999) # Non-existent ID
        self.assertFalse(result)

    def test_get_all_tasks(self):
        tm = TaskManager()
        tm.add("Task 1", "Description 1")
        tm.add("Task 2", "Description 2")
        tasks = tm.get_all()
        self.assertEqual(len(tasks), 2)

    def test_clear_all_tasks(self):
        tm = TaskManager()
        tm.add("Task 1", "Description 1")
        tm.clear_all()
        self.assertEqual(len(tm.get_all()), 0)

    def test_invalid_task_id_remove(self):
        tm = TaskManager()
        with self.assertRaises(ValueError):
            tm.remove("abc")  # Invalid ID type
        with self.assertRaises(ValueError):
            tm.remove(-1)       # Negative ID

    def test_invalid_task_id_finish(self):
        tm = TaskManager()
        with self.assertRaises(ValueError):
            tm.finish("xyz")  # Invalid ID type
        with self.assertRaises(ValueError):
            tm.finish(0)  # non-positive ID

    def test_search_with_invalid_input(self):
        tm = TaskManager()
        with self.assertRaises(ValueError):
            tm.search(123) #Invalid search term

if __name__ == '__main__':
    unittest.main()
