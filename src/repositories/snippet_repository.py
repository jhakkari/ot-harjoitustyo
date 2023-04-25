from db_connection import get_database_connection

class SnippetRepository:

    def __init__(self, connection):
        self._db_connection = connection
        self._db = self._db_connection.cursor()

    def create(self, user_id, content):
        try:
            sql = """INSERT INTO snippets (user_id, content, created_at) VALUES (:user_id, :content, DATETIME('now'))"""
            self._db.execute(sql, {"user_id":user_id, "content":content})
            self._db_connection.commit()
        except:
            return False
        return True

    def get_all(self, user_id):
        sql = """SELECT id, user_id, content, created_at FROM snippets WHERE user_id=:user_id"""
        results = self._db.execute(sql, {"user_id":user_id}).fetchall()
        if not results:
            return None
        return results


snippet_repository = SnippetRepository(get_database_connection())
