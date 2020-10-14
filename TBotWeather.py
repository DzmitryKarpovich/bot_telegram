import telebot
import pyowm

owm = pyowm.OWM('c1341c1ae2dc777c567c862bd4b17d15')
bot = telebot.TeleBot("1288916804:AAGzhRYjprkI7MN2L0px_NytJ1TLO6AVVsE")
@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "Привет. Я тестовый бот Карповича. Могу показать погоду в городе. Напиши мне название города в сообщении." + "\n\n" + "Type a city to see a weather:")

@bot.message_handler(commands=['weather'])
def send_welcome2(message):
	bot.reply_to(message, "Type a city to see a weather:")

@bot.message_handler(content_types=['text'])
def send_weather(message):
	try:
		observation = owm.weather_manager()
		text = str(message.json['text'])
		print('\n' + text)
		w = observation.weather_at_place(text) 
		temperatura = w.weather.temperature('celsius')['temp']
		degree_sign= u'\N{DEGREE SIGN}'
		print(str(round(temperatura)) + degree_sign)
		print('----------------------------' + '\n')
		answer = "City " + message.text + ": " + '\n'
		answer += w.weather.detailed_status + '\n'
		answer += "Temperature is " + str( round(temperatura, 0) ) + degree_sign + '\n\n'
		if temperatura < 10:
			answer += 'It is terribly cold. Hold on there!'+ '\n'
			answer += 'Put on a hat !!!'
		elif temperatura < 20:
			answer+= 'It\'s cold, but bearable.'
		else:
			answer += 'The heat is there, I envy.'
	except:
		answer = 'Are you kidding?' + '\n'
		answer += 'There is no such place on the world map!'+ '\n'
		answer += 'Initial input:'+ '\n'
		answer += message.text+ '\n'
	bot.send_message(message.chat.id, answer)
bot.polling( none_stop = True )
