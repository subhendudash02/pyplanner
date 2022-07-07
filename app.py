from pyagenda import task_register, make_time
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import  QTableWidgetItem
from appUtil.gui_app import Ui_MainWindow
import database.db_ops as ops
import sys
from datetime import datetime

class App(Ui_MainWindow):
    def __init__(self):
        super().__init__()

    def setBackgroundColor(self, row, col, time):
        d = datetime.now()
        green = QtGui.QColor(0, 125, 0)
        red = QtGui.QColor(125, 0, 0)
        if d > make_time(time):
            self.tasks.item(row, col).setBackground(green)
            self.tasks.item(row, col - 1).setBackground(green)
        else:
            self.tasks.item(row, col).setBackground(red)
            self.tasks.item(row, col - 1).setBackground(red)

    
    def table_init(self):
        li = ops.show_tasks()
        self.tasks.setRowCount(len(li))
        self.tasks.setColumnCount(2)

        self.tasks.setHorizontalHeaderLabels(["Task Name", "Time"])
        header = self.tasks.horizontalHeader()
        header.setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)

        for i in range(len(li)):
            for j in range(2):
                self.tasks.setItem(i, j, QTableWidgetItem(str(li[i][j])))
                if j == 1:
                    App.setBackgroundColor(self, row=i, col=j, time=str(li[i][j]))
    
    def add_task(self):
        task = self.setTask.text()
        time = self.setTime.text()
        if len(task) != 0 and len(time) != 0:
            task_register(task, time)
            self.table_init()
            

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = App()
    ui.setupUi(MainWindow)
    ui.table_init()

    ui.addButton.clicked.connect(lambda: ui.add_task())

    MainWindow.show()
    sys.exit(app.exec_())
