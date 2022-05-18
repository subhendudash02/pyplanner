import db_ops as ops
import sys
from datetime import datetime
import time
import subprocess

args = len(sys.argv)

def push_notification(message):
    subprocess.Popen(['notify-send', msg])
    return

try:
    ops.create_table("task", ["name", "time", "unix"], ["text", "text", "bigint"])
except:
    pass

if args == 4:
    d = datetime.now()
    new = datetime(d.year, d.month, d.day, int(sys.argv[3][0:2]), int(sys.argv[3][3:5]), 0)
    unix = time.mktime(new.timetuple())
    ops.insertInto_table(sys.argv[1], [sys.argv[2], sys.argv[3], unix])
    ops.sort_table()
elif args == 2 and sys.argv[1] == "reset":
    ops.remove_db()
elif args == 1:
    print("Set some tasks...")

while True:
    current_time = datetime.now()
    sch_time = ops.topmost_row()
    current_time = time.mktime(current_time.timetuple())
    diff = int(sch_time[0][0]) - current_time
    msg = str(sch_time[0][1])
    if diff == 0:
        push_notification(msg)
        ops.delete_row(sch_time[0][0])