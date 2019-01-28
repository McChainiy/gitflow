from PyQt5 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_calanderTestWindow(object):
    def setupUi(self, calanderTestWindow):
        calanderTestWindow.setObjectName(_fromUtf8("calanderTestWindow"))
        calanderTestWindow.resize(262, 203)
        calanderTestWindow.setWindowTitle(QtGui.QApplication.translate("calanderTestWindow", "Calendar Test Window", None, QtGui.QApplication.UnicodeUTF8))
        self.centralwidget = QtGui.QWidget(calanderTestWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.testCalander = QtGui.QCalendarWidget(self.centralwidget)
        self.testCalander.setGeometry(QtCore.QRect(0, 0, 256, 155))
        self.testCalander.setGridVisible(True)
        self.testCalander.setVerticalHeaderFormat(QtGui.QCalendarWidget.NoVerticalHeader)
        self.testCalander.setNavigationBarVisible(True)
        self.testCalander.setObjectName(_fromUtf8("testCalander"))
        calanderTestWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(calanderTestWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 262, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        calanderTestWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(calanderTestWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        calanderTestWindow.setStatusBar(self.statusbar)

        self.retranslateUi(calanderTestWindow)
        QtCore.QMetaObject.connectSlotsByName(calanderTestWindow)

    def retranslateUi(self, calanderTestWindow):
        pass