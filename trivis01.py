#!/usr/bin/env python3

from flask import Flask
from flask import redirect
from flask import request
from flask import render_template


app = Flask(__name__)

@app.route("/admin")
def full_metal_jacket():
    return "How tall are you? "

@app.route("/guest/<guesty>")
def hello_guest(guesty):
    return f"Hello {guesty} Guest"
    #V2 FORMATTER - return "Hello {} Guest".format(guesty)
    #OLD FORMATTER - return "Hello %s as Guest" % guesty

@app.route("/user/<name>")
def hello_user(name):
    ## if you go to hello_user with a value of admin
    if name =="admin":
        # return a 302 response to redirect to /admin
        return redirect(url_for("hello_admin"))
    else:
        # return a 302 response to redirect to /guest/<guesty>
        return redirect(url_for("hello_guest",guesty = name))

if __name__ == "__main__":
   app.run(host="0.0.0.0", port=2224) # runs the application

