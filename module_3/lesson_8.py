from customtkinter import *

class MainWindow(CTk):

    def __init__(self):
        super().__init__()
        self.title = 'Цвет и фигуры'
        self.geometry('500x500')

        self.grid_columnconfigure(index=(0, 1), weight=1)
        self.grid_rowconfigure(index=(0, 1, 2), weight=1)

        self.button = CTkButton(self, text='Отправить!', fg_color = 'green', command=self.show_info)
        self.button.grid(row=1, column=0, columnspan=2, padx=10, pady=10, sticky='nswe')

        self.text = CTkLabel(self, text='Сделай выбор!', justify=CENTER)
        self.text.grid(row=2, column=0, columnspan=2)

        self.checkbox = MyCheckboxFrame(self, title='Выбери цвет', values=['Красный', 'Зеленый', 'Розовый'])
        self.checkbox.grid(row=0, column=0, padx=10, pady=10, sticky='nswe')

        self.radio = MyRadioButtonFrame(self, title='Выбери фигуру', values=['Квадрат', 'Прямоугольник'])
        self.radio.grid(row=0, column=1, padx=10, pady=10, sticky='nswe')

    def show_info(self):
        self.text.configure(text=f'Цвета: {self.checkbox.get()}\n Фигуры: {self.radio.get()}')


class MyCheckboxFrame(CTkFrame):
    def __init__(self, master, title, values):
        super().__init__(master)
        self.grid_columnconfigure(index=(0), weight=1)

        self.title = CTkLabel(self, text=title, fg_color='grey30', justify=CENTER)
        self.title.grid(row=0, column=0)

        self.checkboxes = []
        for i in range(len(values)):
            checkbox = CTkCheckBox(self, text=values[i])
            checkbox.grid(row=i+1, column=0, padx=10, pady=10, sticky='we')
            self.checkboxes.append(checkbox)

    def get(self):
        selected = []
        for i in self.checkboxes:
            if i.get() == 1:
                selected.append(i.cget('text'))
        return ', '.join(selected)

class MyRadioButtonFrame(CTkFrame):

    def __init__(self, master, title, values):
        super().__init__(master)
        self.grid_columnconfigure(index=(0), weight=1)

        self.title = CTkLabel(self, text=title, fg_color='grey30', justify=CENTER)
        self.title.grid(row=0, column=0)

        self.figure = StringVar()

        for i in range(len(values)):
            radio = CTkRadioButton(self, text=values[i], value=values[i], variable=self.figure)
            radio.grid(row=i+1, column=0, padx=10, pady=10, sticky='we')

    def get(self):
        return self.figure.get()
    
window = MainWindow()
window.mainloop()