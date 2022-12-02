from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QPainter, QColor
import sys
import random

SCREEN_SIZE = [430, 420]

class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("Ui.ui", self)
        self.flag = False
        self.pushButton.clicked.connect(self.draw)
        self.coords = []

    def draw(self):
        self.size = random.randint(10, 100)
        self.color = (253, 244, 0)
        self.flag = True
        self.update()

    def paintEvent(self, event):
        if self.flag:
            qp = QPainter()
            qp.begin(self)
            qp.setPen(QColor(*self.color))
            qp.setBrush(QColor(*self.color))
            self.x, self.y = random.randint(100, SCREEN_SIZE[0] - 100), random.randint(100, SCREEN_SIZE[1] - 100)
            qp.drawEllipse(self.x, self.y, self.size, self.size)
            qp.end()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec_())

