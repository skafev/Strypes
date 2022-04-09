from service.workout_service import WorkoutService


class WorkoutController:
    def __init__(self, service: WorkoutService, view=None):
        self.view = view
        self.service = service

    def get_all_workouts(self):
        return self.service.get_all_workouts()

    def reload_workouts(self):
        return self.service.reload_workouts()

    def save_workout(self):
        return self.service.save_workout()

    def add_workout(self, workout):
        self.service.add_workout(workout)
        self.view.refresh()

    def show_add_workout(self):
        pass