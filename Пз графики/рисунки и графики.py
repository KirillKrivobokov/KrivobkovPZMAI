import numpy as np
import matplotlib.pyplot as plt

print('ЗДРАВСТВУЙТЕ. ЭТО КОД ДЛЯ ВЫПОЛНЕНИЯ ЗАДАНИЙ с ПАРЫ ПО ПРОГРАММИРОВАНИЮ 01.03.2025.')
print('Задание 1, 2 и 3 помечены буквами ABC. Чтобы запустить задание введите 1.')

#Задание 1
def zad1():
    x = np.linspace(-10, 10, 100)
    y1 = x
    y2 = 2 * x
    y3 = 3 * x
    y4 = x ** 2
    y5 = 2 * (x ** 2)

    plt.plot(x, y1, label='y = x', color='blue')
    plt.plot(x, y2, label='y = 2x', color='red')
    plt.plot(x, y3, label='y = 3x', color='green')
    plt.plot(x, y4, label='y = x^2', color='orange')
    plt.plot(x, y5, label='y = 2 * x^2', color='purple')
    plt.xlim(-15, 15)
    plt.ylim(-20, 50)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend()
    plt.show()
a= int(input('Выполнить задание 1? '))
if a ==1:
    print(zad1())
else:
    print('next')
#Задание 2

def zad2():
    num_GP = 5
    GP = np.random.rand(num_GP, 2) * 100
    num_SP = 10
    plt.figure(figsize=(15, 8))
    SP = [i + np.random.normal(0, 5, (num_SP, 2)) for i in GP]
    CP = np.array([np.mean(i, axis=0) for i in SP])
    POG = [np.std(i, axis=0) for i in SP]

    colors = ['blue', 'red', 'green', 'orange', 'purple']

    for i in range(len(SP)):
        plt.scatter(SP[i][:, 0], SP[i][:, 1], color=colors[i], alpha=0.6, label='Группа точек ' + str(i + 1))

    for i in range(len(CP)):
        plt.errorbar(CP[i][0], CP[i][1], xerr=POG[i][0], yerr=POG[i][1], fmt='o', color='black',
                     capsize=5, label='Центральная точка ' + str(i + 1))

    plt.scatter(GP[:, 0], GP[:, 1], color='black', marker='X', s=100, label='Начальные точки')

    plt.title('График смещенных точек')
    plt.xlabel('X координата')
    plt.ylabel('Y координата')
    plt.legend()
    plt.axis('equal')

    plt.show()
    return print('успешно')
b= int(input('Выполнить задание 2? '))
if b ==1:
    print(zad2())
else:
    print('next')

#Задание 3
с= int(input('Выполнить задание 3? '))
if b ==1:
    print('zaidite v drugoi fail')

