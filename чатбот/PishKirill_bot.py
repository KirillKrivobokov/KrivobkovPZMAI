import telebot
import random
from datetime import datetime
from telebot import types
import time

try:
    with open('key.txt', 'r') as file:
        BOT_TOKEN = file.read().strip()
    if not BOT_TOKEN:
        raise ValueError("Файл key.txt пустой")
except FileNotFoundError:
    print("Ошибка: Файл key.txt не найден")
    exit(1)

bot = telebot.TeleBot(BOT_TOKEN)

def make_buttons():
    buttons = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton('Время')
    btn2 = types.KeyboardButton('Рандомное число')
    btn3 = types.KeyboardButton('Мой ID')
    btn4 = types.KeyboardButton('Помощь')
    buttons.add(btn1, btn2, btn3, btn4)
    return buttons

@bot.message_handler(commands=['start'])
def start_bot(message):
    bot.send_message(
        message.chat.id,
        "Привет! Я PISHKIRILL ULTRA бот с временем, случайными числами и вашим ID.",
        reply_markup=make_buttons()
    )

@bot.message_handler(commands=['help'])
def show_help(message):
    help_text = (
        "Что я умею:\n"
        "/start - начать\n"
        "Время - узнать время\n"
        "Рандомное число - получить число (1-100)\n"
        "Мой ID - получить ID\n"
        "Помощь - помощь"
    )
    bot.send_message(message.chat.id, help_text)

@bot.message_handler(content_types=['text'])
def handle_text(message):
    if message.text == 'Время':
        bot.send_message(message.chat.id, f'Текущее время: {datetime.now().strftime("%H:%M:%S")}')
    elif message.text == 'Рандомное число':
        bot.send_message(message.chat.id, f'Ваше число: {random.randint(1, 100)}')
    elif message.text == 'Мой ID':
        bot.send_message(message.chat.id, f'Ваш ID: {message.from_user.id}')
    elif message.text == 'Помощь':
        show_help(message)
    elif message.text.lower() in ['привет', 'hi', 'hello']:
        bot.send_message(message.chat.id, "Привет!)")
    elif message.text == 'Dan Tkach':
        bot.send_message(message.chat.id, "Здравствуйте, DAN TKACH! Не ломайте пожалуйста мой код")
    else:
        bot.send_message(message.chat.id, "ОШИБКА. ВВЕДИТЕ ПРАВИЛЬНО ИЛИ ОЗНАКОМЬТЕСЬ С /help")



bot.polling(none_stop=True, interval=2)
