# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(641, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.addButton = QtWidgets.QPushButton(self.centralwidget)
        self.addButton.setGeometry(QtCore.QRect(250, 160, 31, 23))
        self.addButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.addButton.setObjectName("addButton")
        self.removeButton = QtWidgets.QPushButton(self.centralwidget)
        self.removeButton.setEnabled(True)
        self.removeButton.setGeometry(QtCore.QRect(290, 160, 31, 23))
        self.removeButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.removeButton.setObjectName("removeButton")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(270, 10, 161, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setAutoFillBackground(False)
        self.label.setTextFormat(QtCore.Qt.AutoText)
        self.label.setObjectName("label")
        self.setTask = QtWidgets.QLineEdit(self.centralwidget)
        self.setTask.setGeometry(QtCore.QRect(10, 110, 311, 23))
        self.setTask.setObjectName("setTask")
        self.setTime = QtWidgets.QLineEdit(self.centralwidget)
        self.setTime.setGeometry(QtCore.QRect(10, 160, 141, 23))
        self.setTime.setObjectName("setTime")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 90, 57, 15))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(10, 140, 57, 15))
        self.label_3.setObjectName("label_3")
        self.tasks = QtWidgets.QTableWidget(self.centralwidget)
        self.tasks.setGeometry(QtCore.QRect(360, 110, 261, 192))
        self.tasks.setObjectName("tasks")
        self.tasks.setColumnCount(0)
        self.tasks.setRowCount(0)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 641, 29))
        self.menubar.setObjectName("menubar")
        self.menuEdit = QtWidgets.QMenu(self.menubar)
        self.menuEdit.setObjectName("menuEdit")
        self.menuMore = QtWidgets.QMenu(self.menubar)
        self.menuMore.setObjectName("menuMore")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionRefresh = QtWidgets.QAction(MainWindow)
        self.actionRefresh.setObjectName("actionRefresh")
        self.actionReset = QtWidgets.QAction(MainWindow)
        self.actionReset.setObjectName("actionReset")
        self.actionAbout = QtWidgets.QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.menuEdit.addAction(self.actionRefresh)
        self.menuEdit.addAction(self.actionReset)
        self.menuMore.addAction(self.actionAbout)
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuMore.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.addButton.setText(_translate("MainWindow", "+"))
        self.removeButton.setText(_translate("MainWindow", "-"))
        self.label.setText(_translate("MainWindow", "Your Tasks"))
        self.label_2.setText(_translate("MainWindow", "Task"))
        self.label_3.setText(_translate("MainWindow", "Time"))
        self.menuEdit.setTitle(_translate("MainWindow", "Edit"))
        self.menuMore.setTitle(_translate("MainWindow", "More"))
        self.actionRefresh.setText(_translate("MainWindow", "Refresh"))
        self.actionReset.setText(_translate("MainWindow", "Reset "))
        self.actionAbout.setText(_translate("MainWindow", "About"))
