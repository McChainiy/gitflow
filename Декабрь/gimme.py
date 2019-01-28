import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow
from boooo import Ui_MainWindow


class MyWidget(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.buttonGroup.buttonClicked.connect(self.dosmth)



    def dosmth(self):
        print('lol')

    def run(self):
        self.label.setText("OK")


app = QApplication(sys.argv)
ex = MyWidget()
ex.show()
sys.exit(app.exec_())