import subprocess as sp
import sqlite3 as sql

connect_db = sql.connect("util.db")

def remove_db(): # will be used to reset the application
    x = sp.run(["find", "util.db"], stdout=sp.DEVNULL, stderr=sp.DEVNULL)
    if x.returncode == 1:
        print("No Database found")
    else:
        sp.run(["rm", "util.db"])

def create_table(name, attr, datatypes):
    connect_db.execute("CREATE TABLE {}({} {}, {} {});"
                    .format(name, attr[0], datatypes[0], attr[1], datatypes[1])
                    )

def insertInto_table(name, values):
    connect_db.execute("INSERT INTO {} VALUES({}, '{}');".format(name, values[0], values[1]))
    connect_db.commit()
