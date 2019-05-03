# import Tabliser as Tb
import sqlite3
from sqlite3 import Error
from tabliser import Table, Column
from table_view import TableView
from table_dal import Table_DAL

# connect to databases

def main():

    t = Table()
    t_dal = Table_DAL()
    t_dal.load("test.db", "animals", t)
    tv = TableView(t)
    tv.render()
    tv.render_text()
    # t.show()

if __name__ == '__main__':
    main()
