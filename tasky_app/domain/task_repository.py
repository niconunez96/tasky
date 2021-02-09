from typing import List
from tasky_app.domain.task import Task


class TaskRepository:

    def save(self, task: Task) -> None:
        raise NotImplementedError

    def find_by_id(self, id: int) -> Task:
        raise NotImplementedError

    def find_all(self) -> List[Task]:
        raise NotImplementedError
