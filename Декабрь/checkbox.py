import sys

from PyQt5.QtWidgets import QApplication, QWidget,\
    QPushButton, QLabel, QLineEdit, QCheckBox, QVBoxLayout,\
    QPlainTextEdit, QMainWindow, QGridLayout, QSlider

from PyQt5.QtCore import Qt


class NewWidget(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 200, 200)
        self.move(100, 50)
        self.setWindowTitle('MuckDuck')

        self.box_burg = QCheckBox('Burger [135]', self)
        self.box_cola = QCheckBox('Cola [95]', self)
        self.box_sauce = QCheckBox('Sauce [30]', self)
        self.box_love = QCheckBox('Fried [100]', self)
        self.box_F1 = QCheckBox('Ham [60]', self)
        self.box_sausege = QCheckBox('Chicken [145]', self)

        self.box_burg.stateChanged.connect(self.dish_add)
        self.box_cola.stateChanged.connect(self.dish_add)
        self.box_sauce.stateChanged.connect(self.dish_add)
        self.box_love.stateChanged.connect(self.dish_add)
        self.box_F1.stateChanged.connect(self.dish_add)
        self.box_sausege.stateChanged.connect(self.dish_add)




        self.dishes = {self.box_burg: [0], self.box_cola: [0], self.box_sauce: [0],
                  self.box_love: [0], self.box_F1: [0], self.box_sausege: [0]}



        accept_btn = QPushButton(self)
        accept_btn.setText('Принял')
        accept_btn.clicked.connect(self.accept_dishes)

        self.vbox = QGridLayout()
        self.vbox.addWidget(self.box_burg, 0, 0)
        self.vbox.addWidget(self.box_cola, 1, 0)
        self.vbox.addWidget(self.box_sauce, 2, 0)
        self.vbox.addWidget(self.box_love, 3, 0)
        self.vbox.addWidget(self.box_F1, 4, 0)
        self.vbox.addWidget(self.box_sausege, 5, 0)
        self.vbox.addWidget(accept_btn, 6, 0)

        self.mnss = {}
        self.plss = {}

        for i in range(6):
            mns = QPushButton()
            mns.setText('<')
            mns.setFixedSize(33, 20)
            mns.clicked.connect(self.do_change)

            pls = QPushButton()
            pls.setText('>')
            pls.setFixedSize(33, 20)
            pls.clicked.connect(self.do_change)

            lbl = QLabel()
            lbl.setText('0')

            self.vbox.addWidget(mns, i, 1)
            self.vbox.addWidget(lbl, i, 2)
            self.vbox.addWidget(pls, i, 3)

            key = list(self.dishes.keys())[i]

            self.mnss[mns] = key
            self.plss[pls] = key

            self.dishes[key].append(lbl)

        self.setLayout(self.vbox)

        print(self.dishes.items())

    def dish_add(self, state):

        sender = self.dishes[self.sender()]

        if state == Qt.Checked:
            sender[0] = 1
        else:
            sender[0] = 0

        sender[1].setText(str(sender[0]))

    def do_change(self):
        if self.sender().text() == '>':
            sender = self.dishes[self.plss[self.sender()]]
            if sender[0] == 0:
                self.plss[self.sender()].toggle()
            else:
                sender[0] += 1
            sender[1].setText(str(sender[0]))
        else:
            sender = self.dishes[self.mnss[self.sender()]]
            if sender[0] == 0:
                return
            sender[0] -= 1
            sender[1].setText(str(sender[0]))
            if sender [0] == 0:
                self.mnss[self.sender()].toggle()


    def accept_dishes(self):
        text_widget = QPlainTextEdit()
        self.vbox.deleteLater()

        texted = []
        summ = 0

        for i,x in self.dishes.items():
            if x[0] > 0:
                cur_sum = int(i.text().split('[')[1][:-1]) * x[0]
                texted.append('{} X {} = {}'.format(i.text(), x[0], cur_sum))
                summ += cur_sum
        texted.append('')
        texted.append('Итого {}'.format(summ))
        text_widget.document().setPlainText('\n'.join(texted))

        self.vbox.addWidget(text_widget)

        self.setLayout(self.vbox)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = NewWidget()
    ex.show()
    sys.exit(app.exec())
