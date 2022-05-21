import db_ops as ops
import sys
from datetime import datetime
import time
import cron_job as cr
import task_list as tl

args = len(sys.argv)

try:
    ops.create_table("set_task", ["name", "time", "unix", "cron"], ["text", "text", "bigint", "text"])
except:
    pass

if args == 4:
    d = datetime.now()
    new = datetime(d.year, d.month, d.day, int(sys.argv[3][0:2]), int(sys.argv[3][3:5]), 0)
    unix = time.mktime(new.timetuple())
    cron = "{} {} {} {} *".format(sys.argv[3][3:5], sys.argv[3][0:2], d.day, d.month)
    ops.insertInto_table([sys.argv[2], sys.argv[3], unix, cron])
    final_txt = "XDG_RUNTIME_DIR=/run/user/$(id -u) notify-send Reminder '{}'".format(sys.argv[2])  
    cr.make_job(final_txt, [sys.argv[3][3:5], sys.argv[3][0:2], d.day, d.month])

elif args == 2:
    if sys.argv[1] == "reset":
        ops.remove_db()
        cr.clear_jobs()
        print("All the tasks are removed. Hence you will not receive notifications until you schedule a new task.")
    elif sys.argv[1] == "show_tasks":
        tl.print_tasks()
    
elif args == 1:
    print("Set some tasks...")
    print("Usage: python3 terminal_connect.py set_task <task_name> <time>")