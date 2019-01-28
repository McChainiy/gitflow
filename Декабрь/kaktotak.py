import sys

from PyQt5.QtWidgets import QApplication, QWidget,\
    QPushButton, QLabel, QLineEdit, QCheckBox, QVBoxLayout


class NewWidget(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 200, 200)
        self.move(100, 50)
        self.setWindowTitle('darova')

        self.btn = QPushButton('click ME', self)
        self.btn.move(50, 75)
        self.btn.resize(100, 50)

        self.clicked = True
        self.btn.clicked.connect(self.dont_click)

        self.btn2 = QPushButton('DONT click ME', self)
        self.btn2.move(50, 150)
        self.btn2.resize(100, 50)

        self.clicked2 = False
        self.btn2.clicked.connect(self.dont_click)

        self.label_greetings = QLabel(self)
        self.label_greetings.setText('Привет, неопознаный лев')
        self.label_greetings.move(20, 15)
        self.label_greetings.resize(1000, 20)

        self.label_input_name = QLabel(self)
        self.label_input_name.setText('Введи имя')
        self.label_input_name.move(40, 53)

        self.input_name = QLineEdit(self)
        self.input_name.move(100, 50)
        self.input_name.resize(95, 20)


    def dont_click(self):
        user_name = self.input_name.text()
        self.label_greetings.setText('Ну здравствуй, {}'.format(user_name))

        if self.sender() == self.btn:
            if self.clicked:
                self.clicked2 = True
                self.btn2.setText('click ME')
                self.clicked = False
                self.btn.setText('DO NOT click ME')
            else:
                self.close()
        else:
            if self.clicked2:
                self.clicked2 = False
                self.btn2.setText('DO NO click ME')
                self.clicked = True
                self.btn.setText('click ME')
            else:
                self.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = NewWidget()
    ex.show()
    sys.exit(app.exec())