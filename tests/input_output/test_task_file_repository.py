import pytest
from tasky_app.domain.task import Task
from tasky_app.domain.exceptions import TaskNotFound
from tasky_app.input_output.task_file_repository import TaskFileRepository


class TestTaskFileRepository:

    @pytest.fixture(scope="function", autouse=True)
    def recreate_tasks_db_file(self):
        import os
        os.remove("tests/db/test_tasks_db")
        file = open("tests/db/test_tasks_db", "w")
        file.close()

    @pytest.fixture
    def file_path_test(self):
        return "tests/db/test_tasks_db"

    def test_should_append_task_into_file_when_save_task(self, file_path_test):
        task1 = Task(1, "TODO", "asd", "doe", True)
        task2 = Task(2, "Another task", "asd", "doe", False)

        repository = TaskFileRepository(file_path_test)

        repository.save(task1)
        repository.save(task2)

        with open(file_path_test) as test_file:
            tasks = [line for line in test_file]

        assert tasks[0] == "1, TODO, asd, doe, True\n"
        assert tasks[1] == "2, Another task, asd, doe, False\n"

    def test_should_find_task_with_specified_id(self, file_path_test):
        task1 = Task(1, "TODO", "asd", "doe", True)
        task2 = Task(2, "Another task", "asd", "doe", False)
        repository = TaskFileRepository(file_path_test)
        repository.save(task1)
        repository.save(task2)

        task_fetched = repository.find_by_id(2)

        assert task_fetched.name == "Another task"
        assert task_fetched.description == "asd"
        assert task_fetched.author == "doe"
        assert not task_fetched.is_done

    def test_should_raise_task_not_found_when_id_specified_does_not_exist(
        self,
        file_path_test,
    ):
        repository = TaskFileRepository(file_path_test)

        with pytest.raises(TaskNotFound):
            repository.find_by_id(1)

    def test_should_return_all_tasks_from_file(self, file_path_test):
        task1 = Task(1, "TODO", "asd", "doe", True)
        task2 = Task(2, "Another task", "asd", "doe", False)
        task3 = Task(3, "One more task", "asd", "doe", True)

        repository = TaskFileRepository(file_path_test)
        repository.save(task1)
        repository.save(task2)
        repository.save(task3)

        task_fetched = repository.find_all()

        assert 3 == len(task_fetched)
