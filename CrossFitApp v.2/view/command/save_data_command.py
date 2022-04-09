from controller.workouts_controller import WorkoutController


class LoadDataCommand:
    def __int__(self, workout_controller : WorkoutController):
        self.workout_controller = workout_controller

    def __call__(self, *args, **kwargs):
        self.workout_controller.save_workout()
