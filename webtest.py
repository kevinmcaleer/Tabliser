# web_test.py

from flask import Flask, render_template, request, render_template_string, escape
from flask_bootstrap import Bootstrap
from tabliser import Table
from table_dal import Table_DAL
from table_view import Table_View

APP = Flask(__name__)

table = Table()
table_dal = Table_DAL()
table_dal.load('test.db','animals',table)
table_view = Table_View(table)

@APP.route("/")
def index():
    """ render the main index template """
    # print(f"The contents of tableview are: '{table_view}'"
    table_dal.load('test.db','animals',table)
    table_view = Table_View(table)
    return render_template("index.html", table=table_view, title=table_view.table.name)

def shutdown_server():
    """ shutsdown the SMARSLab web server """
    func = request.environ.get('werkzeug.server.shutdown')
    if func is None:
        raise RuntimeError('Not running with the Werkzeug Server')
    func()


@APP.route('/shutdown')
def shutdown():
    """ requests the web server shutsdown """
    shutdown_server()
    return 'Server shutting down... Done.'

def main():
    """ main event loop """
    print("Starting WebTest")
    APP.secret_key = 'development-key'
    APP.host = '0.0.0.0'
    APP.debug = True
    Bootstrap(APP)
    APP.run(host='0.0.0.0')


if __name__ == "__main__":
    main()
