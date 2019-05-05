# web_test.py

from flask import Flask
from flask_bootstrap import Bootstrap

APP = Flask(__name__)

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
