from customtkinter import *

window = CTk()
window.title('Главное окно')
window.geometry('300x400')

window.grid_columnconfigure(index=(0), weight=1)
window.grid_rowconfigure(index=(0, 1, 2, 3, 4), weight=1)

def button_click():
    global count
    count += 1
    click_label.configure(text=f'Количество нажатий: {count}')

hello = CTkLabel(window, text='Привет!')
hello.grid(row=0, column=0)
hello.cget('font').configure(size=20)

count = 0
click_label = CTkLabel(window, text=f'Количество нажатий: {count}', font=('Arial', 16))
click_label.grid(row=1, column=0)

button = CTkButton(window, text='Нажми на меня!', font=('Arial', 16), corner_radius = 5, fg_color='red', command=button_click)
button.grid(row=2, column=0, padx=20, pady=20, sticky='we')

frame = CTkFrame(window)
frame.grid(row=3, column=0, padx=10, pady=10, sticky='nswe')
frame.grid_columnconfigure(index=(0,1), weight=1)
frame.grid_rowconfigure(index=(0,1), weight=1)

checkbox_1 = CTkCheckBox(frame, text='Вариант 1')
checkbox_1.grid(row=0, column=0)

checkbox_2 = CTkCheckBox(frame, text='Вариант 2')
checkbox_2.grid(row=0, column=1)










window.mainloop()
