import math
def nahodim_e_k (m,v):
    return m*(v**2) / 2
m=2
v=5
while True:
    print("введите nahodim_e_k джоуль")
    user_input=input()
    if user_input == "nahodim_e_k" :
        print("вв m  кг")
        m=float(input())
        print("вв v  м/с")
        v=float(input())
        print(nahodim_e_k (m,v))
    else:
        print("ошибка")