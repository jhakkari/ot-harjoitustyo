from repositories.user_repository import user_repository

class UsernameAlreadyExistsError(Exception):
    pass

class PasswordsDoNotMatchError(Exception):
    pass

class IncorrectInputError(Exception):
    pass


class UserService:

    def __init__(self):
        self._user_repository = user_repository

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
        

user_service = UserService()