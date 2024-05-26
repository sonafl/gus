from tkinter import *

# создание окна
window = Tk()
# заголовок окна
window.title('Анкета')
# размеры окна
window.geometry('700x600')

# функция для реализации действия после нажатия кнопки
def check():
    # два способа замены параметра: 
    # label.configure(text=f'Спасибо, {entry_name.get()}')
    label['text'] = f'Спасибо, {entry_name.get()}'

# однострочный текст
label = Label(text='Расскажите о себе', font=('Arial', 25), fg='white', bg='blue')
# помещаем на окно, указывая координаты
label.place(x=250, y=15)

# многострочный текст
message = Message(text='Мы рады приветствовать вас на нашей платформе. Заполните анкету, чтобы мы познакомились!', font=('Arial', 16), width=600)
message.configure(justify=CENTER)
message.place(x=30, y=70)

name = Label(text='ФИО', font=('Arial', 14))
name.place(x=15, y=150)

# поле для ввода тектса
entry_name = Entry(width=40)
entry_name.place(x=70, y=150)

# хранится целое число в зависимости от того, какую кнопку выбрал пользователь. группирует виджеты друг с другом
selected = IntVar()
# кнопки по выбору 1 из предложенных вариантов
# value - какое значение пойдет в IntVar(), если человек выбрал эту кнопку
# variable -  переменная, в которую пойдет значение кнопки
female = Radiobutton(text='Женский', font=('Arial', 14), value=1, variable=selected)
male = Radiobutton(text='Мужской', font=('Arial', 14), value=0, variable=selected)
female.place(x=30, y=200)
male.place(x=120, y=200)

age_label = Label(text='Укажите возраст',  font=('Arial', 14))
age_label.place(x=15, y=260)

# прокручивающийся список, указываем диапазон возраста
age = Spinbox(from_=0, to=100)
age.place(x=15, y = 310)

# "поставить галочку или нет", значение выбора пользователя отправляется в check_state
check_state = IntVar()
check_1= Checkbutton(text='Запомнить меня', font=('Arial', 14), variable=check_state)
check_1.place(x=15, y=370)

# создание обыкновенной кнопки и указание действия, которое последует за нажатием (параметр command)
button = Button(text='Отправить!', font=('Arial', 16), fg='red', bg='blue', command=check)
button.place(x=280, y=420)

# метод по бесконечному запуску окна, помещается в самый конец
window.mainloop()