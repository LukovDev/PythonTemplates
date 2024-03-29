# ----------------------------------------------------------------------------------------------------------------------
# Сборка под пк: pyinstaller -F --onefile -n NameOutputFile main.py
#
# Для работы с кодом установите эти библиотеки (просто впишите в консоль):
# pip install pyinstaller
# pip install pyTelegramBotApi
# ----------------------------------------------------------------------------------------------------------------------


# Библиотеки: --------------------------------------------------------------------------------------------------------------
if True:
	import telebot
	from telebot import types
# ----------------------------------------------------------------------------------------------------------------------


# Переменные: ----------------------------------------------------------------------------------------------------------
if True:
	token = "" # Токен бота (некий "ключ" доступа к боту).
	bot = telebot.TeleBot(token)
# ----------------------------------------------------------------------------------------------------------------------


# Функции: -------------------------------------------------------------------------------------------------------------
if True:
	# Функция ответа бота на сообщение:
	def reply(message, text):
		bot.reply_to(message, text)
# ----------------------------------------------------------------------------------------------------------------------


# Основное: ------------------------------------------------------------------------------------------------------------
if True:
	@bot.message_handler()

	# Основная функция бота:
	def main(message):
		
		# Код (Исполняется когда бот получает сообщение):
		if True:
			reply(message, message.text) # Отвечает на ваше сообщение текстом из сообщения

	bot.infinity_polling()
# ----------------------------------------------------------------------------------------------------------------------
