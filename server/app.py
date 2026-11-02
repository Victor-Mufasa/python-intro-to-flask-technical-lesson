#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

# 1. Home Page
@app.route('/')
def home():
    return "<h1><em>You</em> are <strong>home</strong>.</h1>"

@app.route('/<string:username>')
def user(username):
    return f"<h1>Profile for {username}</h1>"

if __name__ == '__main__':
    app.run(port=5000, debug=True)