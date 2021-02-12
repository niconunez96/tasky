from typing import List

from tasky_app.domain.task_repository import TaskRepository
from tasky_app.domain.task import Task
from tasky_app.domain.exceptions import TaskNotFound


class TaskFileRepository(TaskRepository):

    SOURCE_PATH = ""

    def __init__(self, source_path: str):
        self.SOURCE_PATH = source_path or "tasky_app/db/tasks_db"

    def _to_task(self, line: str) -> Task:
        name = ""
        author = ""
        done = False
        description = ""
        return Task.create(name, author, description, done)

    def save(self, task: Task) -> None:
        with open(self.SOURCE_PATH, "w") as file:
            pass

    def find_by_id(self, id: int) -> Task:
        with open(self.SOURCE_PATH) as file:
            for line in file:
                if id in line:
                    return line
            else:
                raise TaskNotFound

    def find_all(self) -> List[Task]:
        with open(self.SOURCE_PATH) as file:
            return [self._to_task(line) for line in file]
