#!/usr/bin/python
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/bob")
def bob():
    return "<p>bob</p>"

@app.route("/chart")
def chart():
    return render_template("chart.html")