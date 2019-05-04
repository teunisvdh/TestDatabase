import sqlite3
from flask import Flask
app = Flask(__name__)

# https://www.tutorialspoint.com/flask/flask_sqlite.htm

def main():
    connection = sqlite3.connect('startupdata.db')
    print("Database created")

    connection.execute('CREATE TABLE startups (name TEXT, sector TEXT, bio TEXT)')
    print("Table startups created")
    connection.close

    @app.route('/table')
    def table():
        connection = sqlite3.connect('startupdata.db')
        connection.row_factory = sqlite3.Row

        cur = connection.cursor()
        cursor.execute('SELECT * FROM startups')

        rows = cur.fetchall();
        return render_template('table.html', rows = rows)

if __name__ == "__main__":
    main()
