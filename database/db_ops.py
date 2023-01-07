import subprocess as sp
import sqlite3 as sql

connect_db = sql.connect("database/util.db", check_same_thread=False)
cursor = connect_db.cursor()

def remove_db(): # will be used to reset the application
    x = sp.run(["find", "database/util.db"], stdout=sp.DEVNULL, stderr=sp.DEVNULL)
    if x.returncode == 1:
        print("No Database found")
    else:
        sp.run(["rm", "database/util.db"])

def create_table(name, attr, datatypes):
    cursor.execute("CREATE TABLE {}({} {}, {} {}, {} {}, {} {}, {} {});"
                    .format(name, attr[0], datatypes[0], 
                                attr[1], datatypes[1], 
                                attr[2], datatypes[2],
                                attr[3], datatypes[3],
                                attr[4], datatypes[4])
                    )
    connect_db.commit()

def insertInto_table(values):
    cursor.execute("INSERT INTO set_task VALUES('{}', '{}', '{}', '{}', '{}');".format(values[0], values[1], values[2], values[3], values[4]))
    connect_db.commit()

def topmost_row():
    time = cursor.execute("SELECT name, unix, cron from set_task ORDER BY unix DESC LIMIT 1;")
    connect_db.commit()
    return time.fetchall()

def delete_row(unix):
    cursor.execute("DELETE from set_task where unix = {};".format(unix))
    connect_db.commit()

def show_tasks():
    cursor.execute("SELECT * from set_task;")
    connect_db.commit()
    return cursor.fetchall()