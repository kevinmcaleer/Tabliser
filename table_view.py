from tabliser import Table

class TableView(object):
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
