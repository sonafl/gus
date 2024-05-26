from tkinter import *
from random import choice
# window = Tk()
# window.geometry('500x350')

# методы по адаптации виджетов по строкам и столбцам 
# for i in range(2): window.columnconfigure(index=i, weight=1) # index - номер столбца или строки
# for i in range(2): window.rowconfigure(index=i, weight=1)    # weight - доля или вес, который занимает виджет на экране 

# b1 = Button(text='Кнопочка 1')
# row - номер строки 
# сolumn - номер столбца 
# b1.grid(row=0,column=0)
#rowspan - сколько ячеек по строкам будет "отдано виджету" - объединение строк
# b2 = Button(text='Кнопочка 2')
# b2.grid(row=0,column=1, rowspan=2)
# columnspan - сколько ячеек по столбцам будет "отдано виджету" - объединение столбцов 
# b3 = Button(text='Кнопочка 3')
# b3.grid(row=1,column=0, columnspan=2)


# window.mainloop()

# Класс Game - механика игры:
# что выбрал пользователь, что выбрал компьютер, статистика игры + статус: победа, поражение или ничья

class Game:
    def __init__(self):
        # счетчики для подсчета поражений, побед и ничьих
        self.win = 0
        self.lose = 0
        self.draw = 0
        self.elements = ['Камень', 'Ножницы', 'Бумага']
    
    def start_game(self, user_choice):
        # случайный выбор компьютера 
        comp_choice = choice(self.elements)
        if comp_choice == user_choice:
            self.draw += 1
            return f'Ход игрока: {user_choice}\n Ход компьютера: {comp_choice}\n Ничья'
        elif (user_choice == 'Камень' and comp_choice == 'Ножницы') \
                        or (user_choice == 'Ножницы' and comp_choice == 'Бумага') \
                        or (user_choice == 'Бумага' and comp_choice == 'Камень'):
            self.win += 1
            return f'Ход игрока: {user_choice}\n Ход компьютера: {comp_choice}\n Победа'
        else:
            self.lose += 1
            return f'Ход игрока: {user_choice}\n Ход компьютера: {comp_choice}\n Поражение'
    
    def show_info(self):
        return f'Поражения: {self.lose}\n Побед: {self.win}\n Ничьи: {self.draw}'


class Gui:
    def __init__(self):
        # создаем окно и используем все привычные методы для реализации окна 
        self.window = Tk()
        self.window.geometry('700x600')
        self.window.title('Камень-Ножницы-Бумага')
        # создаем экземляр класса Game(), чтобы объединить механику игры и графический интерфейс
        self.game = Game()
        # вызываем метод по созданию виджетов, чтобы они поместились на окно
        self.start_gui(self.window)
        self.window.mainloop()
    
    def start_gui(self, window):
        # 3 строки, 3 столбца, применяем к ним адаптивность 
        for i in range(3): window.columnconfigure(index=i, weight=1)
        for i in range(3): window.rowconfigure(index=i, weight=1)
        # создаем кнопки, помещая их на 3 столбцах на 1 строке 
        self.b1 = Button(text='Камень', font=('Arial', 16), command = lambda: self.button_click('Камень')) # обманываем ткинтер, указывая безымянную функцию, а в ней вызываем функцию с входным параметром (в зависимости от того, какую кнопку нажали)
        self.b1.grid(row=2, column=0)
        
        self.b2 = Button(text='Ножницы', font=('Arial', 16), command = lambda: self.button_click('Ножницы'))
        self.b2.grid(row=2, column=1)

        self.b3 = Button(text='Бумага', font=('Arial', 16), command = lambda: self.button_click('Бумага'))
        self.b3.grid(row=2, column=2)

        # создаем текст со статистикой, вызывая метод из класса  Game()
        self.lb1 = Label(text=self.game.show_info(), font=('Arial', 20), justify=LEFT)
        self.lb1.grid(row=0, column=0)
        
        # создаем текст с ходом игры
        self.lb2 = Label(text='Начало игры!', font=('Arial', 24))
        self.lb2.grid(row=1, column=0, columnspan=3)
    # реализуем функцию button_click, которая будет менять ход игры и статистику в зависимости от выбора пользователя (какую кнопку нажал)
    def button_click(self, user_choice):
        # вызываем методы механики игры из Game()
        self.lb2['text'] = self.game.start_game(user_choice)
        self.lb1['text'] = self.game.show_info()

app = Gui()