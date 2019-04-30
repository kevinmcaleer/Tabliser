# Tabliser - creates web tables from databases

import sqlite3

class Tableiser:
    name = "" # the name of the table!
    columns = 0 # the number of table columns

    def connect_to_database(self, filename):
        """ returning the connection """
        conn = sqlite3.connect(filename)
        return conn


# - connect to database database file
# - get list of tables from database
# - get list of columns from a table (and the types)
# - draw table headers
# - loop through each row until page limit is hit
# - draw pagination (rows / rows_per_page)
