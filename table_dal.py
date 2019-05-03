# table_dal.py
""" Table Data Access Layer - abstration """

from tabliser import Table, Column
import sqlite3

class Table_DAL(object):

    # table = Table()

    def load(self, filename, table_name, table:Table):
        """ loads the table from the filename into the table and returns it"""

        conn = sqlite3.connect(filename)
        cur = conn.cursor()
        cur.execute(f'SELECT * FROM {table_name}')
        result = cur.fetchall()

        for row in result:
            table.rows.append(row)
            # for col in row:

                # table.add_column(col)

        # get the row headers
        conn.row_factory = sqlite3.Row
        cursor = conn.execute(f'select * from {table_name}')
        row = cursor.fetchone()
        column_names = row.keys()
        table.row_headers = column_names
        table.name = table_name
        return table

    def connect_to_database(self, filename):
        """ returning the connection """
        conn = sqlite3.connect(filename)
        return conn

    def get_tables(self, conn):
        """ return a list of tables """
        cur = conn.cursor()
        cur.execute("SELECT * FROM sqlite_master WHERE type='table'")
        tables = cur.fetchall()
        return tables

    def get_columns(self, conn, table_name):
        conn.row_factory = sqlite3.Row
        cursor = conn.execute('select * from {}', table_name)
        # instead of cursor.description:
        row = cursor.fetchone()
        column_names = row.keys()
        return column_names

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
