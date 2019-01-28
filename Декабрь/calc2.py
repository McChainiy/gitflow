import sys

from PyQt5.QtWidgets import QApplication, QWidget,\
    QPushButton,  QLCDNumber, QGridLayout

from PyQt5.QtCore import Qt

from math import sqrt

from PyQt5.QtGui import QFont


class NewWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setBaseSize(1000, 10000)
        self.move(100, 50)
        self.setWindowTitle('Kek')

        self.grid = QGridLayout()

        self.lcd = QLCDNumber(self)
        self.lcd.setMinimumSize(100, 100)
        self.grid.addWidget(self.lcd, 0, 0, 1, 4)


        self.lcd.setNumDigits(15)

        self.cur_num = 0

        self.btn7 = QPushButton(self)
        self.btn7.setText('7')
        self.grid.addWidget(self.btn7, 1, 0, 1, 1)
        self.btn7.setFont(QFont("Sans", 20))
        self.btn7.clicked.connect(self.add_number)

        self.btn4 = QPushButton(self)
        self.btn4.setText('4')
        self.grid.addWidget(self.btn4, 2, 0, 1, 1)
        self.btn4.setFont(QFont("Sans", 20))
        self.btn4.clicked.connect(self.add_number)

        self.btn1 = QPushButton(self)
        self.btn1.setText('1')
        self.grid.addWidget(self.btn1, 3, 0, 1, 1)
        self.btn1.setFont(QFont("Sans", 20))
        self.btn1.clicked.connect(self.add_number)

        self.btn8 = QPushButton(self)
        self.btn8.setText('8')
        self.grid.addWidget(self.btn8, 1, 1, 1, 1)
        self.btn8.setFont(QFont("Sans", 20))
        self.btn8.clicked.connect(self.add_number)

        self.btn5 = QPushButton(self)
        self.btn5.setText('5')
        self.grid.addWidget(self.btn5, 2, 1, 1, 1)
        self.btn5.setFont(QFont("Sans", 20))
        self.btn5.clicked.connect(self.add_number)

        self.btn2 = QPushButton(self)
        self.btn2.setText('2')
        self.grid.addWidget(self.btn2, 3, 1, 1, 1)
        self.btn2.setFont(QFont("Sans", 20))
        self.btn2.clicked.connect(self.add_number)

        self.btn9 = QPushButton(self)
        self.btn9.setText('9')
        self.grid.addWidget(self.btn9, 1, 2, 1, 1)
        self.btn9.setFont(QFont("Sans", 20))
        self.btn9.clicked.connect(self.add_number)

        self.btn6 = QPushButton(self)
        self.btn6.setText('6')
        self.grid.addWidget(self.btn6, 2, 2, 1, 1)
        self.btn6.setFont(QFont("Sans", 20))
        self.btn6.clicked.connect(self.add_number)

        self.btn3 = QPushButton(self)
        self.btn3.setText('3')
        self.grid.addWidget(self.btn3, 3, 2, 1, 1)
        self.btn3.setFont(QFont("Sans", 20))
        self.btn3.clicked.connect(self.add_number)

        self.btn0 = QPushButton(self)
        self.btn0.setText('0')
        self.grid.addWidget(self.btn0, 4, 0, 1, 2)
        self.btn0.setFont(QFont("Sans", 20))
        self.btn0.clicked.connect(self.add_number)

        self.btn_plus = QPushButton(self)
        self.btn_plus.setText('+')
        self.grid.addWidget(self.btn_plus, 1, 3, 1, 1)
        self.btn_plus.setFont(QFont("Arial", 20))
        self.btn_plus.clicked.connect(self.do_operation)

        self.btn_minus = QPushButton(self)
        self.btn_minus.setText('-')
        self.grid.addWidget(self.btn_minus, 2, 3, 1, 1)
        self.btn_minus.setFont(QFont("Arial", 20))
        self.btn_minus.clicked.connect(self.do_operation)

        self.btn_x = QPushButton(self)
        self.btn_x.setText('*')
        self.grid.addWidget(self.btn_x, 3, 3, 1, 1)
        self.btn_x.setFont(QFont("Arial", 20))
        self.btn_x.clicked.connect(self.do_operation)

        self.btn_div = QPushButton(self)
        self.btn_div.setText('/')
        self.grid.addWidget(self.btn_div, 4, 3, 1, 1)
        self.btn_div.setFont(QFont("Arial", 20))
        self.btn_div.clicked.connect(self.do_operation)

        self.btn_eq = QPushButton(self)
        self.btn_eq.setText('=')
        self.grid.addWidget(self.btn_eq, 4, 2, 1, 1)
        self.btn_eq.setFont(QFont("Arial", 20))
        self.btn_eq.clicked.connect(self.do_operation)

        self.btn_c = QPushButton(self)
        self.btn_c.setText('c')
        self.grid.addWidget(self.btn_c, 5, 0, 1, 1)
        self.btn_c.setFont(QFont("Arial", 20))
        self.btn_c.clicked.connect(self.do_operation)

        self.btn_x1 = QPushButton(self)
        self.btn_x1.setText('x(-1)')
        self.grid.addWidget(self.btn_x1, 5, 1, 1, 1)
        self.btn_x1.setFont(QFont("Arial", 20))
        self.btn_x1.clicked.connect(self.do_operation)

        self.btn_sqrt = QPushButton(self)
        self.btn_sqrt.setText("\/‾‾‾")
        self.grid.addWidget(self.btn_sqrt, 5, 2, 1, 1)
        self.btn_sqrt.setFont(QFont("Arial", 20))
        self.btn_sqrt.clicked.connect(self.do_operation)

        self.btn_dot = QPushButton(self)
        self.btn_dot.setText('.')
        self.grid.addWidget(self.btn_dot, 5, 3, 1, 1)
        self.btn_dot.setFont(QFont("Arial", 20))
        self.btn_dot.clicked.connect(self.add_number)

        self.btn_fucc = QPushButton(self)
        self.btn_fucc.setText('n!')
        self.grid.addWidget(self.btn_fucc, 6, 0, 1, 2)
        self.btn_fucc.setFont(QFont("Arial", 20))
        self.btn_fucc.clicked.connect(self.do_operation)

        self.btn_step = QPushButton(self)
        self.btn_step.setText('^')
        self.grid.addWidget(self.btn_step, 6, 2, 1, 2)
        self.btn_step.setFont(QFont("Arial", 20))
        self.btn_step.clicked.connect(self.do_operation)

        self.op = False

        self.setLayout(self.grid)

        self.lcd.repaint()

    def add_number(self):
        if len(str(self.cur_num)) > 14:
            return
        if self.sender().text() == '.':
            self.cur_num = float(self.cur_num)
            self.set_dislay(str(self.cur_num)[:-1])
            return
        point = self.sender().text()
        if type(self.cur_num) is float:
            flt = str(self.cur_num).split('.')
            kf = 0 if flt[1] == '0' else 1
            ots = 10 ** (len(flt[1]) + kf)
            if self.cur_num < 0:
                self.cur_num = (self.cur_num * ots - int(point)) / ots
            else:
                self.cur_num = (self.cur_num * ots + int(point)) / ots
        else:
            ots = 0
            if self.cur_num < 0:
                self.cur_num = self.cur_num * 10 - int(point)
            else:
                self.cur_num = self.cur_num * 10 + int(point)
        self.set_dislay(self.cur_num)

    def set_dislay(self, toset):
        self.lcd.display(str(toset)[:14])

    def do_operation(self):
        if self.sender().text() == '+':
            self.set_dislay('plus')
            self.last_num = self.cur_num
            self.op = '+'
            self.cur_num = 0

        elif self.sender().text() == '-':
            self.set_dislay('minus')
            self.last_num = self.cur_num
            self.op = '-'
            self.cur_num = 0

        elif self.sender().text() == '*':
            self.set_dislay('Pl1c')
            self.last_num = self.cur_num
            self.op = '*'
            self.cur_num = 0

        elif self.sender().text() == '/':
            self.set_dislay('d')
            self.last_num = self.cur_num
            self.op = '/'
            self.cur_num = 0

        elif self.sender().text() == 'c':
            self.set_dislay(0)
            self.last_num = False
            self.op = False
            self.cur_num = 0

        elif self.sender().text() == 'x(-1)':
            self.last_num = False
            self.op = False
            self.cur_num *= -1
            self.set_dislay(self.cur_num)

        elif self.sender().text() == '\/‾‾‾':
            if self.cur_num < 0:
                self.lcd.display('Error')
                return
            self.last_num = False
            self.op = False
            self.cur_num = sqrt(self.cur_num)
            self.set_dislay(self.cur_num)

        elif self.sender().text() == 'n!':
            if self.cur_num < 0 or type(self.cur_num) is float:
                self.lcd.display('Error')
                return
            self.last_num = False
            self.op = False
            aaa = 1
            for i in range(1, self.cur_num + 1):
                aaa *= i
            self.cur_num = aaa
            self.set_dislay(aaa)

        elif self.sender().text() == '^':
            self.set_dislay('u')
            self.last_num = self.cur_num
            self.op = '^'
            self.cur_num = 0

        elif self.sender().text() == '=':
            if self.op == '+':
                self.cur_num = self.cur_num + self.last_num
                self.last_num = False
                if type(self.cur_num) is float:
                    if str(self.cur_num).split('.')[1] == '0':
                        self.cur_num = int(self.cur_num)
                self.lcd.display(self.cur_num)

            elif self.op == '-':
                self.cur_num = self.last_num - self.cur_num
                self.last_num = False
                if type(self.cur_num) is float:
                    if str(self.cur_num).split('.')[1] == '0':
                        self.cur_num = int(self.cur_num)
                self.lcd.display(self.cur_num)

            elif self.op == '*':
                self.cur_num = self.last_num * self.cur_num
                if type(self.cur_num) is float:
                    if str(self.cur_num).split('.')[1] == '0':
                        self.cur_num = int(self.cur_num)
                self.last_num = False
                self.lcd.display(self.cur_num)

            elif self.op == '/':
                if int(self.cur_num) == 0:
                    self.lcd.display('Error')
                    return
                self.cur_num = self.last_num / self.cur_num
                self.last_num = False
                self.lcd.display(self.cur_num)

            elif self.op == '^':
                self.cur_num = self.last_num ** self.cur_num
                if type(self.cur_num) is float:
                    if str(self.cur_num).split('.')[1] == '0':
                        self.cur_num = int(self.cur_num)
                self.last_num = False
                self.lcd.display(self.cur_num)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = NewWidget()
    ex.show()
    sys.exit(app.exec())
