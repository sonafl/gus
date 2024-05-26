import telebot 
token = '6322061320:AAHs-eycttK7Gw9vf2GMyFQy1ZUCFXZAiEg'
# подключаемся к боту 
bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def start(message):
    keyboard = telebot.types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True, one_time_keyboard=False)
    button1 = telebot.types.KeyboardButton('Привет!')
    button2 = telebot.types.KeyboardButton('Как дела?')
    keyboard.add(button1, button2)
    bot.send_message(message.chat.id, 'Привет! Я эхо-бот теста 5 занятия!', reply_markup=keyboard)

@bot.message_handler(commands=['help'])
def help(message):
    bot.send_message(message.chat.id, 'Я пока умею только повторять за вами ваши слова)')

@bot.message_handler(commands=['goodbye'])
def goodbye(message):
    bot.send_message(message.chat.id, 'Пока-пока, до скорых встреч! Я буду всегда ждать тебя здесь))')

# декоратор по работе с сообщениями пользователя, нужно указать тип контента в сообщении или команду
@bot.message_handler(content_types=['text'])
def echo(message):
    if message.text == 'Привет!':
        text = 'Привет, милый друг!'
    elif message.text == 'Как дела?':
        text = 'Лучше не бывает!'
    else:
        text = message.text # message - объект сообщения, хранит много информации, в том числе text - само сообщение, отправленное пользователем 
    # reply_to - метод который ОТВЕЧАЕТ на сообщение пользователя 
    bot.reply_to(message, text) 

# подобие window.mainloop() - чтобы бот запускался 
bot.polling()
