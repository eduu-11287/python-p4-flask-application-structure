#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

# Routing is the association of URLs & the code that should execute when a request comes in from that URL.
# we use (@app.route) decorator when routing in flask
# functions that map to URLs can be called views.
# A view returns the response that the client delivers to user 

# decorator is an intance method that modifies APP
@app.route('/') # decorators take functions as arguments. => the slash "/" shows the url to a particula page
def index(): # takes index() as its function argument
    return '<h1>Welcome to my page!</h1>'# what should be shown on the page when visited

@app.route('/<string:username>')# anything included in the route passed to the app.route decorator with angle bracket <> 
# surrounding it will be passed the decorater function as parameter.
#we can make sure that the username is a valid string, int, float, or path (strings with slashes) by specifying this in the route
def user(username): #  function user took username as its parameta
    return '<h1>Profile for {username}</h1>' # what should be shown on the page when visited

if __name__ == '__main__':
    app.run(port=5555, debug=True) # treating an applictation as a script with the app.run() method/function