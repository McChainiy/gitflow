from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow,\
    QVBoxLayout, QButtonGroup, QRadioButton, QFrame, QPushButton, QLabel
from PyQt5.QtGui import QPainter, QColor
import sys


class MyWindow(QWidget):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.initUI()

    def initUI(self):
        self.conv = {'Red': QColor(255, 0, 0), 'Blue': QColor(0, 0, 255),
                     'White': QColor(255, 255, 255)}
        self.setGeometry(300, 300, 300, 300)
        self.setWindowTitle('Генерация флага')

        self.color1 = QColor(255, 255, 255)
        self.color2 = QColor(255, 255, 255)
        self.color3 = QColor(255, 255, 255)

        self.vbox = QVBoxLayout()

        self.white_button = QRadioButton('White')
        self.white_button.setChecked(True)
        self.blue_button = QRadioButton('Blue')
        self.red_button = QRadioButton('Red')

        self.group = QButtonGroup()

        self.group.addButton(self.white_button)
        self.group.addButton(self.red_button)
        self.group.addButton(self.blue_button)

        self.group.buttonClicked.connect(self._on_radio_button_clicked)

        self.vbox.addWidget(self.white_button)
        self.vbox.addWidget(self.blue_button)
        self.vbox.addWidget(self.red_button)

        self.line_1 = QFrame(self)
        self.line_1.setFrameShape(QFrame.HLine)
        self.line_1.setFrameShadow(QFrame.Sunken)
        self.vbox.addWidget(self.line_1)

        self.white_button2 = QRadioButton('White')
        self.white_button2.setChecked(True)
        self.blue_button2 = QRadioButton('Blue')
        self.red_button2 = QRadioButton('Red')

        self.group2 = QButtonGroup()

        self.group2.addButton(self.white_button2)
        self.group2.addButton(self.red_button2)
        self.group2.addButton(self.blue_button2)

        self.group2.buttonClicked.connect(self._on_radio_button_clicked2)

        self.vbox.addWidget(self.white_button2)
        self.vbox.addWidget(self.blue_button2)
        self.vbox.addWidget(self.red_button2)

        self.line_2 = QFrame(self)
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)
        self.vbox.addWidget(self.line_2)

        self.white_button3 = QRadioButton('White')
        self.white_button3.setChecked(True)
        self.blue_button3 = QRadioButton('Blue')
        self.red_button3 = QRadioButton('Red')

        self.group3 = QButtonGroup()

        self.group3.addButton(self.white_button3)
        self.group3.addButton(self.red_button3)
        self.group3.addButton(self.blue_button3)

        self.group3.buttonClicked.connect(self._on_radio_button_clicked3)

        self.vbox.addWidget(self.white_button3)
        self.vbox.addWidget(self.blue_button3)
        self.vbox.addWidget(self.red_button3)

        self.btn = QPushButton()
        self.btn.setText('Генерация флага')
        self.btn.clicked.connect(self.gen)
        self.vbox.addWidget(self.btn)

        self.setLayout(self.vbox)

    def _on_radio_button_clicked(self, button):
        self.color1 = self.conv[button.text()]

    def _on_radio_button_clicked2(self, button):
        self.color2 = self.conv[button.text()]

    def _on_radio_button_clicked3(self, button):
        self.color3 = self.conv[button.text()]

    def gen(self):
        self.hlst = Holst([self.color1, self.color2, self.color3])
        self.hlst.show()


class Holst(QMainWindow):
    def __init__(self, clrs):
        super(Holst, self).__init__()
        self.clrs = clrs
        self.initUI()

    def initUI(self):
        self.setGeometry(150, 150, 300, 300)

    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        self.drawFlag(qp)
        qp.end()

    def drawFlag(self, qp):
        qp.setBrush(self.clrs[0])
        qp.drawRect(30, 30, 120, 30)
        qp.setBrush(self.clrs[1])
        qp.drawRect(30, 60, 120, 30)
        qp.setBrush(self.clrs[2])
        qp.drawRect(30, 90, 120, 30)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWindow()
    ex.show()
    sys.exit(app.exec_())