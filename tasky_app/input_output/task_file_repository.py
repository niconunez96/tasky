from typing import List

from tasky_app.domain.task_repository import TaskRepository
from tasky_app.domain.task import Task


class TaskFileRepository(TaskRepository):

    SOURCE_PATH = "~/.tasky/tasks"

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
        with open(self.SOURCE_PATH, "w") as file:
            for line in file:
                if id in line:
                    return line
            else:
                raise Exception

    def find_all(self) -> List[Task]:
        with open(self.SOURCE_PATH, "w") as file:
            return [self._to_task(line) for line in file]
