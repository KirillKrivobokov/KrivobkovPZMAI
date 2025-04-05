import sys
import math
from PyQt5 import QtWidgets
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.figure import Figure
from LizaSHAR1 import Ui_MainWindow


class MyWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.progressBar.setValue(0)
        self.Ux.textChanged.connect(self.do_calc)
        self.uy.textChanged.connect(self.do_calc)
        self.fig = Figure()
        self.plot = FigureCanvasQTAgg(self.fig)
        box = QtWidgets.QVBoxLayout(self.graphicsView)
        box.addWidget(self.plot)
        self.graphicsView.setLayout(box)

    def do_calc(self):
        try:
            x_text = self.Ux.toPlainText()
            y_text = self.uy.toPlainText()

            if not x_text or not y_text:
                self.progressBar.setValue(0)
                return
            vx = float(x_text)
            vy = float(y_text)
            if vy <= 0:
                time = 0
                h = 0
            else:
                t_up = vy / 10
                h = vy * t_up - 5 * t_up * t_up
                t_down = math.sqrt(2 * h / 10)
                time = t_up + t_down

            final_vx = vx
            final_vy = -math.sqrt(20 * h) if vy > 0 else 0
            final_v = math.sqrt(final_vx ** 2 + final_vy ** 2)
            x_end = vx * time
            y_end = 0

            if time > 0:
                some_time = 0.5 * time
                some_vx = vx
                some_vy = vy - 10 * some_time
                some_v = math.sqrt(some_vx ** 2 + some_vy ** 2)
                v_text = "{0:.2f} м/с (на t={1:.2f} с)".format(some_v, some_time)
            else:
                v_text = "шар не взлетел"

            self.tpol.setText("{0:.2f} с".format(time))
            self.ucos.setText("{0:.2f} м/с".format(final_v))
            self.koord.setText("({0:.2f}, {1:.2f}) м".format(x_end, y_end))
            self.uz.setText(v_text)

            self.progressBar.setValue(100)

            self.make_plot(vx, vy, time)

        except:
            self.progressBar.setValue(0)
            self.tpol.setText("Ошибка")
            self.ucos.setText("Ошибка")
            self.koord.setText("Ошибка")
            self.uz.setText("Ошибка")

    def make_plot(self, vx, vy, time):
        self.fig.clear()
        graph = self.fig.add_subplot(111)

        points = 100
        times = [time * i / points for i in range(points + 1)]
        xs = [vx * t for t in times]
        ys = [max(vy * t - 5 * t * t, 0) for t in times]

        graph.plot(xs, ys, 'b-', linewidth=2)
        graph.set_title('Путь шара')
        graph.set_xlabel('X')
        graph.set_ylabel('Y')
        graph.grid(True)

        if max(xs) > 0:
            graph.set_xlim(0, max(xs) * 1.1)
        if max(ys) > 0:
            graph.set_ylim(0, max(ys) * 1.1)
        self.plot.draw()
app = QtWidgets.QApplication(sys.argv)
w = MyWindow()
w.show()
sys.exit(app.exec_())