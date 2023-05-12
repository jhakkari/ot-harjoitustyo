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
    """Käyttäjien hallintaan liittyvästä logiikasta vastaava luokka.
    """

    def __init__(self):
        self._user_repository = user_repository
        self._user = None
        self._logged_in = False

    def register(self, username, password, password_confirmation):
        """Luo uuden käyttäjän ja kirjaa sen sisään.

        Args:
            username: Uuden käyttäjän käyttäjätunnus.
            password: Uuden käyttäjän salasana.
            password_confirmation: Salasanan varmistus.

        Raises:
            UsernameAlreadyExistsError: Virhe, tapahtuu kun käyttäjätunnus on jo käytössä.
            IncorrectInputError: Virhe, tapahtuu kun annetut tiedot eivät vastaa niiden vaatimuksia.
            PasswordsDoNotMatchError: Virhe, tapahtuu kun annetut salasanat eivät vastaa toisiaan.
            IncorrectInputError: Virhe, tapahtuu kun annetut tiedot ovat tyhjiä tai liian pitkiä.
            IncorrectInputError: Virhe, tapahtuu kun annetut tiedot sisältävät välilyöntejä.

        """
        if self._user_repository.check_existing(username):
            raise UsernameAlreadyExistsError(f"Username {username} already exists")

        if " " in username or " " in password:
            raise IncorrectInputError("Username or password cannot contain whitespaces")

        if password != password_confirmation:
            raise PasswordsDoNotMatchError("Passwords do not match. Try again.")

        if len(username) < 1 or len(password) < 1:
            raise IncorrectInputError("Please fill all the fields.")

        if len(username) > 20 or len(password) > 20:
            raise IncorrectInputError("Username or password too long.")

        self._user_repository.create(username, password)
        self.login(username, password)

    def login(self, username, password):
        """Kirjaa käyttäjän sisään.

        Args:
            username: Kirjautuvan käyttäjän käyttäjätunnus.
            password: Kirjautuvan käyttäjän salasana.

        Raises:
            IncorrectInputError: Virhe, tapahtuu kun annetut tiedot eivät sisällä mitään.
            InvalidUserError: Virhe, tapahtuu kun käyttäjää ei ole olemassa.
            IncorrectCredentialsError: Virhe, tapahtuu kun kirjautuminen ei onnistu.
        """
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
        """Kirjaa käyttäjän ulos.
        """
        self._user = None
        self._logged_in = False

    def login_status(self):
        """Palauttaa tiedon, onko käyttäjä kirjautunut sisään.

        Returns:
            True mikäli on, muussa tapauksessa False.
        """
        return self._logged_in

    def get_user_id(self):
        """Palauttaa kirjautuneen käyttäjän yksilöivän id-tunnisteen.

        Returns:
            int: 0 mikäli ei kirjautunut, muussa tapauksessa > 0.
        """
        if self.login_status():
            return self._user.user_id
        return 0

user_service = UserService()
