# Contributing Guidelines

Before contributing to the repository, read the following guidelines carefully so that you can create the issue and make a pull request correctly.

Before changing the codebase of the repository, make sure you have installed the following requirements: 
 - Python (3.7 or higher)
 - Qt Creator for Linux
 - crontab in Linux

# Git Flow and Setup

1. Go to [subhendudash02/pyagenda](https://github.com/subhendudash02/pyagenda) and click on fork button.

![fork](./screenshots/fork.png)

Change the owner where you want to fork and contribute.

2. Now, to clone the repository, type the following command in terminal (any directory).

```
git@github.com:<username>/pyagenda.git
```

**Note**: The `<username>` is the same you chose for the owner in the previous step.

3. Go to the directory.

```
cd pyagenda
```

4. Install all the dependencies.

```
pip3 install -r requirements.txt
```

For CLI part, it is easy to use, just follow the [list of commands](https://github.com/subhendudash02/pyagenda#commands) accordingly.

For GUI part, **don't change `gui_app.py` in `appUtil` file**. That python file is automatically generated after saving `gui.ui` XML file.

# GUI Setup

1. After installing QtCreator, open the software.

![QtCreator](./screenshots/QtCreator.png)

2. Go to "Debug", open `gui.ui` file.

3. You will get the layout as shown below.

![Debug](./screenshots/customise_gui.png)

Now you can change and add any components for the UI.

4. After changing the UI, save the changes. Go to `appUtil` folder and type the following command to compile the XML file to Python.

```
pyuic5 gui.ui > gui_app.py
```

Don't change the file name to anything else.

# Pull Requests

1. After forking and cloning the repository, change the branch to `build`.

```
git checkout build
```

2. Now, make any changes you want in that branch. Don't make any changes to `main` branch.

3. Commit the changes and push the changes.

4. Make the pull request.