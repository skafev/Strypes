class Workouts:
    def __init__(self, title, description, author, good_for, id=None):
        self.id = id
        self.title = title
        self.description = description
        self.author = author
        self.good_for = good_for

    def __str__(self):
        return f'{self.id}) {self.title} {self.description}: {self.good_for}'

    def get_formatted_str(self):
        return f'{self.author}, made a {self.title} workout' \
               f', which is {self.description} and is good for {self.good_for}'
