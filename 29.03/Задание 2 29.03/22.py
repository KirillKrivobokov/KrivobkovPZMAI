import sys
import numpy as np
from PyQt5 import QtWidgets
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from main2 import Ui_MainWindow


class Collebations(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.figure = Figure()
        self.canvas = FigureCanvas(self.figure)

        # Опть заменя на канвас
        layout = QtWidgets.QVBoxLayout(self.widget)
        layout.addWidget(self.canvas)

        self.plotButton.clicked.connect(self.plot_harmonic)


        self.plot_harmonic()

    def plot_harmonic(self):
        try:
            A = float(self.amplitudeEdit.text())
            f = float(self.frequencyEdit.text())
            phi_deg = float(self.phaseEdit.text())
            phi = np.deg2rad(phi_deg)
            t = np.linspace(0, 2, 1000)
            x = A * np.sin(2 * np.pi * f * t + phi)


            self.figure.clear()

            ax = self.figure.add_subplot(111)
            ax.plot(t, x)

            self.canvas.draw()

        except ValueError:
            QtWidgets.QMessageBox.warning(self, 'Ошибка', 'ошибка')


app = QtWidgets.QApplication(sys.argv)
window = Collebations()
window.show()
sys.exit(app.exec_())