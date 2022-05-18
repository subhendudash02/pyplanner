from flask import Flask, render_template
import sqlite3 as sql

app = Flask(__name__)
connect_db = sql.connect("util.db")

@app.route("/")
def index():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)