import os
import subprocess as sp
from datetime import datetime
import time as tt
import pyplanner.cron_job as cr
from pyplanner.db_ops import TableSQL
from pyplanner.os_checker import check_os
from pyplanner._global import *

ops = TableSQL('set_task', attributes, datatypes)

if check_os() != "Linux":
    print("This application is supported for Linux only.")
    exit()

"""
Creates db file on execution of this file
"""

try:
    if not os.path.exists(db_path):
        os.mkdir(db_path)
    ops.create_table()
except:
    pass

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
    rem_time = "{} {} {} {} *".format(str(int(time[3:5]) - 5), time[0:2], d.day, d.month)
    ops.insertInto_table([task, time, unix, cron, rem_time])

    # Notification in Linux
    final_txt = "XDG_RUNTIME_DIR=/run/user/$(id -u) notify-send Reminder '{}'".format(task)  
    
    # Register task in cron
    cr.make_job(final_txt, [str(int(time[3:5]) - 5), time[0:2], d.day, d.month])
