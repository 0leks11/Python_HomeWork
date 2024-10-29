import tkinter as tk
def on_button_click():
    print("Кнопка нажата")
root = tk.Tk()
root.title("Пример приложения")
button = tk.Button(root, text="Нажми меня", command=on_button_click)
button.pack()
listbox = tk.Listbox(root)
listbox.insert(1, "Пункт 1")
listbox.insert(2, "Пункт 2")
listbox.pack()

root.mainloop()
