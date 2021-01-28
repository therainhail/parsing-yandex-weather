import telebot
import config
from telebot import types
import requests
from bs4 import BeautifulSoup as BS
from beautifultable import BeautifulTable
import datetime
from PIL import Image


im = Image.open('C:/Users/Павел/PycharmProjects/Telegrambot/Yandeks.Pogoda.png')
r = requests.get('https://yandex.ru/pogoda/cheboksary?lat=56.138464&lon=47.157849')
html = BS(r.content, 'html.parser')
bot = telebot.TeleBot(config.TOKEN)


@bot.message_handler(content_types=['text'])
def mes(message):
    if message.text.lower() == 'погода':
        keyboard = types.InlineKeyboardMarkup()
        callback_button = types.InlineKeyboardButton(text="Яндекс.Погода", callback_data="test")
        keyboard.add(callback_button)
        bot.send_message(message.chat.id, "Выберите сайт чтобы узнать погоду:", reply_markup=keyboard)

@bot.callback_query_handler(func=lambda c: True)
def inline(c):
    if c.data == 'test':
        for el in html.select('.forecast-briefly__days'):
            day_t = el.select('.forecast-briefly__day_sunday .forecast-briefly__temp_day')[0].text
            night_t = el.select('.forecast-briefly__day_sunday .forecast-briefly__temp_night')[0].text

        date__today = datetime.date.today().strftime("%d.%m.%Y")
        bot.send_message(c.message.chat.id, "Яндекс.Погода" + "\n" +
                                            "Прогноз погоды на " + date__today + "\n" + day_t + " и " + night_t)

bot.polling(none_stop=True)

