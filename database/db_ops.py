import subprocess as sp
import sqlite3 as sql

class TableSQL:
    def __init__(self, table_name, attr, datatypes):
        self.db_path = "database/util.db"
        self.connect_db = sql.connect(self.db_path, check_same_thread=False)
        self.cursor = self.connect_db.cursor()

        self.table_name = table_name
        self.attr = attr
        self.datatypes = datatypes

    def remove_db(self): # will be used to reset the application
        x = sp.run(["find", self.db_path], stdout=sp.DEVNULL, stderr=sp.DEVNULL)
        if x.returncode == 1:
            print("No Database found")
        else:
            sp.run(["rm", self.db_path])

    def create_table(self):
        self.cursor.execute("CREATE TABLE {}({} {}, {} {}, {} {}, {} {}, {} {});"
                        .format(self.table_name, self.attr[0], self.datatypes[0], 
                                    self.attr[1], self.datatypes[1], 
                                    self.attr[2], self.datatypes[2],
                                    self.attr[3], self.datatypes[3],
                                    self.attr[4], self.datatypes[4])
                    )
        self.connect_db.commit()

    def insertInto_table(self, values):
        self.cursor.execute("INSERT INTO set_task VALUES('{}', '{}', '{}', '{}', '{}');"
                            .format(values[0], values[1], values[2], values[3], values[4]))
        self.connect_db.commit()

    def topmost_row(self):
        time = self.cursor.execute("SELECT name, unix, cron from set_task ORDER BY unix DESC LIMIT 1;")
        self.connect_db.commit()
        return time.fetchall()

    def delete_row(self, unix):
        self.cursor.execute("DELETE from set_task where unix = {};".format(unix))
        self.connect_db.commit()

    def show_tasks(self):
        self.cursor.execute("SELECT * from set_task;")
        self.connect_db.commit()
        return self.cursor.fetchall()
