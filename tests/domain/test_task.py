from tasky_app.domain.task import Task


class TestTask:

    def test_create_new_task_set_done_false_as_default(self):
        new_task = Task.create_new(1, "TODO")

        assert not new_task.is_done

    def test_mark_as_done_should_set_task_to_done_true(self):
        new_task = Task.create_new(1, "TODO")

        new_task.mark_as_done()

        assert new_task.is_done

    def test_mark_as_in_progress_should_set_task_to_done_false(self):
        task = Task(1, "TODO", "asd", True)

        task.mark_as_in_progress()

        assert not task.is_done
