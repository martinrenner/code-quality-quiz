
class TaskManager:
    def __init__(self):
        """Initialize the TaskManager with an empty task list and a task ID counter."""
        self.tasks = []
        self.next_id = 1

    def add(self, task_name: str, task_description: str) -> int:
        """
        Adds a task and returns its unique ID.

        Parameters:
        task_name (str): The name of the task.
        task_description (str): The description of the task.

        Returns:
        int: The unique ID of the task.
        """
        if not task_name or not task_description:
            raise ValueError("Task name and description must not be empty.")

        task = {
            "id": self.next_id,
            "task_name": task_name,
            "task_description": task_description,
            "is_finished": False
        }
        self.tasks.append(task)
        self.next_id += 1
        return task["id"]

    def remove(self, task_id: int) -> bool:
        """
        Removes a task by ID and returns success status.

        Parameters:
        task_id (int): The ID of the task to remove.

        Returns:
        bool: True if the task was successfully removed, False otherwise.
        """
        if task_id <= 0:
            raise ValueError("Task ID must be a positive integer.")

        for task in self.tasks:
            if task["id"] == task_id:
                self.tasks.remove(task)
                return True
        return False

    def search(self, task_term: str) -> list[dict]:
        """
        Searches tasks by name or description and returns matching results.

        Parameters:
        task_term (str): The term to search for in task names or descriptions.

        Returns:
        list[dict]: A list of tasks that match the search term.
        """
        if not task_term:
            raise ValueError("Search term must not be empty.")

        return [task for task in self.tasks if task_term in task["task_name"] or task_term in task["task_description"]]

    def finish(self, task_id: int) -> bool:
        """
        Marks a task as completed.

        Parameters:
        task_id (int): The ID of the task to mark as completed.

        Returns:
        bool: True if the task was successfully marked as completed, False otherwise.
        """
        if task_id <= 0:
            raise ValueError("Task ID must be a positive integer.")

        for task in self.tasks:
            if task["id"] == task_id:
                task["is_finished"] = True
                return True
        return False

    def get_all(self) -> list[dict]:
        """
        Retrieves all tasks with their details.

        Returns:
        list[dict]: A list of all tasks.
        """
        return self.tasks

    def clear_all(self) -> bool:
        """
        Deletes all tasks and returns success status.

        Returns:
        bool: True if all tasks were successfully deleted.
        """
        self.tasks = []
        self.next_id = 1
        return True

def main():
    task_manager = TaskManager()

    while True:
        print("\nTodo List Menu:")
        print("1. Add Task")
        print("2. Remove Task")
        print("3. Search Tasks")
        print("4. Mark Task as Finished")
        print("5. Get All Tasks")
        print("6. Clear All Tasks")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            task_name = input("Enter task name: ")
            task_description = input("Enter task description: ")
            try:
                task_id = task_manager.add(task_name, task_description)
                print(f"Task added with ID: {task_id}")
            except ValueError as e:
                print(e)

        elif choice == "2":
            task_id = int(input("Enter task ID to remove: "))
            try:
                success = task_manager.remove(task_id)
                if success:
                    print("Task removed successfully.")
                else:
                    print("Task not found.")
            except ValueError as e:
                print(e)

        elif choice == "3":
            task_term = input("Enter search term: ")
            try:
                results = task_manager.search(task_term)
                if results:
                    for task in results:
                        print(task)
                else:
                    print("No matching tasks found.")
            except ValueError as e:
                print(e)

        elif choice == "4":
            task_id = int(input("Enter task ID to mark as finished: "))
            try:
                success = task_manager.finish(task_id)
                if success:
                    print("Task marked as finished.")
                else:
                    print("Task not found.")
            except ValueError as e:
                print(e)

        elif choice == "5":
            tasks = task_manager.get_all()
            if tasks:
                for task in tasks:
                    print(task)
            else:
                print("No tasks found.")

        elif choice == "6":
            task_manager.clear_all()
            print("All tasks cleared.")

        elif choice == "7":
            print("Exiting the program.")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
