
class Task:
    """
    Represents a single to-do task.
    """
    def __init__(self, task_id: int, task_name: str, task_description: str, is_finished: bool = False):
        """
        Initializes a new Task object.

        :param task_id: Unique identifier for the task.
        :param task_name: The name of the task.
        :param task_description: A description of the task.
        :param is_finished:  Indicates whether the task is completed (default: False).
        :raises ValueError: if task_id is negative, or task_name/task_description are empty
        """
        if task_id < 0:
            raise ValueError("Task ID cannot be negative.")
        if not task_name.strip():
            raise ValueError("Task name cannot be empty.")
        if not task_description.strip():
            raise ValueError("Task description cannot be empty.")

        self.id = task_id
        self.name = task_name
        self.description = task_description
        self.is_finished = is_finished

    def to_dict(self) -> dict:
        """
        Returns a dictionary representation of the task.

        :return: A dictionary containing task details.
        """
        return {
            "id": self.id,
            "task_name": self.name,
            "task_description": self.description,
            "is_finished": self.is_finished,
        }


class TaskManager:
    """
    Manages a collection of to-do tasks.
    """
    def __init__(self):
        """
        Initializes a new TaskManager instance.
        """
        self.tasks = {}  # Dictionary to store tasks, {id: Task}
        self.next_id = 1  # Counter to generate unique task IDs

    def add(self, task_name: str, task_description: str) -> int:
        """
        Adds a new task to the to-do list.

        :param task_name: The name of the task.
        :param task_description: A description of the task.
        :return: The unique ID assigned to the new task.
        :raises ValueError: If task_name or task_description are empty.
        """
        try:
            new_task = Task(self.next_id, task_name, task_description)
            self.tasks[self.next_id] = new_task
            self.next_id += 1
            return new_task.id
        except ValueError as e:
            raise ValueError(f"Failed to add task: {e}")

    def remove(self, task_id: int) -> bool:
        """
        Removes a task from the list by its ID.

        :param task_id: The ID of the task to remove.
        :return: True if the task was successfully removed, False otherwise.
        :raises ValueError: If task_id is negative.
        """
        if task_id < 0:
            raise ValueError("Task ID cannot be negative.")
        if task_id in self.tasks:
            del self.tasks[task_id]
            return True
        return False  # Task not found

    def search(self, task_term: str) -> list[dict]:
        """
        Searches for tasks matching a given term (in name or description).

        :param task_term: The term to search for.
        :return: A list of dictionaries, each representing a matching task.
        :raises ValueError: If task_term is empty.
        """
        if not task_term.strip():
            raise ValueError("Search term cannot be empty.")

        results = []
        for task in self.tasks.values():
            if task_term.lower() in task.name.lower() or task_term.lower() in task.description.lower():
                results.append(task.to_dict())
        return results

    def finish(self, task_id: int) -> bool:
        """
        Marks a task as completed.

        :param task_id: The ID of the task to mark as finished.
        :return: True if the task was found and marked as finished, False otherwise.
        :raises ValueError: If task_id is negative.
        """
        if task_id < 0:
            raise ValueError("Task ID cannot be negative.")

        task = self.tasks.get(task_id)
        if task:
            task.is_finished = True
            return True
        return False  # Task not found

    def get_all(self) -> list[dict]:
        """
        Retrieves all tasks in the list.

        :return: A list of dictionaries, each representing a task.
        """
        return [task.to_dict() for task in self.tasks.values()]

    def clear_all(self) -> bool:
        """
        Deletes all tasks from the list.

        :return: Always returns True, indicating successful clearance.
        """
        self.tasks.clear()
        return True


def main():
    """
    Main function to run the console-based to-do list application.
    """
    task_manager = TaskManager()
    print("Welcome to the To-Do List App!")

    while True:
        print("\nAvailable commands:")
        print("  add <task_name> <task_description>")
        print("  remove <task_id>")
        print("  search <term>")
        print("  finish <task_id>")
        print("  get_all")
        print("  clear_all")
        print("  exit")

        command = input("Enter command: ").strip().split()

        if not command:
            continue

        try:
            if command[0] == "add":
                if len(command) < 3:
                    print("Error: 'add' command requires task name and description.")
                else:
                    task_id = task_manager.add(command[1], " ".join(command[2:]))
                    print(f"Task added with ID: {task_id}")

            elif command[0] == "remove":
                if len(command) < 2:
                    print("Error: 'remove' command requires task ID.")
                else:
                    task_id = int(command[1])
                    if task_manager.remove(task_id):
                        print("Task removed successfully.")
                    else:
                        print("Task not found.")

            elif command[0] == "search":
                if len(command) < 2:
                    print("Error: 'search' command requires a search term.")
                else:
                    results = task_manager.search(command[1])
                    if results:
                        print("Search results:")
                        for task in results:
                            print(task)
                    else:
                        print("No tasks found matching your search term.")

            elif command[0] == "finish":
                if len(command) < 2:
                    print("Error: 'finish' command requires task ID.")
                else:
                    task_id = int(command[1])
                    if task_manager.finish(task_id):
                        print("Task marked as finished.")
                    else:
                        print("Task not found.")

            elif command[0] == "get_all":
                tasks = task_manager.get_all()
                if tasks:
                    print("All tasks:")
                    for task in tasks:
                        print(task)
                else:
                    print("No tasks in the list.")
            elif command[0] == "clear_all":
                task_manager.clear_all()
                print("All tasks cleared.")

            elif command[0] == "exit":
                print("Exiting. Goodbye!")
                break

            else:
                print("Invalid command.")

        except ValueError as e:
            print(f"Error: {e}")
        except IndexError:
            print("Error: Incomplete command. Please check your input.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}") # For unhandled exceptions.

if __name__ == "__main__":
    main()


import unittest

class TestTaskManager(unittest.TestCase):

    def test_add_task(self):
        tm = TaskManager()
        task_id = tm.add("Buy groceries", "Milk, eggs, bread")
        self.assertEqual(task_id, 1)
        self.assertEqual(len(tm.tasks), 1)

    def test_remove_task(self):
        tm = TaskManager()
        task_id = tm.add("Buy groceries", "Milk, eggs, bread")
        result = tm.remove(task_id)
        self.assertTrue(result)
        self.assertEqual(len(tm.tasks), 0)

    # ... add more test methods for other functionalities ...

if __name__ == '__main__':
    unittest.main()
