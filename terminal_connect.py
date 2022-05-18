import sqlite3 as sql
import db_ops as ops
import sys

connect_db = sql.connect("util.db") # will create and connect the database
args = len(sys.argv)

try:
    ops.create_table("task", ["sl_no", "name"], ["integer", "text"])
except:
    pass

if args == 4:
    ops.insertInto_table(sys.argv[1], [sys.argv[2], sys.argv[3]])
else:
    print("Set some tasks...")