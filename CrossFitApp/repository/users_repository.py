from entities.users import Users
from repository.json_repository import JsonRepository
from util.func_utils import find_first


class UsersRepository(JsonRepository):
    def find_by_username(self, username: str)-> Users | None:
        return find_first(lambda u: u.username == username, self.find_all())