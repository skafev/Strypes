from entities.workouts import Workouts
from repository.json_repository import JsonRepository


class WorkoutsRepository(JsonRepository):
    def find_by_title(self, title_part: str) -> list[Workouts]:
        title_part_lower = title_part.lower()
        workouts_list = self.find_all()
        results = [workout for workout in workouts_list if title_part_lower in workout.title.lower()]
        return results

    def find_by_author(self, author_part: str) -> list[Workouts]:
        author_part_lower = author_part.lower()
        workouts_list = self.find_all()
        results = []
        for workout in workouts_list:
            for author in workout.authors:
                if author_part_lower in author.lower():
                    results.append(workout)
                    break
        return results
