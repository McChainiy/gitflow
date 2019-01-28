import sys

from PyQt5.QtWidgets import QApplication, QWidget,\
    QPushButton, QLabel, QLineEdit, QCheckBox, QVBoxLayout,\
    QPlainTextEdit, QMainWindow, QLCDNumber, QGridLayout

from PyQt5.QtCore import Qt

from math import sqrt

from PyQt5.QtGui import QFont


class NewWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setFixedSize(460, 700)
        self.move(100, 50)
        self.setWindowTitle('Kek')

        self.grid = QGridLayout()

        self.lcd = QLCDNumber(self)
        self.lcd.move(15, 15)
        self.lcd.resize(430, 100)

        self.lcd.setNumDigits(10)

        self.cur_num = 0

        self.btn7 = QPushButton(self)
        self.btn7.setText('7')
        self.btn7.resize(100, 100)
        self.btn7.move(15, 150)
        self.btn7.setFont(QFont("Arial", 20))
        self.btn7.clicked.connect(self.add_number)

        self.btn4 = QPushButton(self)
        self.btn4.setText('4')
        self.btn4.resize(100, 100)
        self.btn4.move(15, 260)
        self.btn4.setFont(QFont("Arial", 20))
        self.btn4.clicked.connect(self.add_number)

        self.btn1 = QPushButton(self)
        self.btn1.setText('1')
        self.btn1.resize(100, 100)
        self.btn1.move(15, 370)
        self.btn1.setFont(QFont("Arial", 20))
        self.btn1.clicked.connect(self.add_number)

        self.btn8 = QPushButton(self)
        self.btn8.setText('8')
        self.btn8.resize(100, 100)
        self.btn8.move(125, 150)
        self.btn8.setFont(QFont("Arial", 20))
        self.btn8.clicked.connect(self.add_number)

        self.btn5 = QPushButton(self)
        self.btn5.setText('5')
        self.btn5.resize(100, 100)
        self.btn5.move(125, 260)
        self.btn5.setFont(QFont("Arial", 20))
        self.btn5.clicked.connect(self.add_number)

        self.btn2 = QPushButton(self)
        self.btn2.setText('2')
        self.btn2.resize(100, 100)
        self.btn2.move(125, 370)
        self.btn2.setFont(QFont("Arial", 20))
        self.btn2.clicked.connect(self.add_number)

        self.btn9 = QPushButton(self)
        self.btn9.setText('9')
        self.btn9.resize(100, 100)
        self.btn9.move(235, 150)
        self.btn9.setFont(QFont("Arial", 20))
        self.btn9.clicked.connect(self.add_number)

        self.btn6 = QPushButton(self)
        self.btn6.setText('6')
        self.btn6.resize(100, 100)
        self.btn6.move(235, 260)
        self.btn6.setFont(QFont("Arial", 20))
        self.btn6.clicked.connect(self.add_number)

        self.btn3 = QPushButton(self)
        self.btn3.setText('3')
        self.btn3.resize(100, 100)
        self.btn3.move(235, 370)
        self.btn3.setFont(QFont("Arial", 20))
        self.btn3.clicked.connect(self.add_number)

        self.btn0 = QPushButton(self)
        self.btn0.setText('0')
        self.btn0.resize(210, 100)
        self.btn0.move(15, 480)
        self.btn0.setFont(QFont("Arial", 20))
        self.btn0.clicked.connect(self.add_number)

        self.btn_plus = QPushButton(self)
        self.btn_plus.setText('+')
        self.btn_plus.resize(100, 100)
        self.btn_plus.move(345, 150)
        self.btn_plus.setFont(QFont("Arial", 30))
        self.btn_plus.clicked.connect(self.do_operation)

        self.btn_minus = QPushButton(self)
        self.btn_minus.setText('-')
        self.btn_minus.resize(100, 100)
        self.btn_minus.move(345, 260)
        self.btn_minus.setFont(QFont("Arial", 30))
        self.btn_minus.clicked.connect(self.do_operation)

        self.btn_x = QPushButton(self)
        self.btn_x.setText('*')
        self.btn_x.resize(100, 100)
        self.btn_x.move(345, 370)
        self.btn_x.setFont(QFont("Arial", 30))
        self.btn_x.clicked.connect(self.do_operation)

        self.btn_div = QPushButton(self)
        self.btn_div.setText('/')
        self.btn_div.resize(100, 100)
        self.btn_div.move(345, 480)
        self.btn_div.setFont(QFont("Arial", 30))
        self.btn_div.clicked.connect(self.do_operation)

        self.btn_eq = QPushButton(self)
        self.btn_eq.setText('=')
        self.btn_eq.resize(100, 100)
        self.btn_eq.move(235, 480)
        self.btn_eq.setFont(QFont("Arial", 30))
        self.btn_eq.clicked.connect(self.do_operation)

        self.btn_c = QPushButton(self)
        self.btn_c.setText('c')
        self.btn_c.resize(100, 100)
        self.btn_c.move(15, 590)
        self.btn_c.setFont(QFont("Arial", 30))
        self.btn_c.clicked.connect(self.do_operation)

        self.btn_x1 = QPushButton(self)
        self.btn_x1.setText('x(-1)')
        self.btn_x1.resize(100, 100)
        self.btn_x1.move(125, 590)
        self.btn_x1.setFont(QFont("Arial", 30))
        self.btn_x1.clicked.connect(self.do_operation)

        self.btn_sqrt = QPushButton(self)
        self.btn_sqrt.setText("\/‾‾‾")
        self.btn_sqrt.resize(100, 100)
        self.btn_sqrt.move(235, 590)
        self.btn_sqrt.setFont(QFont("Arial", 25))
        self.btn_sqrt.clicked.connect(self.do_operation)

        self.btn_dot = QPushButton(self)
        self.btn_dot.setText('.')
        self.btn_dot.resize(100, 100)
        self.btn_dot.move(345, 590)
        self.btn_dot.setFont(QFont("Arial", 30))
        self.btn_dot.clicked.connect(self.add_number)

        self.op = False

    def add_number(self):
        if len(str(self.cur_num)) > 15:
            print('lol')
            return
        if self.sender().text() == '.':
            self.cur_num = float(self.cur_num)
            self.lcd.display('{}.{}'.format(str(self.cur_num).split('.')))
            print(self.cur_num)
            return
        point = self.sender().text()
        if self.cur_num < 0:
            self.cur_num = self.cur_num * 10 - int(point)
        else:
            self.cur_num = self.cur_num * 10 + int(point)
        print(self.cur_num)
        self.lcd.display(self.cur_num)

    def do_operation(self):
        if self.sender().text() == '+':
            self.lcd.display('plus')
            self.last_num = self.cur_num
            self.op = '+'
            self.cur_num = 0

        elif self.sender().text() == '-':
            self.lcd.display('minus')
            self.last_num = self.cur_num
            self.op = '-'
            self.cur_num = 0

        elif self.sender().text() == '*':
            self.lcd.display('*')
            self.last_num = self.cur_num
            self.op = '*'
            self.cur_num = 0

        elif self.sender().text() == '/':
            self.lcd.display('d')
            self.last_num = self.cur_num
            self.op = '/'
            self.cur_num = 0

        elif self.sender().text() == 'c':
            self.lcd.display(0)
            self.last_num = False
            self.op = False
            self.cur_num = 0

        elif self.sender().text() == 'x(-1)':
            self.last_num = False
            self.op = False
            self.cur_num *= -1
            self.lcd.display(self.cur_num)

        elif self.sender().text() == '\/‾‾‾':
            if self.cur_num < 0:
                self.lcd.display('Error')
                return
            self.last_num = False
            self.op = False
            self.cur_num = sqrt(self.cur_num)
            self.lcd.display(self.cur_num)


        elif self.sender().text() == '=':
            if self.op == '+':
                self.cur_num = int(self.cur_num) + int(self.last_num)
                self.last_num = False
                self.lcd.display(self.cur_num)

            elif self.op == '-':
                self.cur_num = int(self.last_num) - int(self.cur_num)
                self.last_num = False
                self.lcd.display(self.cur_num)

            elif self.op == '*':
                self.cur_num = int(self.last_num) * int(self.cur_num)
                self.last_num = False
                self.lcd.display(self.cur_num)

            elif self.op == '/':
                if int(self.cur_num) == 0:
                    self.lcd.display('Error')
                    return
                self.cur_num = int(self.last_num) / int(self.cur_num)
                self.last_num = False
                self.lcd.display(self.cur_num)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = NewWidget()
    ex.show()
    sys.exit(app.exec())
