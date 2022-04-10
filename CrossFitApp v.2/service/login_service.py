from exception.credentials_exception import CredentialsException
from repository.users_repository import UsersRepository


class LoginService:
    def __init__(self, user_repository: UsersRepository):
        self.user_repository = user_repository
        self._logged_user = None

    def register(self, user):
        created = self.user_repository.create(user)
        self.user_repository.save()
        return created

    def login(self, username, password):
        user = self.user_repository.find_by_username(username)
        if user is not None and user.password == password:
            self._logged_user = user
            return user
        raise CredentialsException("Invalid username or password. Try again.")

    def logout(self):
        self._logged_user = None

    def get_logged_user(self):
        return self._logged_user
