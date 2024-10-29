import re
class Student:
    def __init__(self, name, email):
        self._name = name
        self._email = email
    
    @staticmethod
    def validate_email(email):      
        pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
        if re.match(pattern, email):
            print("задан новый имейл " + email)
            return True
        else:
            print("неверно задан имейл ")
            return False   


    def get_email(self):
        return self._email

    def set_email(self, email):
        if self.validate_email(email):
            self._email = email
    
stu = Student("Alice", "alice@example.com")
print(stu.get_email()) # Должно вывести: alice@example.com
stu.set_email("sdsd@ceexample.com") # Должно вывести сообщение об ошибк   
print(stu.get_email())



        


        

    # реализовать самостоятельно.
    # Подсказака: почитать про регулярные выражения, Найти информацию самостоятельно как проверить формат email в питоне
    # Реализуйте геттер и сеттер для email
