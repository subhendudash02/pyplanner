import os
import database.db_ops as ops
from datetime import datetime
import time as tt
import cron_job as cr
import task_list as tl
from os_checker import check_os
import click

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
    rem_time = "{} {} {} {} *".format(str(int(time[3:5]) - 5), time[0:2], d.day, d.month)
    ops.insertInto_table([task, time, unix, cron, rem_time])

    # Notification in Linux
    final_txt = "XDG_RUNTIME_DIR=/run/user/$(id -u) notify-send Reminder '{}'".format(task)  
    
    # Register task in cron
    cr.make_job(final_txt, [str(int(time[3:5]) - 5), time[0:2], d.day, d.month])

"""
Creates db file on execution of this file
"""

try:
    ops.create_table(
        "set_task", 
        ["name", "time", "unix", "cron", "rem_time"], 
        ["text", "text", "bigint", "text", "text"]
    )
except:
    pass

"""
List of commands
"""

@click.group()
def main():
    pass

@click.command('set_task')
@click.argument('task', type=str)
@click.argument('time', type=str)
def set_task(task, time):
    task_register(task, time)
    click.echo("Task Scheduled!")

@click.command('reset')
def reset():
    ops.remove_db()
    cr.clear_jobs()
    click.echo("All the tasks are removed. Hence you will not receive notifications until you schedule a new task.")

@click.command('show_tasks')
def show_tasks():
    tl.print_tasks()

@click.command('start_app')
def start_app():
    click.echo("Starting the app...")
    os.system("python3 -m app")

main.add_command(set_task)
main.add_command(reset)
main.add_command(show_tasks)
main.add_command(start_app)

if __name__ == "__main__":
    main()
