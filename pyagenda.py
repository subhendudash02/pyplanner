import os
import database.db_ops as ops
import sys
from datetime import datetime
import time as tt
import cron_job as cr
import task_list as tl
from os_checker import check_os

if check_os() != "Linux":
    print("This application is supported by Linux only.")
    exit()

def task_register(task, time):
    d = datetime.now()
    new = datetime(d.year, d.month, d.day, int(time[0:2]), int(time[3:5]), 0)
    unix = tt.mktime(new.timetuple())
    cron = "{} {} {} {} *".format(time[3:5], time[0:2], d.day, d.month)
    ops.insertInto_table([task, time, unix, cron])

    final_txt = "XDG_RUNTIME_DIR=/run/user/$(id -u) notify-send Reminder '{}'".format(task)  
    
    cr.make_job(final_txt, [time[3:5], time[0:2], d.day, d.month])


args = len(sys.argv)

try:
    ops.create_table("set_task", ["name", "time", "unix", "cron"], ["text", "text", "bigint", "text"])
except:
    pass

if args == 4:
    task_register(sys.argv[2], sys.argv[3])
    print("Task Scheduled!")

elif args == 2:
    if sys.argv[1] == "reset":
        ops.remove_db()
        cr.clear_jobs()
        print("All the tasks are removed. Hence you will not receive notifications until you schedule a new task.")
    elif sys.argv[1] == "show_tasks":
        tl.print_tasks()
    elif sys.argv[1] == "start_app":
        print("Starting the app...")
        os.system("python3 -m app_util")
    elif sys.argv[1] == "help":
        print("""
        Usage:
        python3 -m pyagenda [option] [task] [time]

        Options:
        reset - Removes all the tasks from the database.
        show_tasks - Shows all the tasks in the database.
        start_app - Starts the application.
        """)
    else:
        print("Unknown Command. Please use 'python3 -m pyagenda help' for more info.")