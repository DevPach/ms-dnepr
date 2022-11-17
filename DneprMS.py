

import telebot
from telebot import types

spravka = {'1616': '16168900123', '1617': '16178395805', '1618': '16188395805','1671': '16718395805',
           '1218': '12188395805','1197': '11975805'}
bot = telebot.TeleBot('5640424239:AAF6G35uWt1RBwNG61-7G8Id-VBT99seIaE')


@bot.message_handler(commands=['start'])
def start(message):
    mess = f'Hello, <b>{message.from_user.first_name} <u>{message.from_user.last_name}</u></b>'
    bot.send_message(message.chat.id, mess, parse_mode='html')


# @bot.message_handler(content_types=['text'])
# def get_text(message):
#    if message.text == 'Hello':
#        bot.send_message(message.chat.id, "Godd morning", parse_mode='html')
#    elif message.text == 'id':
#        bot.send_message(message.chat.id, f"Your Id:{message.from_user.id}", parse_mode='html')
#    elif message.text == 'photo':
#        photo = open('we.JPG', 'rb')
#        bot.send_photo(message.chat.id, photo, parse_mode='html')
#    else: bot.send_message(message.chat.id, "I'm do not anderstand you", parse_mode='html')

@bot.message_handler(content_types=['photo'])
def get_photo(message):
    bot.send_message(message.chat.id, 'yo, super photo!', parse_mode='html')


@bot.message_handler(commands=['website'])
def website(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("Посетить сайт mail", url="https://mail.ru"))
    bot.send_message(message.chat.id, 'Перейди на сайт', reply_markup=markup)


@bot.message_handler(commands=['help'])
def website(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    website = types.KeyboardButton('/website')
    start = types.KeyboardButton('Start')
    markup.add(website, start)
    bot.send_message(message.chat.id, 'Перейди на сайт', reply_markup=markup)



@bot.message_handler(commands=['/telephon'])
def get_telephon(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
    btn1 = types.KeyboardButton('1616')
    btn2 = types.KeyboardButton('1617')
    btn3 = types.KeyboardButton('1618')
    btn4 = types.KeyboardButton('1671')
    btn5 = types.KeyboardButton('1218')
    btn6 = types.KeyboardButton('1197')
    markup.add(btn1, btn2, btn3, btn4, btn5, btn6)
    send_mess = f"<b>Привет {message.from_user.first_name} {message.from_user.last_name}</b>!\nЧей телефон тебя интересует?"
    bot.send_message(message.chat.id, send_mess, parse_mode='html', reply_markup=markup)


@bot.message_handler(content_types=['text'])
def mess(message):

    if message.text == '1616':
        bot.send_message(message.chat.id, spravka['1616'], parse_mode='html')
    elif message.text == '1617':
        bot.send_message(message.chat.id, spravka['1617'], parse_mode='html')
    elif message.text == '1618':
        bot.send_message(message.chat.id, spravka['1618'], parse_mode='html')
    elif message.text == '1671':
        bot.send_message(message.chat.id, spravka['1671'], parse_mode='html')
    elif message.text == '1218':
        bot.send_message(message.chat.id, spravka['1218'], parse_mode='html')
    elif message.text == '1197':
        bot.send_message(message.chat.id, spravka['1197'], parse_mode='html')
    else: bot.send_message(message.chat.id, "I'm do not anderstand you", parse_mode='html')

#7203e415-e100-4d06-863c-c6ed5b49fa7f
#9cd0740e-39d0-48d2-a448-f42546488d94
bot.polling(none_stop=True)
