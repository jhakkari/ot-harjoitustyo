from repositories.user_repository import user_repository
from entities.user import User

class UsernameAlreadyExistsError(Exception):
    pass

class PasswordsDoNotMatchError(Exception):
    pass

class IncorrectInputError(Exception):
    pass

class InvalidUserError(Exception):
    pass

class IncorrectCredentialsError(Exception):
    pass


class UserService:

    def __init__(self):
        self._user_repository = user_repository
        self._user = None
        self._logged_in = False

    def register(self, username, password, password_confirmation):
        if self._user_repository.check_existing(username):
            raise UsernameAlreadyExistsError(f"Username {username} already exists")

        if password != password_confirmation:
            raise PasswordsDoNotMatchError("Passwords do not match. Try again.")

        if len(username) < 1 or len(password) < 1:
            raise IncorrectInputError("Please fill all the fields.")

        if len(username) > 20 or len(password) > 20:
            raise IncorrectInputError("Username or password too long.")

        self._user_repository.create(username, password)
        self.login(username, password)

    def login(self, username, password):
        if len(username) < 1 or len(password) < 1:
            raise IncorrectInputError("Please fill all the fields.")

        user = self._user_repository.get_user(username)
        if user is None:
            raise InvalidUserError("User doesn't exist. Create new one.")

        if user[2] != password:
            raise IncorrectCredentialsError("Wrong username or password")

        self._user = User(user[0], user[1], user[2])
        self._logged_in = True

    def logout(self):
        self._user = None
        self._logged_in = False

    def login_status(self):
        return self._logged_in

    def get_user_id(self):
        if self.login_status():
            return self._user.id
        return 0

user_service = UserService()
