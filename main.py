import telebot

token = '7636135667:AAHEhZY1BrDb7PSEDyO5fIuCX0ZezcG6BlY'
bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def get_link(message):
    bot.send_message(message.chat.id,"Привет! Этот бот позволяет работать с Google Sheets. Отправь ссылку на твою таблицу.")

bot.polling(none_stop = True)
