import pyagenda as pya
import click
import pyagenda.task_list as tl
import pyagenda.cron_job as cr

@click.group()
def main():
    pass

@click.command('set_task')
@click.argument('task', type=str)
@click.argument('time', type=str)
def set_task(task, time):
    pya.task_register(task, time)
    click.echo("Task Scheduled!")

@click.command('reset')
def reset():
    pya.ops.remove_db()
    cr.clear_jobs()
    click.echo("All the tasks are removed. Hence you will not receive notifications until you schedule a new task.")

@click.command('show_tasks')
def show_tasks():
    tl.print_tasks()

main.add_command(set_task)
main.add_command(reset)
main.add_command(show_tasks)

if __name__ == "__main__":
    main()