# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'calendar_design2.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(521, 805)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.calendarWidget = QtWidgets.QCalendarWidget(self.centralwidget)
        self.calendarWidget.setGeometry(QtCore.QRect(20, 20, 271, 201))
        self.calendarWidget.setObjectName("calendarWidget")
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(60, 440, 381, 251))
        self.listWidget.setObjectName("listWidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(320, 30, 181, 191))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.minutes_dial = QtWidgets.QDial(self.frame)
        self.minutes_dial.setGeometry(QtCore.QRect(80, 10, 81, 81))
        self.minutes_dial.setObjectName("minutes_dial")
        self.minutes_label = QtWidgets.QLabel(self.frame)
        self.minutes_label.setGeometry(QtCore.QRect(100, 90, 51, 16))
        self.minutes_label.setObjectName("minutes_label")
        self.hours_label = QtWidgets.QLabel(self.frame)
        self.hours_label.setGeometry(QtCore.QRect(30, 90, 47, 13))
        self.hours_label.setObjectName("hours_label")
        self.hours_dial = QtWidgets.QDial(self.frame)
        self.hours_dial.setGeometry(QtCore.QRect(10, 10, 81, 81))
        self.hours_dial.setObjectName("hours_dial")
        self.dateEdit = QtWidgets.QDateTimeEdit(self.frame)
        self.dateEdit.setGeometry(QtCore.QRect(10, 120, 161, 61))
        self.dateEdit.setObjectName("dateEdit")
        self.addEvent = QtWidgets.QPushButton(self.centralwidget)
        self.addEvent.setGeometry(QtCore.QRect(130, 710, 241, 71))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.addEvent.setFont(font)
        self.addEvent.setObjectName("addEvent")
        self.descriptionText = QtWidgets.QTextEdit(self.centralwidget)
        self.descriptionText.setGeometry(QtCore.QRect(30, 270, 441, 101))
        self.descriptionText.setObjectName("descriptionText")
        self.event_description_label = QtWidgets.QLabel(self.centralwidget)
        self.event_description_label.setGeometry(QtCore.QRect(150, 230, 241, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.event_description_label.setFont(font)
        self.event_description_label.setObjectName("event_description_label")
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(20, 380, 481, 20))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.list_of_events_label = QtWidgets.QLabel(self.centralwidget)
        self.list_of_events_label.setGeometry(QtCore.QRect(150, 400, 191, 31))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.list_of_events_label.setFont(font)
        self.list_of_events_label.setObjectName("list_of_events_label")
        self.frame.raise_()
        self.calendarWidget.raise_()
        self.listWidget.raise_()
        self.addEvent.raise_()
        self.descriptionText.raise_()
        self.event_description_label.raise_()
        self.line_2.raise_()
        self.list_of_events_label.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionSave = QtWidgets.QAction(MainWindow)
        self.actionSave.setObjectName("actionSave")
        self.actionKek = QtWidgets.QAction(MainWindow)
        self.actionKek.setObjectName("actionKek")

        self.hours_dial.setSliderPosition(12)
        self.hours_dial.setRange(0, 23)

        self.minutes_dial.setSliderPosition(30)
        self.minutes_dial.setRange(0, 59)




        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.minutes_label.setText(_translate("MainWindow", "Minutes"))
        self.hours_label.setText(_translate("MainWindow", "Hours"))
        self.addEvent.setText(_translate("MainWindow", "Добавить Событие"))
        self.event_description_label.setText(_translate("MainWindow", "Описание События"))
        self.list_of_events_label.setText(_translate("MainWindow", "Список событий"))
        self.actionSave.setText(_translate("MainWindow", "Save"))
        self.actionKek.setText(_translate("MainWindow", "  "))

