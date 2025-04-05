import sys
import math
import numpy as np
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QVBoxLayout

from main_ui import Ui_MainWindow


class Trajectory(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.figure = Figure()
        self.canvas = FigureCanvas(self.figure)

        # смена пустого виджета, костыль
        layout = QVBoxLayout(self.plot_widget)
        layout.addWidget(self.canvas)

        self.plot_button.clicked.connect(self.trajectory)

    def trajectory(self):
        try:
            v0 = float(self.U0_input.text())
            phi = float(self.phi_input.text())

            if v0 <= 0:
                raise ValueError("Error")
            if phi <= 0 or phi >= 90:
                raise ValueError("error")

            phi_rad = math.radians(phi)

            # Время полета
            t_flight = 2 * v0 * math.sin(phi_rad) / 10
            t = np.linspace(0, t_flight, 100)
            x = v0 * np.cos(phi_rad) * t
            y = v0 * np.sin(phi_rad) * t - 0.5 * 10 * t ** 2
            self.figure.clear()

            # Создаем график
            ax = self.figure.add_subplot(111)
            ax.plot(x, y)
            ax.set_xlabel('x')
            ax.set_ylabel('y')
            ax.set_title('Траектория движения тела')
            ax.grid(True)
            self.canvas.draw()

        except ValueError as e:
            QMessageBox.warning(self, "error", str(e))
        except Exception as e:
            QMessageBox.critical(self, "error", f"Cлучилось что-то странное: {str(e)}")



app = QApplication(sys.argv)
window = Trajectory()
window.show()
sys.exit(app.exec_())