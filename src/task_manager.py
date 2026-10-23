from src.task import Task
from src.file_handler import save_tasks
import src.date_controller as date_controller
from datetime import datetime
from tabulate import tabulate


def add_task(tasks, title, description, due_date):
    """
    Add a new task to the task list.

    Args:
        tasks (list): The list of existing Task objects.
        title (str): The title of the new task.
        description (str): A brief description of the task.
        due_date (str): The due date of the task in 'DD-MM-YYYY' format.

    Returns:
        bool: True if the task is added successfully, False otherwise.

    Raises:
        ValueError: If the due date is not in the correct format.

    Side Effects:
        - Saves the updated task list to a file using `save_tasks`.
    """
    # Prevent duplicate tasks
    if any(task.title == title for task in tasks):
        print("Error: A task with this title already exists.")
        return False

    # Validate due date format
    formated_date = date_controller.format_date(due_date)
    if formated_date is None:
        print("Error: Invalid date format. Use DD-MM-YYYY.")
        return False

    tasks.append(Task(title, description, formated_date))
    save_tasks(tasks)
    return True


def delete_task(tasks, title):
    """
    Delete a task from the task list based on its title.

    Args:
        tasks (list): The list of existing Task objects.
        title (str): The title of the task to be deleted.

    Returns:
        bool: True if the task was found and deleted, False otherwise.

    Side Effects:
        - Saves the updated task list to a file using `save_tasks`.
    """
    for task in tasks:
        if task.title == title:
            tasks.remove(task)
            save_tasks(tasks)
            return True
    return False


def list_tasks(tasks, status=None, check_overdue=True):
    """
    Display tasks in the task list, optionally filtered by status.

    Args:
        tasks (list): The list of existing Task objects.
        status (str, optional): The status to filter tasks
        by (e.g., "pending" or "completed").
        check_overdue (bool, optional): Check if the tasks are overdue

    Returns:
        None

    Side Effects:
        - Prints the list of tasks to the console.
    """
    if check_overdue:
        check_if_overdue(tasks)

    filtered = []
    if not status:
        # If status is not set
        for task in tasks:
            filtered.append(task.to_list())
    else:
        # Filter tasks based on their status
        for task in tasks:
            if task.status == status:
                filtered.append(task.to_list())

    if not filtered:
        print("No tasks found.")
        return
    headers = ["Title", "Description", "Due Date", "Status"]
    print(tabulate(filtered, headers=headers))


def filter_tasks_by_status(tasks, status):
    """
    Filter tasks by their status.

    Args:
        tasks (list): The list of existing Task objects.
        status (str): The status to filter tasks by (e.g., "pending" or "completed").

    Returns:
        list: A list of Task objects that match the specified status.
    """
    return [task for task in tasks if task.status == status]


def check_if_overdue(tasks, today_date=None):
    """
    Checks to see if a pending task is overdue and marks them as overdue

    Args:
        tasks (list): The list of existing Task objects.
        today_date (datetime): Date that would be considered today

    Returns:
        list: A list of Task objects that got set to overdue.

    Side Effects:
        Sets the task's status to overdue
    """
    pending_tasks = filter_tasks_by_status(tasks, "pending")
    overdue_tasks = []
    for task in pending_tasks:
        if date_controller.before_today(task.due_date, today_date=today_date):
            task.status = "overdue"
            overdue_tasks.append(task)
    return overdue_tasks
