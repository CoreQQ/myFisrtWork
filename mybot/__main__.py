import telebot
from telebot import types

TOKEN = '2112718081:AAGrgQ5SoyRYvXVTPVU2NtvmEhyLQTJAmdQ'

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
	markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
	item1 = types.KeyboardButton('Какая погода сегодня?')
	item2 = types.KeyboardButton('Помощь!')
	item3 = types.KeyboardButton('Как дела?')
	item4 = types.KeyboardButton('Что ты там?')

	markup.add(item1, item2, item3, item4)

	bot.send_message(message.chat.id, 'Привет пупсик'.format(message.from_user), reply_markup = markup)

@bot.message_handler(content_types=['text'])
def bot_message(message):
	if message.chat.type == 'private':
		if message.text == 'Какая погода сегодня?':
			bot.send_message(message.chat.id, 'Погода сегодня пасмурная😔')
		elif message.text == 'Как дела?':
			markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
			item1 = types.KeyboardButton('У меня тоже дела супер')
			item2 = types.KeyboardButton('Помощь!')
			back = types.KeyboardButton('Назад<--')
			markup.add(item1, item2, back)

			bot.send_message(message.chat.id, 'У меня всё супер, у тебя как?', reply_markup = markup)

		elif message.text == 'Помощь!':
			markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
			item1 = types.KeyboardButton('У меня появились проблемы с твоим использованием...')
			item2 = types.KeyboardButton('Как мне тебя отблагодарить?)')
			back = types.KeyboardButton('Назад<--')
			markup.add(item1, item2, back)

			bot.send_message(message.chat.id, 'С чем тебе помочь, пупсик?', reply_markup=markup)

		elif message.text == 'Назад<--':
			markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
			item1 = types.KeyboardButton('Какая погода сегодня?')
			item2 = types.KeyboardButton('Помощь!')
			item3 = types.KeyboardButton('Как дела?')
			item4 = types.KeyboardButton('Что ты там?')

			markup.add(item1, item2, item3, item4)

			bot.send_message(message.chat.id, 'Назад<--', reply_markup=markup)
bot.polling(none_stop=True)


