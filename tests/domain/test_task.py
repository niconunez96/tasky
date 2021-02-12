from tasky_app.domain.task import Task


class TestTask:

    def test_create_new_task_set_done_false_as_default(self):
        new_task = Task.create_new("TODO", "doe")

        assert not new_task.done

    def test_mark_as_done_should_set_task_to_done_true(self):
        new_task = Task.create_new("TODO", "doe")

        new_task.mark_as_done()

        assert new_task.done

    def test_mark_as_in_progress_should_set_task_to_done_false(self):
        task = Task("TODO", "asd", "doe", True)

        task.mark_as_in_progress()

        assert not task.done
