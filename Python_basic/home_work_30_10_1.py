import math
def main():
    # Ввод числа x,a
    x = float(input("Введите число x: "))
    a = float(input("Введите число a: "))
    def funkcii(a,x,pi=3.14):
        y = 4*(math.cos(a*x*pi))**2
        return y
    print(funkcii(a,x,pi=3.14))
main()