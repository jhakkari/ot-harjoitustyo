from db_connection import get_database_connection

class UserRepository:

    def __init__(self, connection):
        self._db_connection = connection
        self._db = self._db_connection.cursor()


    def create(self, username, password):
        try:
            sql = "INSERT INTO users (username, password) VALUES (:username, :password)"
            self._db.execute(sql, {"username":username, "password":password})

            self._db_connection.commit()
        except:
            return False
        return True

    def check_existing(self, username):
        sql = ("SELECT * FROM users WHERE username=:username")
        result = self._db.execute(sql, {"username":username}).fetchone()
        if result:
            return True
        return False

user_repository = UserRepository(get_database_connection())