from controller.workouts_controller import WorkoutController


class AddWorkoutCommand:
    def __init__(self, workout_controller: WorkoutController):
        self.workout_controller = workout_controller

    def __call__(self, workout):
        self.workout_controller.add_workout(workout)
