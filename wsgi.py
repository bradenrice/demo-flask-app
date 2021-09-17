#!/usr/bin/python
from flask import Flask, render_template
import psycopg2
from config import config

app = Flask(__name__)

def get_list():
    conn = None
    try:
        # read connection parameters
        params = config()

        # connect to the PostgreSQL server
        print('Connecting to the PostgreSQL database...')
        conn = psycopg2.connect(**params)

        # create a cursor
        cur = conn.cursor()
        cur.execute('SELECT * from votes')
        list = cur.fetchall()
        flat_list = []
        for row in list:
            flat_list.append(row[0])
	# close the communication with the PostgreSQL
        cur.close()
        return flat_list
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
        return None
    finally:
        if conn is not None:
            conn.close()
            print('Database connection closed.')

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/bob")
def bob():
    return "<p>bob</p>"

@app.route("/chart")
def chart():
    return render_template("chart.html", votes = get_list())