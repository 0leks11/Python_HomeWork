HELP = """
help - напечатать справку по программе.
add - добавить задачу в список (название задачи запрашиваем у пользователя).
show - напечатать все добавленные задачи.
exit - выйти из программы.
"""

today = []
tomorow = []
other = []

run = True

while run:
    command = input("Введите команду: ")
    if command == "help":
        print(HELP)
    elif command == "show":
        print("Сегодняшние задачи:", today)
        print("Завтрашние задачи:", tomorow)
        print("Другие задачи:", other)
    elif command == "add":
        day = input("В какой день?: ")
        if day == "today":
            task = input("Введите название задачи: ")
            today.append(task)
        elif day == "tomorow":
            task = input("Введите название задачи: ")
            tomorow.append(task)
        elif day == "other":
            task = input("Введите название задачи: ")
            other.append(task)
        print("Задача добавлена.")
    elif command == "exit":
        print("Спасибо за использование! До свидания!")
        break
    else:
        print("Неизвестная команда")
        break

print("До свидания!")