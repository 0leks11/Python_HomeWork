import math
def nahodim_a (x1,x2):
    return abs(x1 - x2)**2
def nahodim_b (y1,y2):
    return abs(y1 - y2)**2
def nahodim_d (x1,x2,y1,y2):
    return math.sqrt((nahodim_a (x1,x2) + nahodim_b (y1,y2)))
while True:
    print("введите nahodim_d")
    user_input=input()
    if user_input == "nahodim_d" :
        print("вв x1")
        x1=float(input())
        print("вв x2")
        x2=float(input())
        print("вв y1")
        y1=float(input())
        print("вв y2")
        y2=float(input())
        print(nahodim_d (x1,x2,y1,y2))
    else:
        print("ошибка")