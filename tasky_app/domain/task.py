class Task:

    done = False
    name = ""
    description = ""
    author = ""

    def __init__(self, name, description, author, done):
        self.name = name
        self.description = description
        self.author = author
        self.done = done

    @staticmethod
    def create_new(name: str, author: str):
        return Task(name=name, description="", author=author, done=False)

    @property
    def is_done(self):
        return self.done

    def mark_as_done(self):
        self.done = True

    def mark_as_in_progress(self):
        self.done = False
