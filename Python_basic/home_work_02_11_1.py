top = int(input("Введите размер : "))
side = int(input("Введите размер : "))
for i in range(top):
    for j in range(side):
        if i == 0 or i == top:
            print(top)
        elif i == 0 or j == side:
            print("*" * (side))