class Results:
    def __init__(self, workout, score, id=None):
        self.id = id
        self.workout = workout
        self.score = score

    def get_formatted_str(self):
        print(f'{self.id} did {self.workout} for {self.score}')