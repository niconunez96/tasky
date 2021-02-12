from typing import List
from tasky_app.domain.task import Task
from tasky_app.domain.task_repository import TaskRepository


class TaskFinder:

    def __init__(self, repository: TaskRepository):
        self.repository = repository

    def find_all(self) -> List[Task]:
        return self.repository.find_all()
