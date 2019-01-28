import sys
from PyQt5.QtWidgets import QLabel, QLCDNumber, QLineEdit
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QHBoxLayout
from PyQt5.QtGui import QPixmap


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.hbox = QHBoxLayout(self)

        self.setGeometry(300, 200, 300, 300)
        self.setWindowTitle('Aa')

        self.btn1 = QPushButton('Вывести', self)
        self.btn1.clicked.connect(self.count)
        self.btn1.resize(75, 30)
        self.btn1.move(130, 210)

        self.label2 = QLabel(self)
        self.label2.setText('Название картинки')
        self.label2.move(20, 252)

        self.num2 = QLineEdit(self)
        self.num2.move(130, 250)

        self.label0 = QLabel(self)

    def count(self):
        print('1')
        pikcha = self.num2.text()
        print(pikcha)

        pixmap = QPixmap(pikcha)
        self.label0.setPixmap(pixmap)
        self.label0.resize(pixmap.width(), pixmap.height())
        self.resize(pixmap.width(), pixmap.height())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())

