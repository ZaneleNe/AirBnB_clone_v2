#!/usr/bin/python3
""" Starts a Flash Web Application """
from flask import Flask

app = Flask(__name__)

# Define the route for the root URL'/'
@app.route('/airbnb-onepage/', strict_slashes=FalseI)
def hello_hbnb():
    """ Prints a Message when / is called """
    return "Hello HBNB!"

if __name__ == "__main__":
    """ Main Function """
    app.run(host='0.0.0.0', port=5000)
