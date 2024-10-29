height = int(input("Введите высоту: "))
for i in range(height):
    # Отступ левый
    sides = " " * (height - i - 1)
    if i == 0 or i == height - 1:
        # Верх и низ
        print(sides + "*" * (2 * i + 1))
    else:
        # Бокa
        print(sides + "*" * (2 * i) + "*")