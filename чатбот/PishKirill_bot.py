import telebot
import requests
import random
import numpy as np
import matplotlib.pyplot as plt
from telebot import types
import io

bot = telebot.TeleBot('7755266056:AAHIGXnXSYylKlYidtHujhSG45aQEcceupQ')
API_KEY = '79d1ca96933b0328e1c7e3e7a26cb347'

user_data = {}

sticker_list = {
    'goida': [
        'CAACAgIAAxkBAAIBjWf9iyRZzyMSNCr7EkrCLk-cu0UDAAIVWQACSSdpSL8SJQ0c01KENgQ',
        'CAACAgIAAxkBAAIBj2f9i0hRsrwD9AOBTA2c0YlFrsnLAAK-XgACLxRhSMBBRpm1AAHlPzYE',
        'CAACAgIAAxkBAAIBk2f9i3fsqZHT7TSQBjH2A5aY1TQ2AAJiYAACsUFpSPB4XrMwSCB1NgQ',
        'CAACAgIAAxkBAAIBlWf9i4BNKpVxdl3L2yGSMnm6ZAVuAAJ-VgAC8NxgSMtxOZeyz2dHNgQ',
        'CAACAgIAAxkBAAIBl2f9i4dP7htWLU9lOdzlm3gfEft1AAKaXQACsAJhSILyyC9CKUfuNgQ',
        'CAACAgIAAxkBAAIBmWf9i5LN6uQgeQz-vqu8AhQdEnzhAALPWwACTLRhSB-tRVkmQlX_NgQ',
        'CAACAgIAAxkBAAIBm2f9i5pO6P4QDudQ39zepS-Z1XhvAAKxYAACEuNhSPj4pYJtqz9dNgQ',
        'CAACAgIAAxkBAAIBnWf9jK89It7vzPaNi4wkL54g3VR8AAJrWwACqH5hSDu7PlGWgbw7NgQ',
        'CAACAgIAAxkBAAIBoWf9jMUIMnvI6i3_b_wVEtsdCpDOAAJ1YAAC6Sf4SIO12Wu8t5LpNgQ',
        'CAACAgIAAxkBAAIBp2f9jOFfeETp6EXmo8XztA6Yom07AAKzbQACybBhSKqVole1eRSaNgQ',
        'CAACAgIAAxkBAAIBqWf9jO33H7aDwflmFUbRFhR0U28fAAJxXAACEt75SSvthXlIwj1INgQ',
        'CAACAgIAAxkBAAIBq2f9jPYacx2JtOiySDT9ddzp9CgKAAI5WQACv0j5SYVNfQSA1tWwNgQ',
        'CAACAgIAAxkBAAIBrWf9jP_cqK6At_oBgq-SLw_OQzfLAAKMYAAC38_5STAkcfWUgVSzNgQ',
        'CAACAgIAAxkBAAIBr2f9jQ5uRMUm6L7O_LzXI6m-OiT6AAIDZgACff-ASEjpE1-U_qE5NgQ',
        'CAACAgIAAxkBAAIBsWf9jRc5XI6BPQq5K5sPwYFvg9BNAAJLXQACtaaZSUL7M-CQQ0q_NgQ',
        'CAACAgIAAxkBAAIBs2f9jSCCGXJqklkalemtPsdm-nMSAAKjaQAC856ZSaKAjaemUAawNgQ',
        'CAACAgIAAxkBAAIBtWf9jS3mZFrZFRtCocSYbl5udBv3AALXVwACHnuJSMRYCB1F2QKPNgQ',
        'CAACAgIAAxkBAAIBwWf9jUJRP2EsVGxg4sFUfN5lScFuAALCZAACoEI5Sc8JaxQ_OT20NgQ',
        'CAACAgIAAxkBAAIBw2f9jU3PgyPuHSyjS39J5uP5CqgpAAKubwACwmgxSVHiIyNmAAE6uTYE',
        'CAACAgIAAxkBAAIBxWf9jVWDp_CAneQGDsEdSVuOmmy4AALdXQACuWc5SYTI1jHzvjf9NgQ',
        'CAACAgIAAxkBAAIBx2f9jV8MMOiXf-cZixOJ6ycmlR5KAAL1ZgACrWY4Sd2W-U1fsG1nNgQ',
        'CAACAgIAAxkBAAIByWf9jWvpWvjbBqtQPCAfy6ZFz41UAAKGXQACdl85SZjTrqm5dLCVNgQ',
        'CAACAgIAAxkBAAIBy2f9jXkT0U7XnJzVY1UtZa9R3E9NAAKMZAACsd85SeFysc7KHrtaNgQ',
        'CAACAgIAAxkBAAIBzWf9jYSdxWb57XnwyHmkmknz2GLUAALjbAACYMwwSYmsbibWy9tbNgQ',
        'CAACAgIAAxkBAAIBz2f9jYzoqyV-PzDbemaaripFLHCHAAJreAACqHYwSf3Kfpk2P5a6NgQ',
        'CAACAgIAAxkBAAIB92f9jnsKlV4PP5JKS6YkxGj43srJAALhVQACsCq4SoJA_2mfcoZkNgQ',
        'CAACAgIAAxkBAAIB82f9jkssx_DsePgvfKWTQ_yolblrAALaXgACe-NoSrFDlx2JFWHhNgQ',
        'CAACAgIAAxkBAAIB62f9jjUjEZbxWqMtbXqouwfGsj3TAAK8YgACFmXISlCbihextuJGNgQ',
        'CAACAgIAAxkBAAIB52f9jeVRftut_-PGFJ2puwzdeyarAAIJAANuu201zS95agN--ZE2BA',
        'CAACAgIAAxkBAAIB5Wf9jctE8m0MqH4P1jmskeAy46EJAAKPHAACJXmoSf3kLULbL1gvNgQ',
        'CAACAgIAAxkBAAIB42f9jcTxLRMUWKVGY7CETNmzPrhhAALdGAACCQ94SQfGPAOx5BlvNgQ',
        'CAACAgIAAxkBAAIB4Wf9jbnPvwg9WgWOc6OlTyZrTrWGAAKzOQACzUwBSe-wwKfZ0HOYNgQ'
    ]
}

def make_buttons():
    buttons = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton('Погода')
    btn2 = types.KeyboardButton('Стикеры')
    btn3 = types.KeyboardButton('График')
    btn4 = types.KeyboardButton('Помощь')
    buttons.add(btn1, btn2, btn3, btn4)
    return buttons

@bot.message_handler(commands=['start'])
def start_bot(message):
    bot.send_message(message.chat.id, "Привет! Я PISHKIRILL ULTRA бот с погодой, стикерами и графиками.", reply_markup=make_buttons())
    bot.send_sticker(message.chat.id, random.choice(sticker_list['hello']))

@bot.message_handler(commands=['help'])
def show_help(message):
    bot.send_message(message.chat.id, "Что я умею:\n/start - начать\nПогода - узнать погоду\nСтикеры - получить стикер\nГрафик - построить график")

def ask_for_numbers(message):
    msg = bot.send_message(message.chat.id, "Введи три числа через пробел для уравнения y = k1*x² + k2*x + k3:")
    bot.register_next_step_handler(msg, get_numbers)

def get_numbers(message):
    try:
        numbers = list(map(float, message.text.split()))
        if len(numbers) != 3:
            raise ValueError

        user_data[message.chat.id] = numbers
        draw_graph(message.chat.id)

    except:
        bot.send_message(message.chat.id, "Неправильный ввод. Нужно три числа через пробел, например: 1 -2 3")
        bot.send_sticker(message.chat.id, random.choice(sticker_list['error']))
        ask_for_numbers(message)

def draw_graph(chat_id):
    try:
        k1, k2, k3 = user_data[chat_id]

        x = np.linspace(0, 100, 400)
        y = k1 * x ** 2 + k2 * x + k3

        plt.figure(figsize=(10, 6))
        plt.plot(x, y, color='blue')
        plt.title(f'График: y = {k1}x² + {k2}x + {k3}')
        plt.xlabel('x')
        plt.ylabel('y')
        plt.grid(True)

        img = io.BytesIO()
        plt.savefig(img, format='png')
        img.seek(0)

        bot.send_photo(chat_id, img)
        plt.close()

    except Exception as e:
        bot.send_message(chat_id, f"Ошибка: {str(e)}")
        bot.send_sticker(chat_id, random.choice(sticker_list['error']))

@bot.message_handler(content_types=['text'])
def handle_text(message):
    if message.text == 'Погода':
        ask_city(message)
    elif message.text == 'Стикеры':
        send_sticker(message.chat.id)
    elif message.text == 'График':
        ask_for_numbers(message)
    elif message.text == 'Помощь':
        show_help(message)
    elif message.text.lower() in ['привет', 'hi', 'hello']:
        bot.send_message(message.chat.id, "Привет!)")
        bot.send_sticker(message.chat.id, random.choice(sticker_list['hello']))
    elif message.text == 'Dan Tkach':
        bot.send_message(message.chat.id, "Здравствуйте, DAN TKACH! Не ломайте пожалуйста мой код")
        bot.send_sticker(message.chat.id, random.choice(sticker_list['fun']))
    else:
        try:
            city = message.text
            url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&lang=ru&appid={API_KEY}'
            data = requests.get(url).json()

            if data['cod'] == 200:
                weather = data['weather'][0]['description']
                temp = data['main']['temp']
                feels = data['main']['feels_like']
                msg = f"Погода в {city}:\n{weather}\nТемпература: {temp}°C\nОщущается как: {feels}°C"
                bot.send_message(message.chat.id, msg)
            else:
                bot.send_message(message.chat.id, "Город не найден")
        except:
            bot.send_message(message.chat.id, "Ошибка")

def ask_city(message):
    msg = bot.send_message(message.chat.id, "Напиши город:")
    bot.register_next_step_handler(msg, handle_text)

def send_sticker(chat_id):
    all_stickers = []
    for v in sticker_list.values():
        all_stickers += v
    bot.send_sticker(chat_id, random.choice(all_stickers))

bot.polling(none_stop=True)