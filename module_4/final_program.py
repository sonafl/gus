import telebot
import random

token = '7049016817:AAFQwoIZxtb98k6UO2DKAG0ovMvbjeSHGOQ'
bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def start(message):
    keyboard = telebot.types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True, one_time_keyboard=False)
    button_1 = telebot.types.KeyboardButton('Привет')
    button_2 = telebot.types.KeyboardButton('Как дела?')
    button_3 = telebot.types.KeyboardButton('Расскажи интересный факт')
    keyboard.add(button_1, button_2, button_3)
    bot.send_message(message.chat.id, 'Добрый день! Я небольшой эхо-бот.', reply_markup=keyboard)

@bot.message_handler(commands=['help'])
def about(message):
    bot.send_message(message.chat.id, 'Пока что я умею только повторять за вами :)')

@bot.message_handler(commands=['goodbye'])
def goodbuy(message):
    bot.send_message(message.chat.id, 'До свидания, приятно было с вами поболтать!')

@bot.message_handler(content_types=['text'])
def echo(message):
    if message.text == 'Привет':
        text = 'И тебе привет!'
    elif message.text == 'Как дела?':
        text = 'Все супер! А у тебя как?'
    elif message.text == 'Расскажи интересный факт':
        facts = [
            'Хамелеоны могут двигать глазами в разных направлениях одновременно.',
            'Электрический угорь может вырабатывать  энергию, способную зажечь 12 лампочек',
            'Морские котики могут задерживать дыхание на два часа.'
        ]
        text = random.choice(facts)
    else:
        text = message.text
    bot.reply_to(message, text)

bot.polling()

