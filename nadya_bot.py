from telegram.ext import Updater
from telegram.ext import CommandHandler
from telegram.ext import CallbackQueryHandler
from telegram import InlineKeyboardButton
from telegram import InlineKeyboardMarkup
updater = Updater(token='1145342159:AAEwfxOCLaQleZtlsJ4X29KE_37MP_qzPSU', use_context=True)
dispatcher = updater.dispatcher

# логирование
import logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
# 
def start(update, context):
    reply_markup = InlineKeyboardMarkup([[InlineKeyboardButton("\u2764 W-o-W", callback_data='like')]]) 
    context.bot.send_message(chat_id=update.effective_chat.id, text="I love you!", reply_markup=reply_markup)
def btn(update, context):
    context.bot.answer_callback_query(callback_query_id=update.callback_query.id, text="You are beautiful!", show_alert=True)

start_handler = CommandHandler('start', start)
inline_btn_handler = CallbackQueryHandler(btn)
dispatcher.add_handler(start_handler)
dispatcher.add_handler(inline_btn_handler)

updater.start_polling()