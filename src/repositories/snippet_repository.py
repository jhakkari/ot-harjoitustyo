import sqlite3
from db_connection import get_database_connection


class SnippetRepository:
    """Koodinpätkiin liittyvistä tietokantaoperaatioista vastaava luokka.
    """

    def __init__(self, connection):
        """Luokan konstruktori. Luo saamastaan tietokantayhteydestä cursor-olion.

        Args:
            connection: Tietokantayhteyden connection-olio.
        """

        self._db_connection = connection
        self._db = self._db_connection.cursor()

    def create(self, user_id, content):
        """Tallentaa koodinpätkän tietokantaan.

        Args:
            user_id: Koodinpätkän luoneen käyttäjän yksilöivä tunniste.
            content: Koodinpätkän sisältö

        Returns:
            True tallentamisen onnistuessa, muussa tapauksessa False.
        """

        try:
            sql = """INSERT INTO snippets (user_id, content, created_at) VALUES (:user_id, :content, DATETIME('now'))"""
            self._db.execute(sql, {"user_id": user_id, "content": content})
            self._db_connection.commit()
        except sqlite3.DatabaseError:
            return False
        return True

    def delete(self, snippet_id):
        """Poistaa koodinpätkän tietokannasta.

        Args:
            id: Koodinpätkän yksilöivä tunniste.

        Returns:
            True poistamisen onnistuessa, muussa tapauksessa False.
        """

        try:
            sql = """DELETE FROM snippets WHERE id=:id"""
            self._db.execute(sql, {"id": snippet_id})
            self._db.connection.commit()
        except sqlite3.DatabaseError:
            return False
        return True

    def get_all(self, user_id):
        """Palauttaa kaikki käyttäjään yhdistetyt koodinpätkät.

        Args:
            user_id: Käyttäjän yksilöivä tunnuste, jonka koodinpätkät haetaan.

        Returns:
            Lista koodinpätkistä tietokantariveinä. Muussa tapauksessa None.
        """

        sql = """SELECT id, user_id, content, created_at FROM snippets WHERE user_id=:user_id ORDER BY created_at DESC"""
        results = self._db.execute(sql, {"user_id": user_id}).fetchall()
        if not results:
            return None
        return results

    def delete_all(self, user_id):
        """Poistaa kaikki käyttäjän luomat koodinpätkät tietokannasta.

        Args:
            user_id: Käyttäjän yksilöivä tunniste, jonka koodinpätkät poistetaan.

        Returns:
            Palauttaa True
        """

        sql = """DELETE FROM snippets WHERE user_id=:user_id"""
        self._db.execute(sql, {"user_id": user_id})
        self._db.connection.commit()
        return True


snippet_repository = SnippetRepository(get_database_connection())
