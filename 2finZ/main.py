from PyQt5 import QtWidgets
from main_ui import Ui_MainWindow
import sys
import matplotlib.pyplot as plt
import random


class my_win(QtWidgets.QMainWindow):
    def __init__(self):
        super(my_win, self).__init__()  # наследование атрибутов из QMainWindow
        self.ui = Ui_MainWindow()  # cоздание ui
        self.ui.setupUi(self)  # создание приложения
        self.ui.pushButton.clicked.connect(self.generate_random)
        self.ui.pushButton_2.clicked.connect(self.plot)

    def generate_random(self):
        self.Znach = [random.randint(1, 20) for i in range(10)]
        self.ui.lineEdit.setText(', '.join(map(str, self.Znach)))

    def plot(self):
        try:
            input_text = self.ui.lineEdit.text()
            if not input_text:
                self.ui.label_4.setText('Введите значения через запятую')
                return

            self.Znach = [float(x.strip()) for x in input_text.split(',') if x.strip()]

            if not self.Znach:
                self.ui.label_4.setText('Не удалось, попробуйте еще раз')
                return

            plt.figure(figsize=(8, 5))
            plt.hist(self.Znach, bins=20, color='red', edgecolor='black')
            plt.title('Гистограмма значений', fontsize=12)
            plt.xlabel('Значение', fontsize=10)
            plt.ylabel('Частота появления', fontsize=10)
            plt.show()

        except ValueError:
            self.ui.label_4.setText('Вводите только числа, разделенные запятыми')


app = QtWidgets.QApplication(sys.argv)
window = my_win()
window.show()
sys.exit(app.exec_())