from db_connection import get_database_connection

def register(username, password):
    try:
        connection = get_database_connection()
        cursor = connection.cursor()

        cursor.execute("INSERT INTO users VALUES (?, ?)", (username, password))

        connection.commit()
    except:
        return False
    return True