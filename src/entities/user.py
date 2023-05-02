class User:
    """Luokka, joka kuvaa yksittäistä käyttäjää.
    """

    def __init__(self, id, username, password):
        """Luokan konstruktori, joka luo uuden käyttäjän.

        Args:
            id (int): Käyttäjän yksilöivä tunniste
            username (String): Käyttäjän käyttäjätunnus
            password (String): Käyttäjän salasana.
        """

        self.id = id
        self.username = username
        self.password = password
