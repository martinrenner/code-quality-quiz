import re

class TaskManager:
    def __init__(self):
        self.tasks = {}
        self.next_id = 1

    def add(self, task_name: str, task_description: str) -> int:
        """
        Adds a task and returns its unique ID.

        :param task_name: Name of the task
        :param task_description: Description of the task
        :return: Unique ID of the task
        """
        if not task_name or not task_description:
            raise ValueError("Task name and description cannot be empty.")

        task_id = self.next_id
        self.tasks[task_id] = {
            "id": task_id,
            "task_name": task_name,
            "task_description": task_description,
            "is_finished": False
        }
        self.next_id += 1
        return task_id

    def remove(self, task_id: int) -> bool:
        """
        Removes a task by ID and returns success status.

        :param task_id: ID of the task to be removed
        :return: True if task was removed successfully, False otherwise
        """
        if task_id in self.tasks:
            del self.tasks[task_id]
            return True
        return False

    def search(self, task_term: str) -> list[dict]:
        """
        Searches tasks by name or description and returns matching results.

        :param task_term: Term to search in task name or description
        :return: List of tasks that match the search term
        """
        if not task_term:
            raise ValueError("Search term cannot be empty.")

        results = [task for task in self.tasks.values() if re.search(task_term, task["task_name"], re.IGNORECASE) or re.search(task_term, task["task_description"], re.IGNORECASE)]
        return results

    def finish(self, task_id: int) -> bool:
        """
        Marks a task as completed.

        :param task_id: ID of the task to be marked as completed
        :return: True if task was marked as completed successfully, False otherwise
        """
        if task_id in self.tasks:
            self.tasks[task_id]["is_finished"] = True
            return True
        return False

    def get_all(self) -> list[dict]:
        """
        Retrieves all tasks with their details.

        :return: List of all tasks
        """
        return list(self.tasks.values())

    def clear_all(self) -> bool:
        """
        Deletes all tasks and returns success status.

        :return: True if all tasks were deleted successfully
        """
        self.tasks.clear()
        self.next_id = 1
        return True

def main():
    task_manager = TaskManager()

    while True:
        print("\n1. Add Task")
        print("2. Remove Task")
        print("3. Search Tasks")
        print("4. Mark Task as Finished")
        print("5. Get All Tasks")
        print("6. Clear All Tasks")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            task_name = input("Enter task name: ")
            task_description = input("Enter task description: ")
            try:
                task_id = task_manager.add(task_name, task_description)
                print(f"Task added with ID: {task_id}")
            except ValueError as e:
                print(e)

        elif choice == '2':
            task_id = int(input("Enter task ID to remove: "))
            if task_manager.remove(task_id):
                print("Task removed successfully.")
            else:
                print("Task not found.")

        elif choice == '3':
            task_term = input("Enter search term: ")
            try:
                results = task_manager.search(task_term)
                for task in results:
                    print(task)
            except ValueError as e:
                print(e)

        elif choice == '4':
            task_id = int(input("Enter task ID to mark as finished: "))
            if task_manager.finish(task_id):
                print("Task marked as finished successfully.")
            else:
                print("Task not found.")

        elif choice == '5':
            tasks = task_manager.get_all()
            for task in tasks:
                print(task)

        elif choice == '6':
            if task_manager.clear_all():
                print("All tasks cleared successfully.")

        elif choice == '7':
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
