
class TaskManager:
    """
    Manages a list of to-do tasks.  This class provides functionality to
    add, remove, search, finish, retrieve, and clear tasks.  It uses an
    in-memory list for task storage.
    """

    def __init__(self):
        """
        Initializes the TaskManager with an empty task list and sets the
        initial task ID to 1.
        """
        self.tasks = []
        self.next_task_id = 1

    def add(self, task_name: str, task_description: str) -> int:
        """
        Adds a new task to the to-do list.

        Args:
            task_name: The name of the task (must not be empty).
            task_description: A description of the task.

        Returns:
            The unique ID assigned to the newly added task.

        Raises:
            ValueError: If task_name is empty.
        """
        if not task_name.strip():
            raise ValueError("Task name cannot be empty.")

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
            task_id: The ID of the task to remove.

        Returns:
            True if the task was successfully removed, False otherwise.

        Raises:
            TypeError: if task_id is not an integer
            ValueError: If task_id is not positive.
        """

        if not type(task_id) is int:
            raise TypeError("Task ID must be an integer")
        if task_id <= 0:
            raise ValueError("Task ID must be a positive integer.")

        for i, task in enumerate(self.tasks):
            if task["id"] == task_id:
                del self.tasks[i]
                return True
        return False  # Task not found

    def search(self, task_term: str) -> list[dict]:
        """
        Searches for tasks by name or description.

        Args:
            task_term: The search term (can be part of the name or description).

        Returns:
            A list of tasks that match the search term.  Returns an empty list
            if no matches are found.
        """
        if not task_term.strip():
            return []  # Return empty list for empty search term

        results = []
        for task in self.tasks:
            if task_term.lower() in task["name"].lower() or task_term.lower() in task["description"].lower():
                results.append(task)
        return results

    def finish(self, task_id: int) -> bool:
        """
        Marks a task as completed.

        Args:
            task_id: The ID of the task to finish.

        Returns:
            True if the task was found and marked as finished, False otherwise.

        Raises:
            TypeError: if task_id is not an integer
            ValueError: If task_id is not positive.
        """
        if not type(task_id) is int:
            raise TypeError("Task ID must be an integer")
        if task_id <= 0:
            raise ValueError("Task ID must be a positive integer.")

        for task in self.tasks:
            if task["id"] == task_id:
                task["is_finished"] = True
                return True
        return False  # Task not found

    def get_all(self) -> list[dict]:
        """
        Retrieves all tasks in the to-do list.

        Returns:
            A list of all tasks, including their details. Returns an empty list if
            no tasks exist.
        """
        return self.tasks

    def clear_all(self) -> bool:
        """
        Deletes all tasks from the to-do list.

        Returns:
            Always returns True, indicating that the list has been cleared.
        """
        self.tasks = []
        return True


def main():
    """
    Main function to run the console-based to-do list application.
    Provides a simple command-line interface for interacting with the
    TaskManager.
    """
    task_manager = TaskManager()

    while True:
        print("\nChoose an action:")
        print("1. Add task")
        print("2. Remove task")
        print("3. Search tasks")
        print("4. Finish task")
        print("5. Get all tasks")
        print("6. Clear all tasks")
        print("7. Exit")

        choice = input("Enter your choice (1-7): ")

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
                    print("Search results:")
                    for task in results:
                        print_task(task)
                else:
                    print("No tasks found matching the search term.")

            elif choice == "4":
                task_id = int(input("Enter task ID to finish: "))
                if task_manager.finish(task_id):
                    print("Task marked as finished.")
                else:
                    print("Task not found.")

            elif choice == "5":
                tasks = task_manager.get_all()
                if tasks:
                    print("All tasks:")
                    for task in tasks:
                        print_task(task)
                else:
                    print("No tasks in the list.")

            elif choice == "6":
                task_manager.clear_all()
                print("All tasks cleared.")

            elif choice == "7":
                print("Exiting...")
                break

            else:
                print("Invalid choice. Please enter a number between 1 and 7.")

        except ValueError as e:
            print(f"Error: {e}")
        except TypeError as e:
            print(f"Error: {e}")


def print_task(task: dict):
    status = "Finished" if task["is_finished"] else "Not Finished"
    print(f"  ID: {task['id']}, Name: {task['name']}, Description: {task['description']}, Status: {status}")


if __name__ == "__main__":
    main()


import unittest
# from your_module import TaskManager  # Assuming your code is in 'your_module.py'

class TestTaskManager(unittest.TestCase):

    def setUp(self):
        self.task_manager = TaskManager()

    def test_add_task(self):
        task_id = self.task_manager.add("Grocery Shopping", "Buy milk and eggs")
        self.assertEqual(task_id, 1)
        self.assertEqual(len(self.task_manager.tasks), 1)
        self.assertEqual(self.task_manager.tasks[0]["name"], "Grocery Shopping")

    def test_add_empty_task_name(self):
        with self.assertRaises(ValueError):
            self.task_manager.add("", "Description")

    def test_remove_task(self):
        task_id = self.task_manager.add("Grocery Shopping", "Buy milk and eggs")
        result = self.task_manager.remove(task_id)
        self.assertTrue(result)
        self.assertEqual(len(self.task_manager.tasks), 0)

    def test_remove_nonexistent_task(self):
        result = self.task_manager.remove(999)  # Non-existent ID
        self.assertFalse(result)

    def test_remove_negative_task_id(self):
        with self.assertRaises(ValueError):
            self.task_manager.remove(-1)

    def test_remove_not_int_task_id(self):
        with self.assertRaises(TypeError):
            self.task_manager.remove("abc")

    def test_search_tasks(self):
        self.task_manager.add("Grocery Shopping", "Buy milk and eggs")
        self.task_manager.add("Book Appointment", "Dentist appointment")
        results = self.task_manager.search("grocery")
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0]["name"], "Grocery Shopping")

        results = self.task_manager.search("appointment")
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0]["description"], "Dentist appointment")

    def test_search_empty_term(self):
        results = self.task_manager.search("")
        self.assertEqual(len(results), 0)
        results = self.task_manager.search("   ")
        self.assertEqual(len(results), 0)


    def test_finish_task(self):
        task_id = self.task_manager.add("Grocery Shopping", "Buy milk")
        result = self.task_manager.finish(task_id)
        self.assertTrue(result)
        self.assertTrue(self.task_manager.tasks[0]["is_finished"])

    def test_finish_nonexistent_task(self):
        result = self.task_manager.finish(999)
        self.assertFalse(result)

    def test_finish_negative_task_id(self):
        with self.assertRaises(ValueError):
            self.task_manager.finish(-1)

    def test_finish_not_int_task_id(self):
        with self.assertRaises(TypeError):
            self.task_manager.finish("abc")

    def test_get_all_tasks(self):
        self.task_manager.add("Task 1", "Description 1")
        self.task_manager.add("Task 2", "Description 2")
        tasks = self.task_manager.get_all()
        self.assertEqual(len(tasks), 2)

    def test_get_all_empty(self):
        tasks = self.task_manager.get_all()
        self.assertEqual(len(tasks), 0)

    def test_clear_all_tasks(self):
        self.task_manager.add("Task 1", "Description 1")
        result = self.task_manager.clear_all()
        self.assertTrue(result)
        self.assertEqual(len(self.task_manager.tasks), 0)

if __name__ == '__main__':
    unittest.main()
