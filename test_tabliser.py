# import Tabliser as Tb
import sqlite3
from sqlite3 import Error

connect to databases


def get_tables(conn):
    """ get a list of all the tables in the SQL lite file """
# get a list of all the tables in the current sql database:
# SELECT * FROM dbname.sqlite_master WHERE type='table';

    cur = conn.cursor()
    cur.execute("SELECT * FROM sqlite_master WHERE type='table'")
    tables = cur.fetchall()
    return tables


def create_connection(db_file):
    """ create a database connection to the SQLite database specified by the db_file
    :param db_file: database file
    :return: Connection object or None """
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)

    return None

def main():
    database = "test.db"

    # create a database connection
    conn = create_connection(database)
    with conn:
        tabs = get_tables(conn)
        for table in tabs:
            if table[0] == 'table':
                print(table[1])
    conn.close()

if __name__ == '__main__':
    main()
