from controller.workouts_controller import WorkoutController


class ShowAddWorkoutCommand:
    def __init__(self, workout_controller: WorkoutController):
        self.workout_controller = workout_controller

    def __call__(self, *args, **kwargs):
        self.workout_controller.show_add_workout()
