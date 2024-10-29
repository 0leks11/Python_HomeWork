import math
def nahodim_s (a,b,c):
    return (a + b + c)/2
def nahodim_aa (a,b,c,):
    return math.sqrt(nahodim_s (a,b,c) * (nahodim_s (a,b,c) - a) * (nahodim_s (a,b,c) - b) * (nahodim_s (a,b,c) - c))
#a = 7
#b = 3
#c = 5
#print(nahodim_aa (a,b,c,))
while True:
    print("введите nahodim_aa")
    user_input=input()
    if user_input == "nahodim_aa" :
        print("вв a")
        a=float(input())
        print("вв b")
        b=float(input())
        print("вв c")
        c=float(input())
        print(nahodim_aa (a,b,c,))
    else:
        print("ошибка")