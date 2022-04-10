from controller.workouts_controller import WorkoutController


class ListWorkoutCommand:
    def __init__(self, workout_controller: WorkoutController):
        self.workout_controller = workout_controller

    def __call__(self, *args, **kwargs):
        print("Listing all books")
