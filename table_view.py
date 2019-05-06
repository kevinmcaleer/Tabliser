from tabliser import Table

# TODO: need to add pagination
# TODO: add bootstrap div tags

class Table_View(object):
    table = Table()

    def __init__(self, table:Table):
        """ Initialise the TableView object with the provided Table """
        self.table = table

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

    def render_to_string(self):
        # table_string = ""

        table_string = f'<table>'
        for row_header in self.table.row_headers:
            table_string = table_string + f"<th>{row_header}</ht>"
        for rows in self.table.rows:
            table_string = table_string + f"<tr>"
            for row in rows:
                table_string = table_string + f"<td>{row}</td>"
            table_string = table_string + f"</tr>"
        table_string = table_string + f'</table>'
        print(table_string)
        return table_string

    def __repr__(self):
        return self.render_to_string()


    def __str__(self):
        return self.render_to_string()

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
