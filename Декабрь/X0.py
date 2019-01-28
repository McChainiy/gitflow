import sys

from PyQt5.QtWidgets import QApplication, QWidget,\
    QPushButton, QLabel, QLineEdit, QCheckBox, QVBoxLayout, \
    QPlainTextEdit, QMainWindow, QLCDNumber, QGridLayout, QRadioButton, QButtonGroup

from PyQt5.QtCore import Qt

from math import sqrt

from time import sleep

from PyQt5.QtGui import QFont


class TextOut(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setFixedSize(350, 350)
        self.setWindowTitle('Result')

        if ex.winner == None:
            self.lbl1 = QLabel()
            self.lbl1.setText('НИЧЬЯ')

        self.lbl1 = QLabel()
        print(ex.winner)
        self.lbl1.setText('ПОБЕДА\nЗА\n{}'.format('НОЛИКАМИ' if ex.winner == '0' else 'КРЕСТИКАМИ'))

        self.box = QGridLayout()

        self.box.addWidget(self.lbl1)

        self.setLayout(self.box)




class NewWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()


    def initUI(self):
        self.setFixedSize(350, 350)
        self.setWindowTitle('Argue')

        self.winner = False

        self.grid = QGridLayout()
        self.grid.setSpacing(10)

        self.btns = [[False for i in range(3)] for x in range(3)]
        coords = [(i, j) for i in range(3) for j in range(3)]
        self.dic = {}
        self.zeros = True

        self.radio_button_0 = QRadioButton('0')
        self.radio_button_0.resize(40, 30)
        self.radio_button_0.setChecked(True)

        self.radio_button_x = QRadioButton('X')

        self.button_group = QButtonGroup()
        self.button_group.addButton(self.radio_button_0)
        self.button_group.addButton(self.radio_button_x)

        self.button_group.buttonClicked.connect(self.radio_clicked)

        for coord in coords:

            self.btn = QPushButton()
            self.btn.setFixedSize(100, 100)
            self.dic[self.btn] = coord
            self.btn.clicked.connect(self.do_turn)
            self.grid.addWidget(self.btn, coord[0], coord[1])

        self.grid.addWidget(self.radio_button_0, 3, 1)
        self.grid.addWidget(self.radio_button_x, 3, 2)
        self.setLayout(self.grid)

    def radio_clicked(self, button):
        if button == self.radio_button_0:
            self.zeros = True
        else:
            self.zeros = False

    def do_turn(self):
        self.radio_button_0.hide()
        self.radio_button_x.hide()
        if self.sender().text() != '':
            return
        coords = self.dic[self.sender()]
        cur_znak = '0' if self.zeros else 'X'
        self.btns[coords[0]][coords[1]] = cur_znak
        self.sender().setText(cur_znak)
        self.sender().setFont(QFont("Arial", 20))
        self.zeros = not self.zeros
        self.txt = QPlainTextEdit()
        if self.check_win(cur_znak):
            tab = '\t' * 1 + '        '
            self.txt.document().setPlainText('{}Победа \n{}{}за \n{}{}'.format(tab, tab, '   ', tab,
                'НОЛИКАМИ' if cur_znak == '0' else 'КРЕСТИКАМИ'))

        elif all([all(i) for i in self.btns]):
            self.txt.document().setPlainText('\n\n\n\n\n\n                                 НИЧЬЯ')
        else:
            return

        self.txt.setFont(QFont('Arial', 10))
        self.grid.addWidget(self.txt, 4, 0, 1, 3)

        self.new_game_button = QPushButton()
        self.new_game_button.setText('New Game')
        self.new_game_button.clicked.connect(self.new_game)
        self.grid.addWidget(self.new_game_button, 5, 0, 1, 3)
        for i in self.dic.keys():
            i.hide()

    def new_game(self):
        self.btns = [[False for i in range(3)] for x in range(3)]
        for i in self.dic.keys():
            i.show()
            i.setText('')
        self.new_game_button.hide()
        self.txt.hide()
        self.radio_button_0.show()
        self.radio_button_x.show()
        self.zeros = True


    def create_res(self):
        res = TextOut()
        res.show()

    def check_win(self, znak):
        for i in self.btns:
            if i == [znak, znak, znak]:
                return True
        for i in range(3):
            lizd = []
            for x in range(3):
                lizd.append(self.btns[x][i])
            if lizd == [znak, znak, znak]:
                return True
        if [self.btns[0][0], self.btns[1][1], self.btns[2][2]] == [znak, znak, znak]:
            return True
        if [self.btns[0][2], self.btns[1][1], self.btns[2][0]] == [znak, znak, znak]:
            return True
        return False



if __name__ == '__main__':
    while True:
        app = QApplication(sys.argv)
        ex = NewWidget()
        ex.show()
        sys.exit(app.exec())