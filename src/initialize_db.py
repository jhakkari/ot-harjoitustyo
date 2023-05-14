from db_connection import get_database_connection


def drop_tables(connection):
    cursor = connection.cursor()

    cursor.execute('''
        drop table if exists users;
    ''')

    connection.commit()

    cursor.execute('''
        drop table if exists snippets;
    ''')

    connection.commit()


def create_tables(connection):
    cursor = connection.cursor()

    cursor.execute('''
        create table users (
            id integer primary key,
            username text UNIQUE,
            password text
        );
    ''')

    connection.commit()

    cursor.execute('''
        create table snippets (
            id integer primary key,
            user_id integer,
            content text,
            created_at datetime
        );
    ''')

    connection.commit()


def initialize_database():
    connection = get_database_connection()

    drop_tables(connection)
    create_tables(connection)


if __name__ == '__main__':
    initialize_database()
