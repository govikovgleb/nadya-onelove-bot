from telegram.ext import Updater
from telegram.ext import CommandHandler
updater = Updater(token='1145342159:AAEwfxOCLaQleZtlsJ4X29KE_37MP_qzPSU', use_context=True)
dispatcher = updater.dispatcher

# логирование
import logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
# 
def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="I'm a bot, please talk to me!")

start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)

updater.start_polling()