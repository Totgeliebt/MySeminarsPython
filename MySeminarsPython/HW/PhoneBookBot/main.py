from telegram import Update, Bot
from telegram.ext import Updater, CommandHandler, CallbackContext
from bot_commands import *

bot = Bot(token='5773125696:AAEob7v8Vbrn6dp-TiW9FJwoHm9aTKTO-0c')
updater = Updater(token = '5773125696:AAEob7v8Vbrn6dp-TiW9FJwoHm9aTKTO-0c' )
updater.dispatcher.add_handler(CommandHandler('hi', hi_command))
updater.dispatcher.add_handler(CommandHandler('time', time_command))
updater.dispatcher.add_handler(CommandHandler('help', help_command))
updater.dispatcher.add_handler(CommandHandler('sum', sum_command))

print('server start')
updater.start_polling()
updater.idle()