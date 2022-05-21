from crontab import CronTab

cron = CronTab(user="subhendu")

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