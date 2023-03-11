"""
Collection of all global variables used in the pyagenda package.
"""

import subprocess as sp

attributes = ["name", "time", "unix", "cron", "rem_time"]
datatypes = ["text", "text", "bigint", "text", "text"]
username = sp.check_output(["whoami"], shell=True).decode("utf-8").strip()
db_path = "/home/{}/.pyagenda".format(username)