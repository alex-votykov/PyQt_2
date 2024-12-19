import sys
from PyQt6.QtGui import QPainter, QColor
from PyQt6.QtWidgets import QMainWindow, QApplication
from random import choice
from UI import *

numbers = [_ for _ in range(1, 101)]
colors = [_ for _ in range(0, 256)]


class Example(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setupUi(self)
        self.do_paint = False
        self.btn.clicked.connect(self.paint)

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            self.draw_flag(qp)
            qp.end()
        self.do_paint = False

    def paint(self):
        self.do_paint = True
        self.update()

    def draw_flag(self, qp):
        qp.setBrush(QColor(choice(colors), choice(colors), choice(colors)))
        qp.drawEllipse(choice(numbers), choice(numbers), choice(numbers), choice(numbers))

        qp.setBrush(QColor(choice(colors), choice(colors), choice(colors)))
        qp.drawEllipse(choice(numbers), choice(numbers), choice(numbers), choice(numbers))

        qp.setBrush(QColor(choice(colors), choice(colors), choice(colors)))
        qp.drawEllipse(choice(numbers), choice(numbers), choice(numbers), choice(numbers))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
