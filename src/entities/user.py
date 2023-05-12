class User:
    """Luokka, joka kuvaa yksittäistä käyttäjää.
    """

    def __init__(self, user_id, username, password):
        """Luokan konstruktori, joka luo uuden käyttäjän.

        Args:
            user_id (int): Käyttäjän yksilöivä tunniste
            username (String): Käyttäjän käyttäjätunnus
            password (String): Käyttäjän salasana.
        """

        self.user_id = user_id
        self.username = username
        self.password = password
