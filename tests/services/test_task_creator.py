from typing import List
from mock import Mock
from tasky_app.services.task_creator import TaskCreator
from tasky_app.domain.task import Task


class TestTaskCreator:

    class TaskStubRepository(Mock):

        def __init__(self, *arg):
            super().__init__(arg)
            self.tasks = []

        def save(self, task: Task):
            self.tasks.append(task)

        def find_all(self) -> List[Task]:
            return self.tasks

    def test_should_create_task(self):
        repository = self.TaskStubRepository()
        task_creator = TaskCreator(repository)

        task_creator.create("New task")

        task_created = repository.tasks[0]
        assert 1 == task_created.id
        assert "New task" == task_created.name

    def test_should_create_task_with_done_as_false(self):
        repository = self.TaskStubRepository()
        task_creator = TaskCreator(repository)

        task_creator.create("New task")

        task_created = repository.tasks[0]
        assert not task_created.is_done

    def test_should_create_task_with_id_greater_by_one_than_the_last_task(
        self,
    ):
        repository = self.TaskStubRepository()
        repository.save(Task(1, "bla", "desc", True))
        repository.save(Task(2, "bla", "desc", True))
        repository.save(Task(3, "bla", "desc", True))
        task_creator = TaskCreator(repository)

        task_creator.create("New task")

        task_created = repository.tasks[-1]
        assert 4 == task_created.id
