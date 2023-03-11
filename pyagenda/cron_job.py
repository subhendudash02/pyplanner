from crontab import CronTab
import subprocess as sp
from pyagenda.os_checker import check_os

os = check_os()
username = sp.check_output(["whoami"], shell=True).decode("utf-8").strip()
cron = CronTab(user=username)

def clear_jobs():
    cron.remove_all()
    cron.write()

def make_job(command, li):
    job = cron.new(command)
    job.minute.on(li[0])
    job.hour.on(li[1])
    job.day.on(li[2])
    job.month.on(li[3])
    cron.write()