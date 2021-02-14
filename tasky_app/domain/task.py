class Task:

    def __init__(
        self,
        id: int,
        name: str,
        description: str,
        done: bool
    ):
        self.id = id
        self.name = name
        self.description = description
        self.done = done

    @staticmethod
    def create_new(id: int, name: str):
        return Task(
            id=id,
            name=name,
            description="",
            done=False,
        )

    @property
    def is_done(self):
        return self.done

    def mark_as_done(self):
        self.done = True

    def mark_as_in_progress(self):
        self.done = False
