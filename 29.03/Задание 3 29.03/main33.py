import sys
import numpy as np
from PyQt5 import QtWidgets
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from main3 import Ui_MainWindow


class COLLING(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.figure = Figure(figsize=(10, 6))
        self.canvas = FigureCanvas(self.figure)
        layout = QtWidgets.QVBoxLayout(self.widget)
        layout.addWidget(self.canvas)

        self.pushButton.clicked.connect(self.coling)
    def coling(self):
        try:
            T0 = float(self.t0Edit.toPlainText())
            Tenv = float(self.tenvEdit.toPlainText())
            k = float(self.kEdit.toPlainText())


            t = np.linspace(0, 50, 500)
            T = Tenv + (T0 - Tenv) * np.exp(-k * t)

            self.figure.clear()
            ax = self.figure.add_subplot(111)
            ax.plot(t, T, 'r-', linewidth=4)
            ax.grid(True)

            self.canvas.draw()

        except ValueError:

            self.label_5.setText(" введите числа правильно!")



app = QtWidgets.QApplication(sys.argv)
window = COLLING()
window.show()
sys.exit(app.exec_())