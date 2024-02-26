import logging
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
import settings

PROXY = {'proxy_url':'socks5://t1.learn.python.ru:1080','urllib3_proxy_kwargs':{'username':'learn', 'password':'python'}}

logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s', level=logging.INFO, filename='bot.log')

def greet_user(update: Update, context: CallbackContext):
    text = 'Вызван /start'
    #print(text)
    logging.info(text)
    update.message.reply_text(text)

def echo(update: Update, context: CallbackContext):
    text = "Привет {}! Ты писал {}".format(update.message.chat.first_name, update.message.text)
    #print(update.message)
    #logging.info(update.message)
    logging.info('User: %s, Chat id: %s, Messege: %s', update.message.chat.first_name, update.message.chat.id, 
                 update.message.text)
    update.message.reply_text(text)

def main():
    mybot = Updater(settings.TOKEN)
    logging.info('Бот запускается')
    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(MessageHandler(Filters.text, echo))
    mybot.start_polling()
    mybot.idle()

#Вызов функций
main()
