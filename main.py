import sqlite3
from flask import Flask, render_template
app = Flask(__name__)

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
