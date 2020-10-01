from telegram.ext import Updater
from telegram.ext import CommandHandler
from telegram import InlineKeyboardButton
from telegram import InlineKeyboardMarkup
updater = Updater(token='1145342159:AAEwfxOCLaQleZtlsJ4X29KE_37MP_qzPSU', use_context=True)
dispatcher = updater.dispatcher

# логирование
import logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
# 
def start(update, context):
    reply_markup = InlineKeyboardMarkup([[InlineKeyboardButton("Test btn", callback_data='1')]]) 
    context.bot.send_message(chat_id=update.effective_chat.id, text="I love you!", reply_markup=reply_markup)

start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)

updater.start_polling()