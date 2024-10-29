import tkinter as tk
from datetime import datetime
class Book:
    def __init__(self, name, author, year, genre, pages):
        self._name = name
        self._author = author
        self._year = year
        self._genre = genre
        self._pages = pages

    @staticmethod
    def isYearValidated(year):
        try:
            year = int(year)
            current_year = datetime.now().year
            return 0 < year <= current_year
        except ValueError:
            return False

    def isPagesValidated(self, pages):      
        if pages > 0 :
            return True
        else:
            print("неверно задано кол-во страниц")
            return False   

    def get_email(self):
        return self._name
    def get_email(self):
        return self._author
    def get_email(self):
        return self._year
    def get_email(self):
        return self._genre
    def get_email(self):
        return self._lists
    
    def set_name(self, name):
        self._name = name
    def set_author(self, author):
        self._author = author
    def set_genre(self, genre):
        self._genre = genre

    def set_year(self, year):
        if self.isYearValidated(year):
            self._year = year

    def set_pages(self, pages):
        if self.isPagesValidated(pages):
            self._pages = pages

    def __str__(self):
        return f"{self._name}, {self._author}, {self._year}, {self._genre}, {self._pages}"

class App:
    def __init__(self, root):
        self.root = root
        self.books = []

        self.root.title("Картотека книг")

        tk.Label(root, text="Название книги: ").pack()
        self.title_entry = tk.Entry(root)
        self.title_entry.pack()

        tk.Label(root, text="Автор: ").pack()
        self.author_entry = tk.Entry(root)
        self.author_entry.pack()

        tk.Label(root, text="Год: ").pack()
        self.year_entry = tk.Entry(root)
        self.year_entry.pack()

        tk.Label(root, text="Жанр: ").pack()
        self.genre_entry = tk.Entry(root)
        self.genre_entry.pack()

        tk.Label(root, text="Страницы: ").pack()
        self.pages_entry = tk.Entry(root)
        self.pages_entry.pack()

        add_button = tk.Button(root, text="Добавить книгу", command=self.add_book)
        add_button.pack()

        self.listbox = tk.Listbox(root, width=80, height=20)
        self.listbox.pack()

#    def add_book(self):
 #       new_book = Book(self, name, author, year, genre, pages)
  #      new_book.set_title(self.title_entry.get())
   #     new_book.set_author(self.author_entry.get())
    #    new_book.set_year(self.year_entry.get())
     #   new_book.set_genre(self.genre_entry.get())
      #  new_book.set_pages(self.pages_entry.get())

    def add_book(self):
        new_book = Book(
            self.title_entry.get(),
            self.author_entry.get(),
            self.year_entry.get(),
            self.genre_entry.get(),
            self.pages_entry.get()
            )
        
        self.books.append(new_book)
        self.listbox.insert(tk.END, str(new_book))
        
root = tk.Tk()
app = App(root)
root.mainloop()