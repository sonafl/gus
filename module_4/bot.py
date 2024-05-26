import telebot
from api import get_weather, get_forecast

token = '6813552259:AAEHcz-mO9mxMJEoWd_GbG4tJ_jqaBz9Xs0'
bot = telebot.TeleBot(token)
users_city = {}
forecast = {}
@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Привет, я бот, отправляющий прогноз погоды')
    change_city(message)

def change_city(message):
    bot.send_message(message.chat.id, 'Укажите название города')
    bot.register_next_step_handler(message, save_city)

def save_city(message):
    users_city[str(message.chat.id)] = message.text
    bot.send_message(message.chat.id, 'Я сохранил твой город', reply_markup=menu())

def menu():
    keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False, row_width=3)
    btn1 = telebot.types.KeyboardButton('Текущая погода')
    btn2 = telebot.types.KeyboardButton('Сменить город')
    btn3 = telebot.types.KeyboardButton('Подробный погод на дату')
    keyboard.add(btn1, btn2, btn3)
    return keyboard

def days_button(message):
    forecast.update(get_forecast(users_city[str(message.chat.id)]))
    days = telebot.types.InlineKeyboardMarkup()
    for date in forecast.keys():
        button = telebot.types.InlineKeyboardButton(text=date, callback_data=date)
        days.add(button)
    bot.send_message(message.chat.id, 'Выберите нужную дату', reply_markup=days)

@bot.callback_query_handler(func=lambda call: ':' not in call.data)
def hour_button(call):
    date = call.data
    hours = telebot.types.InlineKeyboardMarkup()
    for hour in forecast[date].keys():
        button = telebot.types.InlineKeyboardButton(text=hour, callback_data=f'{date} {hour}')
        hours.add(button)
    bot.send_message(call.message.chat.id, 'Выберите нужное время', reply_markup=hours)

@bot.callback_query_handler(func=lambda call: ':' in call.data)
def show_forecast(call):
    date = call.data.split()[0]
    hour = call.data.split()[1]
    answer = forecast[date][hour]
    bot.send_message(call.message.chat.id, answer)

def current_weather(message):
    try:
        weather = get_weather(users_city[str(message.chat.id)])
        answer = '\n'.join(weather)
    except:
        answer = 'Погода не найдена'

    bot.send_message(message.chat.id, answer)

@bot.message_handler(content_types=['text'])
def check_text(message):
    if message.text == 'Текущая погода':
        current_weather(message)
    elif  message.text == 'Сменить город':
        change_city(message)
    elif  message.text == 'Подробный погод на дату':
        days_button(message)
    else:
        bot.reply_to(message, 'Я вас не понимаю')

bot.polling()