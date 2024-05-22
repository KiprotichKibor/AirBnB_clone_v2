#!/usr/bin/python3
from flask import Flask, render_template
"""
Starts a flask web application
"""
app = Flask(__name__)

@app.route("/", strict_slashes=False)
def hello_hbnb():
    """ returns Hello HBNB! """
    return "Hello HBNB!"

@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """ returns HBNB """
    return "HBNB"

@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    """ display “C ” followed by the value of the text variable """
    text_no_underscore = text.replace('_', ' ')
    return "C {}".format(text_no_underscore)

@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def py_text(text='is cool'):
    """ display “Python ”, followed by the value of the text variable """
    text_no_underscore = text.replace('_', ' ')
    return "Python {}".format(text_no_underscore)

@app.route('/number/<int:n>', strict_slashes=False)
def is_int(n):
    """ display “n is a number” only if n is an integer """
    return "{:d} is a number".format(n)

@app.route('/number_template/<int:n>', strict_slashes=False)
def n_template(n):
    """ display a HTML page only if n is an integer """
    return render_template('5-number.html', n=n)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
