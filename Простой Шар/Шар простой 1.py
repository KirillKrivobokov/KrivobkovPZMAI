import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from math import sqrt
from LizaSHAproto1 import Ui_MainWindow


class BallFallCalculator(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.g = 10
        self.ui.textEdit.textChanged.connect(self.calculate_fall)
        self.ui.textEdit_2.textChanged.connect(self.calculate_fall)

    def calculate_fall(self):
        try:
            h0_text = self.ui.textEdit.toPlainText().strip().replace(',', '.')
            if not h0_text:
                raise ValueError
            h0 = float(h0_text)
            time_text = self.ui.textEdit_2.toPlainText().strip().replace(',', '.')
            t = float(time_text) if time_text else 0.0
            if h0 <= 0:
                raise ValueError("Высота должна быть положительной")
            t_fall = sqrt(2 * h0 / self.g)

            v_fall = self.g * t_fall

            if t < 0:
                raise ValueError("Время не может быть отрицательным")
            elif t <= t_fall:
                h = max(0, h0 - 0.5 * self.g * t ** 2)
                v = self.g * t
            else:
                h = 0
                v = v_fall
            progress = min(100, int(100 * t / t_fall)) if t_fall > 0 else 100
            self.ui.progressBar.setValue(progress)
            self.ui.label_5.setText(f"Время падения: {t_fall:.2f} с")
            self.ui.label_6.setText(f"Скорость при падении: {v_fall:.2f} м/с")
            self.ui.label_7.setText(f"Высота: {h:.2f} м")
            self.ui.label_8.setText(f"Текущая скорость: {v:.2f} м/с")

        except ValueError as e:
            self.clear_results()
        except Exception:
            self.clear_results()

    def clear_results(self):
        self.ui.label_5.setText("Время падения:")
        self.ui.label_6.setText("Скорость при падении:")
        self.ui.label_7.setText("Высота:")
        self.ui.label_8.setText("Текущая скорость:")
        self.ui.progressBar.setValue(0)


app = QtWidgets.QApplication(sys.argv)
window = BallFallCalculator()
window.setWindowTitle("Калькулятор падения шара")
window.show()
sys.exit(app.exec_())