import db_ops as ops
import sys
from datetime import datetime
import time
import cron_job as cr

args = len(sys.argv)

try:
    ops.create_table("task", ["name", "time", "unix", "cron"], ["text", "text", "bigint", "text"])
except:
    pass

if args == 4:
        d = datetime.now()
        new = datetime(d.year, d.month, d.day, int(sys.argv[3][0:2]), int(sys.argv[3][3:5]), 0)
        unix = time.mktime(new.timetuple())
        cron = "{} {} {} {} *".format(sys.argv[3][3:5], sys.argv[3][0:2], d.day, d.month)
        ops.insertInto_table(sys.argv[1], [sys.argv[2], sys.argv[3], unix, cron])
elif args == 2 and sys.argv[1] == "reset":
    ops.remove_db()
elif args == 1:
    print("Set some tasks...")

final_txt = "XDG_RUNTIME_DIR=/run/user/$(id -u) notify-send Reminder '{}'".format(sys.argv[2])

cr.make_job(final_txt, [sys.argv[3][3:5], sys.argv[3][0:2], d.day, d.month])