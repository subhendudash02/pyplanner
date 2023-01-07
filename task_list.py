from rich.console import Console
from rich.table import Table
from database.db_ops import TableSQL
import os

attr = ["name", "time", "unix", "cron", "rem_time"]
datatypes = ["text", "text", "bigint", "text", "text"]
ops = TableSQL('set_task', attr, datatypes)

def print_tasks():
    os.system("clear")
    table = Table(title="\nYour Scheduled Tasks\n", expand=True, show_lines=True)

    table.add_column("Sl.no", justify="center")
    table.add_column("Task Name", justify="center")
    table.add_column("Time", justify="center")

    li = ops.show_tasks()
    sl = 1

    for i in li:
        table.add_row(str(sl), i[0], i[1])
        sl += 1

    console = Console()
    console.print(table)
    print("\n")