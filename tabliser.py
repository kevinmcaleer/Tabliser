# Tabliser - creates web tables from databases

class Column(object):
    """ models a table column """
    type = 0
    name = ""

    def is_type(self):
        """ returns the columns type """
        return self.type

    def get_name(self):
        """ returns the column name """
        return self.name

class Table(object):
    """ table controller """
    name = "" # the name of the table!
    columns = 0 # the number of table columns
    row_headers = [Column()]
    rows = [] # an array of columns

    def count(self):
        """ returns the number of rows """
        return len(self.rows)

    def add_column(self, column: Column):
        """ adds a column to the current table """
        self.rows.append(column)

    def show(self):
        """ shows the table """
        print(self.name)
        for col in self.row_headers:
            print(col)
        for col in self.rows:
            print(col)
                # print(col.name, " | ",col.type)
            # print(col.type)
# - connect to database database file
# - get list of tables from database
# - get list of columns from a table (and the types)
# - draw table headers
# - loop through each row until page limit is hit
# - draw pagination (rows / rows_per_page)
