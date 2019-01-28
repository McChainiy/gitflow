from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow,\
    QVBoxLayout, QButtonGroup, QRadioButton, QFrame, QPushButton, QLabel, QDialog, QSpinBox
from PyQt5.QtGui import QPainter, QColor
import sys


class MyWindow(QWidget):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.initUI()

    def initUI(self):
        self.setFixedSize(1380, 770)
        self.btn = QPushButton(self)
        self.btn.setText('Генерация флага')
        self.btn.clicked.connect(self.gen)
        self.btn.setGeometry(630, 720, 100, 50)

    def gen(self):
        dial = Dialog()
        dial.exec()
        count = int(dial.spin.text())
        print(count)
        if count == 0:
            return
        height = 720 // count
        width = height * 3
        print(123)



class Dialog(QDialog):
    def __init__(self):
        super(Dialog, self).__init__()
        self.initUI()

    def initUI(self):
        self.setFixedSize(200, 150)
        self.move(300, 300)

        self.spin = QSpinBox(self)
        self.spin.setFixedSize(100, 50)
        self.spin.move(85, 25)

        self.lbl = QLabel(self)
        self.lbl.setText('Цветов: ')
        self.lbl.move(20, 40)

        self.btn = QPushButton(self)
        self.btn.setText('Принять')
        self.btn.move(60, 100)
        self.btn.setFixedSize(100, 40)
        print('a')
        self.btn.clicked.connect(self.accepting)

    def accepting(self):
        self.close()






if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWindow()
    ex.show()
    sys.exit(app.exec_())