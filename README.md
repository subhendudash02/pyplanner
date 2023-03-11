# pyplanner

![Stars](https://img.shields.io/github/stars/subhendudash02/pyagenda.svg?logo=github) ![forks](https://img.shields.io/github/forks/subhendudash02/pyagenda.svg?logo=github&color=green) ![lang](https://img.shields.io/github/languages/top/subhendudash02/pyagenda?color=blue&logo=python)

This is the official pyplanner repository.

This lightweight application allows you to quickly schedule your activities.

pyplanner keeps track of all your activities and notifies you when they are due.

## Getting Started

1. Fork this repository.

2. Clone the repository.

```
git@github.com:<username>/pyplanner.git
```

3. Go to the directory

```
cd pyplanner
```

4. Install all the dependencies.

```
pip3 install -r requirements.txt
```

5. Run the following command

```
python3 -m pyplanner set_task <task-name> <time-scheduled>
```

That's it! You have scheduled a task.

![reminder](./screenshots/reminder.png)

## System Requirements

This app is supported in Linux as of now. So if you have any Linux distribution (Ubuntu, Fedora, Manjaro, etc.), you are good to go.

1. Python (3.8 or higher) and pip (21 or higher)

2. [crontab](https://en.wikipedia.org/wiki/Cron) if it is not installed.

3. Visual Studio Code ([install here](https://code.visualstudio.com/))

4. Git

**Note:** The installation process differs in different Linux distributions.

## Commands

1. Reset all the tasks or if anything goes wrong.

```
python3 -m pyplanner reset 
```

2. Display list of tasks in command line.

```
python3 -m pyplanner show_tasks
```

![show_tasks](screenshots/show_tasks.png)

3. Set a task

```
python3 -m pyplanner set_task <task-name> <time-scheduled>
```

## Plans

 - [x] Make package of this app
 - [ ] Add / Remove Tasks using [Textualize](https://github.com/Textualize) TUI library.
 - [ ] Add test cases to validate before merging PR.

<br>

## Contributing

 - Make sure you read [contributing guidelines](https://github.com/subhendudash02/pyplanner/blob/main/CONTRIBUTING.md) first.

 - Follow our [code of conduct](https://github.com/subhendudash02/pyplanner/blob/main/CODE_OF_CONDUCT.md). Violation of any rule will lead to disqualification from Hacktoberfest 2022.

 - Follow PR template and issue template accordingly before creating any issue/PR.

## License

[Licensed](https://github.com/subhendudash02/pyagenda/blob/main/LICENSE) under MIT License

Copyright (c) 2022 Subhendu Dash
