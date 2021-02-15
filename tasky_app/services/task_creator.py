from tasky_app.domain.task_repository import TaskRepository
from tasky_app.domain.task import Task


class TaskCreator:

    def __init__(self, repository: TaskRepository):
        self.repository = repository

    def _obtain_last_id(self):
        try:
            return int(self.repository.find_all()[-1].id)
        except IndexError:
            return 0

    def create(self, name: str):
        last_id = self._obtain_last_id()
        new_task = Task.create_new(id=last_id + 1, name=name)
        self.repository.save(new_task)
