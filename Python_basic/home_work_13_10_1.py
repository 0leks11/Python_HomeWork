import math
def diskreminante_d (a,b,c):
    d = b**2 - 4*a*c
    return d
def ischem_iks_x (a,b,d):
    if d > 0 :
        x1 = (-b + math.sqrt(d))/(2*a)
        x2 = (-b - math.sqrt(d))/(2*a)
        return x1, x2
    elif d == 0 :
        x = -b/(2*a)
        return x
    else: 
        print("уравнение не имеет корней")    
#a=3
#b=-14
#c=-5
#print(ischem_iks_x (a,b,d))
while True:
    print("введите nahodim_d")
    user_input=input()
    if user_input == "nahodim_d" :
        print("вв a")
        a=float(input())
        print("вв b")
        b=float(input())
        print("вв c")
        c=float(input())
        d=diskreminante_d (a,b,c)
        print(ischem_iks_x (a,b,d))
    else:
            print("ошибка")