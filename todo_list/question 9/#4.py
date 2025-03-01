class Task:
    """
    Represents a single to-do list item.
    """
    def __init__(self, task_id: int, task_name: str, task_description: str, is_finished: bool = False):
        """
        Initializes a new Task object.

        Args:
            task_id (int): A unique identifier for the task.
            task_name (str): The name of the task.
            task_description (str): A description of the task.
            is_finished (bool): Whether the task is completed (default: False).
        """
        if not isinstance(task_id, int) or task_id < 0:
            raise ValueError("Task ID must be a non-negative integer.")
        if not task_name.strip():
            raise ValueError("Task name cannot be empty.")
        # Description *can* be empty, so we don't validate that.

        self.id = task_id
        self.task_name = task_name
        self.task_description = task_description
        self.is_finished = is_finished

    def to_dict(self) -> dict:
        """
        Converts the Task object to a dictionary.

        Returns:
            dict: A dictionary representation of the task.
        """
        return {
            "id": self.id,
            "task_name": self.task_name,
            "task_description": self.task_description,
            "is_finished": self.is_finished
        }

    def __str__(self):  #Added for better representation when printing
        status = "Finished" if self.is_finished else "Not Finished"
        return f"ID: {self.id}, Name: {self.task_name}, Description: {self.task_description}, Status: {status}"

    def __repr__(self): #Added for better representation in lists etc.
        return self.__str__()
class TaskManager:
    """
    Manages a collection of tasks in a to-do list.
    """
    def __init__(self):
        """
        Initializes a new TaskManager object.
        """
        self.tasks: dict[int, Task] = {}  # Dictionary to store tasks, keyed by ID
        self.next_id: int = 1  # Counter to generate unique task IDs

    def add(self, task_name: str, task_description: str) -> int:
        """
        Adds a new task to the to-do list.

        Args:
            task_name (str): The name of the task.
            task_description (str): A description of the task.

        Returns:
            int: The unique ID of the newly added task.

        Raises:
            ValueError: If task_name is empty after stripping whitespace.
        """
        try:
            new_task = Task(self.next_id, task_name, task_description)
            self.tasks[self.next_id] = new_task
            self.next_id += 1
            return new_task.id
        except ValueError as e:
            print(f"Error adding task: {e}")
            return -1  # Return -1 to indicate failure


    def remove(self, task_id: int) -> bool:
        """
        Removes a task from the to-do list by its ID.

        Args:
            task_id (int): The ID of the task to remove.

        Returns:
            bool: True if the task was successfully removed, False otherwise.
        """
        if not isinstance(task_id, int) or task_id not in self.tasks:
            print(f"Error: Task with ID {task_id} not found.")
            return False

        del self.tasks[task_id]
        return True

    def search(self, task_term: str) -> list[dict]:
        """
        Searches for tasks by name or description.

        Args:
            task_term (str): The term to search for.

        Returns:
            list[dict]: A list of dictionaries representing matching tasks.  Returns an empty list if no matches are found.
        """
        if not isinstance(task_term, str):
             print("Error: Search term must be a string.")
             return []

        task_term = task_term.lower()
        results = []
        for task in self.tasks.values():
            if task_term in task.task_name.lower() or task_term in task.task_description.lower():
                results.append(task.to_dict())
        return results

    def finish(self, task_id: int) -> bool:
        """
        Marks a task as completed.

        Args:
            task_id (int): The ID of the task to mark as finished.

        Returns:
            bool: True if the task was successfully marked as finished, False otherwise.
        """
        if not isinstance(task_id, int) or task_id not in self.tasks:
            print(f"Error: Task with ID {task_id} not found.")
            return False

        self.tasks[task_id].is_finished = True
        return True

    def get_all(self) -> list[dict]:
        """
        Retrieves all tasks in the to-do list.

        Returns:
            list[dict]: A list of dictionaries representing all tasks.
        """
        return [task.to_dict() for task in self.tasks.values()]
    
    def clear_all(self) -> bool:
        """
        Deletes all tasks in the to-do list
        Returns:
            bool: Returns True after clearing the list.
        """

        self.tasks.clear()
        self.next_id = 1 # Reset next_id
        return True

def main():
    """
    Main function to run the console-based to-do list application.
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
                task_name = input("Enter task name: ")
                task_description = input("Enter task description: ")
                task_id = task_manager.add(task_name, task_description)
                if task_id != -1:
                    print(f"Task added with ID: {task_id}")

            elif choice == '2':
                task_id = int(input("Enter task ID to remove: "))
                if task_manager.remove(task_id):
                    print("Task removed successfully.")

            elif choice == '3':
                search_term = input("Enter search term: ")
                results = task_manager.search(search_term)
                if results:
                    print("Search Results:")
                    for task_data in results:
                        print(task_data)
                else:
                    print("No tasks found matching your search term.")

            elif choice == '4':
                task_id = int(input("Enter task ID to mark as finished: "))
                if task_manager.finish(task_id):
                    print("Task marked as finished.")

            elif choice == '5':
                all_tasks = task_manager.get_all()
                if all_tasks:
                    print("All Tasks:")
                    for task_data in all_tasks:
                       print(task_data)
                else:
                    print("The to-do list is empty.")

            elif choice == '6':
                if task_manager.clear_all():
                    print("All tasks cleared.")
                else:
                    print("Error occurred while attempting to clear all tasks.")
            elif choice == '7':
                print("Exiting...")
                break
            else:
                print("Invalid choice. Please try again.")

        except ValueError:
            print("Invalid input. Please enter a valid number.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
