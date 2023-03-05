import sys

from PyQt6.QtCore import Qt
from PyQt6.QtCore import QSize
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QWidget, QGridLayout, QPushButton


class Button(QPushButton):
    def __init__(self, name):
        super().__init__(name)
        self.name = name


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("кукулятор")
        self.setFixedSize(QSize(1280, 720))
        self.result = '0'
        self.label = QLabel(self.result)
        self.label.setFixedSize(1080, 100)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.layout = QGridLayout()
        self.layout.addWidget(self.label)

        self.num_1 = Button('1')
        self.num_2 = Button('2')
        self.num_3 = Button('3')
        self.num_4 = Button('4')
        self.num_5 = Button('5')
        self.num_6 = Button('6')
        self.num_7 = Button('7')
        self.num_8 = Button('8')
        self.num_9 = Button('9')
        self.num_0 = Button('0')
        self.ac = Button('AC')
        self.multiply = Button('*')
        self.divide = Button('/')
        self.plus = Button('+')
        self.minus = Button('-')
        self.ravno = Button('=')

        self.num_1.clicked.connect(lambda: self.clicked_(self.num_1.name))
        self.num_2.clicked.connect(lambda: self.clicked_(self.num_2.name))
        self.num_3.clicked.connect(lambda: self.clicked_(self.num_3.name))
        self.num_4.clicked.connect(lambda: self.clicked_(self.num_4.name))
        self.num_5.clicked.connect(lambda: self.clicked_(self.num_5.name))
        self.num_6.clicked.connect(lambda: self.clicked_(self.num_6.name))
        self.num_7.clicked.connect(lambda: self.clicked_(self.num_7.name))
        self.num_8.clicked.connect(lambda: self.clicked_(self.num_8.name))
        self.num_9.clicked.connect(lambda: self.clicked_(self.num_9.name))
        self.num_0.clicked.connect(lambda: self.clicked_(self.num_0.name))
        self.ac.clicked.connect(lambda: self.clicked_(self.ac.name))
        self.multiply.clicked.connect(lambda: self.clicked_(self.multiply.name))
        self.divide.clicked.connect(lambda: self.clicked_(self.divide.name))
        self.plus.clicked.connect(lambda: self.clicked_(self.plus.name))
        self.minus.clicked.connect(lambda: self.clicked_(self.minus.name))
        self.ravno.clicked.connect(self.equals)

        self.layout.addWidget(self.num_7, 1, 0)
        self.layout.addWidget(self.num_8, 1, 1)
        self.layout.addWidget(self.num_9, 1, 2)
        self.layout.addWidget(self.multiply, 1, 3)
        self.layout.addWidget(self.num_4, 2, 0)
        self.layout.addWidget(self.num_5, 2, 1)
        self.layout.addWidget(self.num_6, 2, 2)
        self.layout.addWidget(self.divide, 2, 3)
        self.layout.addWidget(self.num_1, 3, 0)
        self.layout.addWidget(self.num_2, 3, 1)
        self.layout.addWidget(self.num_3, 3, 2)
        self.layout.addWidget(self.plus, 3, 3)
        self.layout.addWidget(self.ac, 4, 0)
        self.layout.addWidget(self.num_0, 4, 1)
        self.layout.addWidget(self.minus, 4, 2)
        self.layout.addWidget(self.ravno, 4, 3)

        self.layout.setContentsMargins(100, 52, 100, 40)
        self.layout.setHorizontalSpacing(0)
        self.container = QWidget()
        self.container.setLayout(self.layout)
        self.setCentralWidget(self.container)

    def clicked_(self, button):
        if button == 'AC':
            self.label.setText('0')
        else:
            if self.label.text() == "0":
                self.label.setText("")

            self.label.setText(f'{self.label.text()}{button}')

    def equals(self):
        screen = self.label.text()
        try:
            answer = eval(screen)
            self.label.setText(str(answer))
        except:
            self.label.setText("беда случилась")