import matplotlib.pyplot as plt
import numpy as np
import math
# Генерируем значения для x и y
ot = 1
jm = 0
e=2.71828
ni=3.14
x = np.linspace(-3, 3,)
y = ((e**(-(((x-jm)**2)/(2*ot**2))))/((ot*(math.sqrt(2*ni)))))
# Создаем график
plt.plot(x, y)
# Добавляем название графика и осей
plt.title("График функции y = ((e**(-(((x-jm)**2)/(2*ot**2))))/((ot*(n_root(2*ni)))))")
plt.xlabel("x")
plt.ylabel("y")
# Отображаем график
plt.show()