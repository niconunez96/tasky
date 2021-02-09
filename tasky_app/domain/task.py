class Task:

    done = False
    name = ""
    description = ""
    author = ""

    def create(self, name: str, description: str, author: str, done: bool):
        self.name = name
        self.description = description
        self.author = author
        self.done = done

    def create_new(self, name: str, description: str, author: str):
        self.done = False
        self.name = name
        self.author = author

    def is_done(self):
        return self.done

    def mark_as_done(self):
        self.done = True

    def mark_as_in_progress(self):
        self.done = False
