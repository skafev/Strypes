from entities.workouts import Workouts
from repository.workout_repository import WorkoutsRepository


class WorkoutService:
    def __init__(self, workout_repo: WorkoutsRepository):
        self._workout_repo = workout_repo

    def add_workout(self, workout: Workouts):
        self._workout_repo.create(workout)
        self._workout_repo.save()

    def get_all_workouts(self):
        return self._workout_repo.find_all()

    def get_all_workouts_by_id(self, id):
        return self._workout_repo.find_by_id(id)

    def reload_workouts(self):
        self._workout_repo.load()
        print(self.get_all_workouts())

    def save_workout(self):
        self._workout_repo.save()
        print("Workout saved successfully.")
