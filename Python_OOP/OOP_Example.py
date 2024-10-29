class Person:
    def __init__(self, name, age):
        self._name = name # Используется защищенный атрибут (одно подчеркивание)
        self._age = age
    # Геттер для имени
    def get_name(self):
        return self._name
    # Сеттер для имени
    def set_name(self, value):
        if isinstance(value, str) and len(value) > 0:
            self._name = value
        else:
            raise ValueError("Invalid name")
    # Геттер для возраста
    def get_age(self):
        return self._age
    # Сеттер для возраста
    def set_age(self, value):
        if value > 0:
            self._age = value
        else:
            raise ValueError("Age must be positive")
p = Person("Alice", 30)
print(p.get_name()) # Доступ к атрибуту через геттер
p.set_age(-5) # Попытка присвоить некорректное значение вызовет ошибку