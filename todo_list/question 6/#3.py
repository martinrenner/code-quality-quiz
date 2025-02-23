
#!/usr/bin/env python3

class TaskManager:
    """
    TaskManager class manages the todo tasks.
    
    Supported operations:
      - add(task_name: str, task_description: str) -> int
      - remove(task_id: int) -> bool
      - search(task_term: str) -> list[dict]
      - finish(task_id: int) -> bool
      - get_all() -> list[dict]
      - clear_all() -> bool

    Each task is a dictionary with keys: (id, task_name, task_description, is_finished)
    """
    def __init__(self):
        """Initializes the TaskManager with an empty task store and a unique ID counter."""
        self.tasks = {}      # Stores tasks using task_id as key
        self.next_id = 1     # A counter to assign unique IDs to tasks

    def add(self, task_name: str, task_description: str) -> int:
        """
        Adds a new task and returns its unique ID.
        
        :param task_name: Name of the task. Must not be empty.
        :param task_description: Detailed description of the task. Must not be empty.
        :return: The unique ID of the added task.
        :raises ValueError: If task_name or task_description is empty.
        """
        if not task_name or not task_name.strip():
            raise ValueError("Task name cannot be empty.")
        if not task_description or not task_description.strip():
            raise ValueError("Task description cannot be empty.")

        task_id = self.next_id
        self.tasks[task_id] = {
            'id': task_id,
            'task_name': task_name.strip(),
            'task_description': task_description.strip(),
            'is_finished': False
        }
        self.next_id += 1
        return task_id

    def remove(self, task_id: int) -> bool:
        """
        Removes a task by its unique ID.
        
        :param task_id: The ID of the task to remove. Must be a positive integer.
        :return: True if the task was removed; False if the task does not exist.
        """
        if not isinstance(task_id, int) or task_id < 1:
            return False
        if task_id not in self.tasks:
            return False
        del self.tasks[task_id]
        return True

    def search(self, task_term: str) -> list:
        """
        Searches for tasks by checking if the search term is contained in
        the task's name or description (case-insensitive).
        
        :param task_term: The term to search for; returns an empty list if blank.
        :return: A list of task dictionaries matching the search term.
        """
        if not task_term or not task_term.strip():
            return []
        term = task_term.strip().lower()
        results = []
        for task in self.tasks.values():
            if term in task['task_name'].lower() or term in task['task_description'].lower():
                results.append(task)
        return results

    def finish(self, task_id: int) -> bool:
        """
        Marks the task with the specified ID as finished.
        
        :param task_id: The unique ID of the task to mark as finished.
        :return: True if the task was found and marked; False otherwise.
        """
        if task_id in self.tasks:
            self.tasks[task_id]['is_finished'] = True
            return True
        return False

    def get_all(self) -> list:
        """
        Retrieves all tasks currently stored.
        
        :return: A list of all task dictionaries.
        """
        return list(self.tasks.values())

    def clear_all(self) -> bool:
        """
        Deletes all tasks from the manager.
        
        :return: True after all tasks have been cleared.
        """
        self.tasks.clear()
        self.next_id = 1  # Reset the counter for reuse
        return True


def print_task(task: dict):
    """
    Helper function to print task details in a friendly format.
    
    :param task: A task dictionary.
    """
    status = "Finished" if task["is_finished"] else "Pending"
    print(f'ID: {task["id"]} | Name: {task["task_name"]} | Description: {task["task_description"]} | Status: {status}')


def display_menu():
    """
    Displays the available commands to the user.
    """
    print("\nTodo List Manager")
    print("-" * 20)
    print("Commands:")
    print("1. add       - Add a new task")
    print("2. remove    - Remove a task by ID")
    print("3. search    - Search tasks by term")
    print("4. finish    - Mark a task as finished")
    print("5. get_all   - Display all tasks")
    print("6. clear_all - Clear all tasks")
    print("7. exit      - Exit the application")


def main():
    """
    Main function to run the interactive console-based todo list application.
    """
    task_manager = TaskManager()
    while True:
        display_menu()
        command = input("Enter command: ").strip().lower()
        
        if command in ['add', '1']:
            task_name = input("Enter task name: ").strip()
            task_desc = input("Enter task description: ").strip()
            try:
                task_id = task_manager.add(task_name, task_desc)
                print(f"Task added successfully with ID: {task_id}")
            except ValueError as error:
                print(f"Error adding task: {error}")

        elif command in ['remove', '2']:
            task_id_input = input("Enter task ID to remove: ").strip()
            try:
                task_id = int(task_id_input)
                if task_manager.remove(task_id):
                    print(f"Task with ID {task_id} removed successfully.")
                else:
                    print(f"Task with ID {task_id} could not be found or is invalid.")
            except ValueError:
                print("Invalid input. Please enter a valid integer for the task ID.")

        elif command in ['search', '3']:
            search_term = input("Enter search term: ").strip()
            results = task_manager.search(search_term)
            if results:
                print("Search results:")
                for task in results:
                    print_task(task)
            else:
                print("No tasks match the search criteria.")

        elif command in ['finish', '4']:
            task_id_input = input("Enter task ID to mark as finished: ").strip()
            try:
                task_id = int(task_id_input)
                if task_manager.finish(task_id):
                    print(f"Task with ID {task_id} marked as finished.")
                else:
                    print(f"Task with ID {task_id} not found or invalid.")
            except ValueError:
                print("Invalid input. Please enter a valid integer for the task ID.")

        elif command in ['get_all', '5']:
            all_tasks = task_manager.get_all()
            if all_tasks:
                print("Current tasks:")
                for task in all_tasks:
                    print_task(task)
            else:
                print("No tasks found.")

        elif command in ['clear_all', '6']:
            confirmation = input("Are you sure you want to clear all tasks? (yes/no): ").strip().lower()
            if confirmation == 'yes':
                task_manager.clear_all()
                print("All tasks have been cleared.")
            else:
                print("Clear operation cancelled.")

        elif command in ['exit', '7']:
            print("Exiting Todo List Manager. Goodbye!")
            break

        else:
            print("Invalid command. Please try again.")

if __name__ == "__main__":
    main()
