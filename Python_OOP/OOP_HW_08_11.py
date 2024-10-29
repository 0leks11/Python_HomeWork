class Account:
    def __init__(self, balance = 0):
        self._balance = balance # Используем подчеркивание для создания "приватного" атрибута
# Геттер для получения баланса
    def get_balance(self):
        return self._balance
    # Сеттер для установки баланса
    def set_balance(self, value):
        if value < 0:
            print("Ошибка: Баланс не может быть отрицательным.")
        else:
            self._balance = value
# Тестирование
acc = Account(100)
print(acc.get_balance()) # Выведет: 100
acc.set_balance(200)
print(acc.get_balance()) # Выведет: 200
acc.set_balance(-50) # Выведет сообщение об ошибке и не изменит баланс
