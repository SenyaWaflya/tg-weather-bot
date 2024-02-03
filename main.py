import telebot
import config

from telebot import types
from utils.pointdata import get_weather

bot = telebot.TeleBot(config.TOKEN)


@bot.message_handler(commands=['start'])
def send_welcome(message):
	markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
	button1 = types.KeyboardButton('🍀 Узнать погоду')
	button2 = types.KeyboardButton('🆘 Помощь')
	markup.add(button1, button2)

	sticker = open('img/sticker.webp', 'rb')
	bot.send_sticker(message.chat.id, sticker)
	bot.send_message(message.chat.id, f"Добро пожаловать, <b>{message.from_user.first_name}</b>! \n Я - <b>{bot.get_me().first_name}</b>, создан чтобы подсказать тебе погоду в любой точке мира!", parse_mode="html", reply_markup=markup)
	bot.delete_message(message.chat.id, message.message_id)


@bot.message_handler(commands=['help'])
def send_help(message):
	bot.send_message(message.chat.id, 'Если у вас возникли какие-либо вопросы, обратитесь к администратору: @Mulpe')
	bot.delete_message(message.chat.id, message.message_id)


@bot.message_handler(content_types=['text'])
def text_handler(message):
	if message.text.lower() == 'помощь' or message.text == '🆘 Помощь':
		bot.send_message(message.chat.id, 'Если у вас возникли какие-либо вопросы, обратитесь к администратору: @Mulpe')
		bot.delete_message(message.chat.id, message.message_id)
	elif message.text == '🍀 Узнать погоду' or message.text == 'Узнать погоду' or message.text == 'узнать погоду':
		keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
		loc_button = types.KeyboardButton('👁 Отправить геолокацию', request_location=True)
		keyboard.add(loc_button)
		bot.send_message(message.chat.id, 'Отправьте геолокацию места, где хотите узнать погоду.', reply_markup=keyboard)
	else:
		bot.send_message(message.chat.id, 'Я такой команды не знаю, вот список моих команд: /start, /help, Get weather.')


@bot.message_handler(content_types=['location'])
def handle_location(message):
	point = get_weather(float(message.location.latitude), float(message.location.longitude))
	bot.send_message(message.chat.id, point)


bot.polling(none_stop=True)
