from flask import Flask, render_template 
import sqlite3
app = Flask(__name__)


@app.route("/")
def index():
    con = sqlite3.connect("/home/pi/Desktop/iot2/Data_1.db")
    con.row_factory = sqlite3.Row 
    cur = con.cursor() 
    cur.execute("select * from tilbud") 
    rows = cur.fetchall() 
    return render_template("index.html", rows = rows)

if __name__ == '__main__':
    app.run(host='192.168.137.216')
