import subprocess as sp
import sqlite3 as sql

connect_db = sql.connect("util.db", check_same_thread=False)
cursor = connect_db.cursor()

def remove_db(): # will be used to reset the application
    x = sp.run(["find", "util.db"], stdout=sp.DEVNULL, stderr=sp.DEVNULL)
    if x.returncode == 1:
        print("No Database found")
    else:
        sp.run(["rm", "util.db"])

def create_table(name, attr, datatypes):
    cursor.execute("CREATE TABLE {}({} {}, {} {}, {} {}, {} {});"
                    .format(name, attr[0], datatypes[0], 
                                attr[1], datatypes[1], 
                                attr[2], datatypes[2],
                                attr[3], datatypes[3])
                    )
    connect_db.commit()

def insertInto_table(name, values):
    cursor.execute("INSERT INTO {} VALUES('{}', '{}', '{}', '{}');".format(name, values[0], values[1], values[2], values[3]))
    connect_db.commit()

def topmost_row():
    time = cursor.execute("SELECT name, unix, cron from task ORDER BY unix DESC LIMIT 1;")
    connect_db.commit()
    return time.fetchall()

def delete_row(unix):
    cursor.execute("DELETE from task where unix = {};".format(unix))
    connect_db.commit()