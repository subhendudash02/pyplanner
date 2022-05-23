# pyagenda

This is the official pyagenda repository.

This lightweight application allows you to quickly schedule your activities.

pyagenda keeps track of all your activities and notifies you when they are due.

Both CLI and GUI are supported by pyagenda.

<b>Note: </b> For the time being, this app only runs on Linux. Windows support will be available soon.

<br>

# Getting Started

1. Fork this repository.

2. Clone the repository.

```
git@github.com:<username>/pyagenda.git
```

3. Go to the directory

```
cd pyagenda
```

4. Install all the dependencies.

```
pip3 install -r requirements.txt
```

5. Run the following command

```
python3 -m pyagenda set_task <task-name> <time-scheduled>
```

That's it! You have scheduled a task.

<br>

# Commands

1. Reset all the tasks

```
python3 -m pyagenda reset 
```

2. Display list of tasks in command line.

```
python3 -m pyagenda show_tasks
```

![show_tasks](screenshots/show_tasks.png)

3. Start GUI application.

```
python3 -m pyagenda start_app
```

![start_app](screenshots/start_app.png)

4. Set a task

```
python3 -m pyagenda set_task <task-name> <time-scheduled>
```

<br>

# License

[Licensed](https://github.com/subhendudash02/pyagenda/blob/main/LICENSE) under MIT License

Copyright (c) 2022 Subhendu Dash
