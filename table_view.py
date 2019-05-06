from tabliser import Table

# TODO: need to add pagination
# TODO: add bootstrap div tags

class Table_View(object):
    table = Table()
    page_index = ""
    rows_per_page = 5 # default number of rows to show per page.
    current_page = 1

    def __init__(self, table:Table):
        """ Initialise the TableView object with the provided Table """
        self.table = table

    def set_current_page(self, page_number):
        """ sets the current page to the number provided """
        self.current_page = page_number


    def set_rows_per_page(self, number_of_rows):
        """ set the number of rows shown per page """
        self.rows_per_page = number_of_rows

    def render(self):
        """ Render the table in HTML """
        print("<table>")
        # for each row in the table print it out
        for row_header in self.table.row_headers:
            print("<th>",row_header,"</th>")
        for rows in self.table.rows:
            print("<tr>")
            for row in rows:
                print("<td>", row, "</td>")
            print("</tr>")
        print("</table>")

    def render_to_string(self, page):
        # table_string = 0987657""

        table_string = f'<table class="table">'
        for row_header in self.table.row_headers:
            table_string = table_string + f"<th>{row_header}</ht>"

        r = 0
        # r = self.current_page * self.rows_per_page
        print(f"r is {r}")
        for rows in self.table.rows:
            if (r < (self.current_page * self.rows_per_page) and (r >= (self.current_page -1 ) * self.rows_per_page )):

                table_string = table_string + f"<tr>"
                for row in rows:
                    print(page)
                    table_string = table_string + f"<td>{row}</td>"

                table_string = table_string + f"</tr>"
            r += 1
        table_string = table_string + f'</table>'
        # print(table_string)
        return table_string

    def __repr__(self):
        return self.render_to_string(self.current_page)


    def __str__(self):
        return self.render_to_string(self.current_page)

    def render_text(self):
        """ Render the table in commandline text """
        print("Table:", self.table.name)

        print("+", end =" "),
        for row_header in self.table.row_headers:
            print(row_header, end =" ")
            # print("|", end =" ")
        print("+")
        # print("+")
        for rows in self.table.rows:
            for row in rows:
                print("|", row, end =" ")
            print("|")
        print("")
