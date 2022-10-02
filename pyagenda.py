import os
import database.db_ops as ops
import sys
from datetime import datetime
import time as tt
import cron_job as cr
import task_list as tl
from os_checker import check_os

if check_os() != "Linux":
    print("This application is supported for Linux only.")
    exit()

def make_time(time):
    d = datetime.now()
    new = datetime(d.year, d.month, d.day, int(time[0:2]), int(time[3:5]), 0)
    return new

def task_register(task, time):

    # add task to database
    d = datetime.now()
    new = make_time(time)
    if d >= new:
        print("Invalid time passed.")
        exit()
    unix = tt.mktime(new.timetuple())
    cron = "{} {} {} {} *".format(time[3:5], time[0:2], d.day, d.month)
    ops.insertInto_table([task, time, unix, cron])

    # Notification in Linux
    final_txt = "XDG_RUNTIME_DIR=/run/user/$(id -u) notify-send Reminder '{}'".format(task)  
    
    # Register task in cron
    cr.make_job(final_txt, [time[3:5], time[0:2], d.day, d.month])


args = len(sys.argv)


"""
Creates db file on execution of this file
"""

try:
    ops.create_table("set_task", ["name", "time", "unix", "cron"], ["text", "text", "bigint", "text"])
except:
    pass

"""
List of commands
"""

# python3 -m pyagenda set_task <task-name> <time-scheduled>

if args == 4:
    task_register(sys.argv[2], sys.argv[3])
    print("Task Scheduled!")

elif args == 2:

    # python3 -m pyagenda reset 

    if sys.argv[1] == "reset":
        ops.remove_db()
        cr.clear_jobs()
        print("All the tasks are removed. Hence you will not receive notifications until you schedule a new task.")
    
    # python3 -m pyagenda show_tasks

    elif sys.argv[1] == "show_tasks":
        tl.print_tasks()
    
    # python3 -m pyagenda start_app

    elif sys.argv[1] == "start_app":
        print("Starting the app...")
        os.system("python3 -m app")
    
    # python3 -m pyagenda help

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