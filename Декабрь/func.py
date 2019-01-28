from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget,\
    QLineEdit, QLabel, QPushButton, QTableWidget, QTableWidgetItem
from PyQt5.QtGui import QFont
import pyqtgraph as pg
import sys


class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(100, 100, 300, 200)

        font = QFont()
        font.setPointSize(12)
        font.setWeight(50)

        self.func = QLineEdit(self)
        self.func.setGeometry(100, 50, 150, 20)

        self.fx = QLabel('f(x) ', self)
        self.fx.setGeometry(50, 50, 50, 20)
        self.fx.setFont(font)

        self.accept_btn = QPushButton(self)
        self.accept_btn.clicked.connect(self.accept)
        self.accept_btn.setGeometry(110, 145, 100, 50)
        self.accept_btn.setText('Принять')

    def accept(self):
        self.tab = Table(self.func.text(), self.point.text(), self.count.text(), self.d.text())
        self.tab.show()


class Table(QMainWindow):
    def __init__(self, func, point, count, d):
        super(Table, self).__init__()
        self.func = func
        self.point = float(point)
        self.count = int(count)
        self.d = int(d)
        self.initUI()

    def initUI(self):
        if False:
            self.tbl = QTableWidget(self)
            height = self.count * 30 + 50
            self.setGeometry(150, 150, 250, height + 20 if height < 720 else 750)
            self.tbl.setGeometry(10, 10, 225, height if height < 720 else 720)
            self.tbl.setRowCount(self.count)
            self.tbl.setColumnCount(2)
            self.tbl.setItem(0, 0, QTableWidgetItem("a"))

            a = [self.point]
            for i in range(self.count):
                a.append(a[-1] + self.d)

            for count, i in enumerate(a):
                try:
                    self.tbl.setItem(count, 0, QTableWidgetItem(str(i)))
                    self.tbl.setItem(count, 1, QTableWidgetItem(str(calc(sort(parse(self.func, i))))))
                except Exception:
                    self.tbl.setItem(count, 0, QTableWidgetItem('Error'))
                    self.tbl.setItem(count, 1, QTableWidgetItem('Error'))

        y1 = [0, -1, -2, -3, -4, -5]
        x1 = [1, 2, 3, 4, 5, 6]
        self.widget = pg.GraphicsWindow()
        p1 = self.widget.addPlot(title='Plot1')
        curve1 = p1.plot([1,2pen='b')

OPERATORS = {'+': (1, lambda x, y: x + y), '-': (1, lambda x, y: x - y),
             '*': (2, lambda x, y: x * y), '/': (2, lambda x, y: x / y),
             '^': (3, lambda x, y: x ** y)}


def parse(line, x):
    num = ''
    skip = False
    for i in line:
        if i == 'x':
            yield float(x)
            skip = True
            continue
        if not num and i == '-' and not skip:
            num += i
            continue
        skip = False
        if i in '1234567890.':
            num += i
        elif num:
            yield float(num)
            num = ''
        if i in OPERATORS or i in '()':
            yield i
    if num:
        yield float(num)


def sort(parsed):
    tmp = []
    for i in parsed:
        if i in OPERATORS:
            while tmp and tmp[-1] != '(' and OPERATORS[i][0] <= OPERATORS[tmp[-1]][0]:
                yield tmp.pop()
            tmp.append(i)
        elif i == ')':
            while tmp:
                x = tmp.pop()
                if x == '(':
                    break
                yield x
        elif i == '(':
            tmp.append(i)
        else:
            yield i
    while tmp:
        yield tmp.pop()


def calc(sort):
    tmp = []
    for i in sort:
        if i in OPERATORS:
            y = tmp.pop()
            x = tmp.pop()
            tmp.append(OPERATORS[i][1](x, y))
        else:
            tmp.append(i)
    return tmp[0]


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWindow()
    ex.show()
    sys.exit(app.exec_())
