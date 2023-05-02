from db_connection import get_database_connection

class UserRepository:
    """Käyttäjiin liittyvistä tietokantaoperaatioista vastaava luokka
    """

    def __init__(self, connection):
        """Luokan konstruktori. Luo saamastaan tietokantayhteydestä cursor-olion.

        Args:
            connection: Tietokantayhteyden connection-olio.
        """
        self._db_connection = connection
        self._db = self._db_connection.cursor()


    def create(self, username, password):
        """Tallentaa käyttäjätiedot tietokantaan.

        Args:
            username: Käyttäjän käyttäjätunnus.
            password: Käyttäjän salasana.

        Returns:
            True, jos lisääminen oniistui, muussa tapauksessa False.
        """

        try:
            sql = """INSERT INTO users (username, password) VALUES (:username, :password)"""
            self._db.execute(sql, {"username":username, "password":password})

            self._db_connection.commit()
        except:
            return False
        return True

    def check_existing(self, username):
        """Tarkastaa, löytyykö käyttäjä jo tietokannasta.

        Args:
            username: Etsittävä käyttäjätunnus.

        Returns:
            True, mikäli käyttäjä löytyy, muussa tapauksessa False.
        """
        sql = """SELECT * FROM users WHERE username=:username"""
        result = self._db.execute(sql, {"username":username}).fetchone()
        if result:
            return True
        return False

    def get_user(self, username):
        """Palauttaa haettavan käyttäjän tiedot.

        Args:
            username: Käyttäjän käyttäjätunnus.

        Returns:
            Tietokantarivi, jossa käyttäjän id, käyttäjätunnus ja salasana. Muussa tapauksessa None.
        """
        sql = """SELECT * FROM users WHERE username=:username"""
        result = self._db.execute(sql, {"username":username}).fetchone()
        if not result:
            return None
        return result

user_repository = UserRepository(get_database_connection())
