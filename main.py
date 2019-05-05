import os
import sqlite3

from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

project_directory = os.path.dirname(os.path.abspath(__file__))
database_file = "sqlite:///{}".format(os.path.join(project_directory, "startupdata.db"))

app = Flask(__name__)
# app.config["SQLALCHEMY_DATABASE_URI"] = database_file
#
# db = SQLAlchemy(app)

# https://www.tutorialspoint.com/flask/flask_sqlite.htm
# from gevent.pywsgi import WSGIServer
#
# connection = sqlite3.connect('startupdata.db')
# print("Database created")
#
# connection.execute('CREATE TABLE startups (name TEXT, sector TEXT, bio TEXT)')
# print("Table startups created")
# connection.close

# cur = connection.cursor()
# sql_command = 'INSERT INTO startups (name, sector, bio) VALUES (?, ?, ?)'
# values = ('Company1', 'Tech', 'Hello world')
# cur.execute(sql_command, values)
@app.route('/', methods = ['GET', 'POST'])
def home():
    if request.method == 'POST':
        print(request.form)
        connection = sqlite3.connect('startupdata.db')
        print(1)
        connection.row_factory = sqlite3.Row
        print(2)
        cur = connection.cursor()
        print(3)
        cur.execute("INSERT INTO startups (name, sector, bio) VALUES(?, ?, ?)",
        (request.form["Name"], request.form["Sector"], request.form["Bio"]))
        print(4)
        connection.commit()
        print(connection)
    return render_template('home.html')

@app.route('/table')
def table():
    connection = sqlite3.connect('startupdata.db')
    connection.row_factory = sqlite3.Row

    cur = connection.cursor()
    cur.execute('SELECT * FROM startups')

    rows = cur.fetchall();
    return render_template('table.html', rows = rows)

if __name__ == "__main__":
    app.run()
