import matplotlib.pyplot as plt
import numpy as np
import math
if user_input == "1" :
    print("распределения")
    jm=float(input())
    # jm = 0
    print("отклонение")
    ot=float(input())
    # ot = 1
e=2.71828
ni=3.14
x = np.linspace(-10, 10, 100)
y = ((e**(-(((x-jm)**2)/(2*ot**2))))/((ot*(math.sqrt(2*ni)))))
# Создаем график
plt.plot(x, y)
# Добавляем название графика и осей
plt.title("График функции y = ((e**(-(((x-jm)**2)/(2*ot**2))))/((ot*(n_root(2*ni)))))")
plt.xlabel("x")
plt.ylabel("y")
# Отображаем график
plt.show()