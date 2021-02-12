#!./env/bin/python

from tasky_app.cli.tasky_entrypoint import parser
from tasky_app.input_output.task_file_repository import TaskFileRepository
from tasky_app.domain.task import Task
from tasky_app.services.task_finder import TaskFinder


def display_task(task: Task):
    icon = "✔️" if task.is_done else "❌"
    print("{}_  {}: {} -- {}".format(
        task.id,
        task.name,
        task.description,
        icon,
    ))


if __name__ == "__main__":
    arguments = parser.parse_args()
    if arguments.list:
        tasks = TaskFinder(TaskFileRepository()).find_all()
        for task in tasks:
            display_task(task)
