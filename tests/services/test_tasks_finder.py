from typing import List
from mock import Mock
from tasky_app.services.task_finder import TasksFinder
from tasky_app.domain.task import Task


class TestTasksFinder:

    class TaskStubRepository(Mock):

        def find_all(self) -> List[Task]:
            return [
                Task(1, "TODO", "desc", True),
                Task(2, "TODO", "desc", True),
                Task(3, "TODO", "desc", True),
            ]

    def test_should_return_all_tasks(self):
        tasks_finder = TasksFinder(self.TaskStubRepository())

        tasks = tasks_finder.find_all()

        assert 3 == len(tasks)
