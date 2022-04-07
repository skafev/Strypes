from entities.users import Users
from entities.workouts import Workouts
from repository.id_generator_uuid import IdGeneratorUuid
from repository.users_repository import UsersRepository
from repository.workout_repository import WorkoutsRepository

if __name__ == '__main__':
    # u1 = Users('Gosho', 'Gogata', '123', 'male', 'trainee')
    # u2 = Users('Petko', 'Pekata', '4124', 'male', 'crossfitinstructor')
    # u3 = Users('Mariq', 'Mariika', '5445', 'female', 'admin')
    # users = [u1, u2, u3]

    id_gen = IdGeneratorUuid()
    # users_repo = UsersRepository(id_gen)

    # for u in users:
    #     users_repo.create(u)
    #
    # for u in users_repo.find_all():
    #     print(u.get_formatted_str())
    #
    # workout1 = Workouts('22.2', 'Fast Phase', 'Mariika', 'loosing fat')
    # workout2 = Workouts('22.1', 'Fast Phase', 'Gogata', 'muscle gain')
    # workouts = [workout2, workout1]
    # workouts_repo = WorkoutsRepository(id_gen)
    #
    # for w in workouts:
    #     workouts_repo.create(w)
    #
    # for w in workouts_repo.find_all():
    #     print(w.get_formatted_str())
    userRepo = UsersRepository(id_gen, 'users_db.json')
    u1 = Users('Ivan', 'Vanko', 'alabala', 'male', '1')
    u2 = Users('Ivan2', 'Vanko2', 'alabala2', 'male', '1')
    u3 = Users('Ivan3', 'Vanko3', 'alabala3', 'male', '2')
    userRepo.create(u1)
    userRepo.create(u2)
    userRepo.create(u3)

    userRepo.save()
