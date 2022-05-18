import subprocess as sp

def add_db():
    x = sp.run(["find", "util.db"], stdout=sp.DEVNULL, stderr=sp.DEVNULL)
    if x.returncode == 0:
        print("Database already there")
    else:
        sp.run(["touch", "util.db"])

def remove_db():
    x = sp.run(["find", "util.db"], stdout=sp.DEVNULL, stderr=sp.DEVNULL)
    if x.returncode == 1:
        print("No Database found")
    else:
        sp.run(["rm", "util.db"])