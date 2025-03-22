from PyQt5 import QtWidgets, QtCore, QtGui
from zad1 import Ui_MainWindow
from math import sqrt, sin, cos, radians
import sys

class MyWin(QtWidgets.QMainWindow):
    def __init__(self):
        super(MyWin, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.btnClicked)

        self.scene = QtWidgets.QGraphicsScene(self)
        self.ui.graphicsView.setScene(self.scene)

    def proverka(self, input_str):
        try:
            return float(input_str)
        except ValueError:
            return None

    def btnClicked(self):
        try:
            U0 = self.proverka(self.ui.lineEdit.text())
            theta = self.proverka(self.ui.lineEdit_2.text())
            t = self.proverka(self.ui.lineEdit_3.text())

            if U0 is not None and t is not None and theta is not None:
                if 0 < U0 < 1000 and 0 < t < 1000 and 0 < theta < 90:
                    theta_rad = radians(theta)


                    TT = (2 * U0 * sin(theta_rad)) / 10
                    self.ui.TT.setText(f"{TT:.2f}")


                    if t > TT:
                        self.ui.er2.setText('Введенное время превышает время полета.')
                        self.ui.er1.setText(f'Максимальное время полета: {TT:.2f} сек')
                        t = TT


                    Uu = U0
                    self.ui.Uu.setText(f"{Uu:.2f}")
                    X = U0 * cos(theta_rad) * t
                    Y = U0 * sin(theta_rad) * t - 5 * t * t
                    self.ui.X1.setText(f"{X:.2f}")
                    self.ui.Y1.setText(f"{Y:.2f}")
                    Ut = sqrt((U0 * cos(theta_rad)) ** 2 + (U0 * sin(theta_rad) - 10 * t) ** 2)
                    self.ui.Ut.setText(f"{Ut:.2f}")


                    self.scene.clear()
                    self.track(U0, theta_rad, t)

                else:
                    self.ui.er2.setText('Вы ввели что-то странное.....')
                    self.ui.er1.setText('Не заходите сюда больше пожалуйста')

            else:
                self.ui.er2.setText('Вы ввели что-то странное.....')
                self.ui.er1.setText('Не заходите сюда больше пожалуйста')

        except Exception as e:
            self.ui.er2.setText('Вы ввели что-то странное.....')
            self.ui.er1.setText('Не заходите сюда больше пожалуйста')

    def track(self, U0, theta, t_max):
        points = []
        for t in range(0, int(t_max * 100)):
            t_sec = t / 100
            x = U0 * cos(theta) * t_sec
            y = U0 * sin(theta) * t_sec - 5 * t_sec * t_sec
            if y < 0:
                y = 0
            points.append(QtCore.QPointF(x, -y))

        if points:
            path = QtGui.QPainterPath()
            path.moveTo(points[0])
            for point in points[1:]:
                path.lineTo(point)
            self.scene.addPath(path, QtGui.QPen(QtCore.Qt.blue, 2))

            self.scene.addLine(0, 0, max(p.x() for p in points) + 50, 0, QtGui.QPen(QtCore.Qt.black, 1))
            self.scene.addLine(0, 0, 0, -max(abs(p.y()) for p in points) - 50, QtGui.QPen(QtCore.Qt.black, 1))

app = QtWidgets.QApplication([])
window = MyWin()
window.show()
sys.exit(app.exec())