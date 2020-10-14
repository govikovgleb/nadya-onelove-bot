from telegram.ext import Updater
from telegram.ext import CommandHandler
from telegram.ext import MessageHandler
from telegram.ext import CallbackQueryHandler
from telegram.ext import Filters
from telegram import InlineKeyboardButton
from telegram import InlineKeyboardMarkup
updater = Updater(token='1145342159:AAEwfxOCLaQleZtlsJ4X29KE_37MP_qzPSU', use_context=True)
dispatcher = updater.dispatcher

# логирование
import logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

heart = "\u2764"
array_counter = []
counter = 1
reply_markup = InlineKeyboardMarkup([[InlineKeyboardButton(heart, callback_data='1')]])

def start(update, context):        
    context.bot.send_message(chat_id=update.effective_chat.id, text="I love you!", reply_markup=reply_markup)

def btn(update, context):
    msg_id = update.callback_query.message.message_id
    if not array_counter[msg_id]:
        array_counter[msg_id] = counter
        pass 
    str_counter = str(array_counter[msg_id])
    counter_RM = InlineKeyboardMarkup([[InlineKeyboardButton(heart+" "+str_counter, callback_data='1')]])
    context.bot.edit_message_reply_markup(chat_id=update.effective_chat.id, message_id=msg_id, reply_markup=counter_RM)    
    context.bot.answer_callback_query(callback_query_id=update.callback_query.id, text="You are beautiful!")
    array_counter[msg_id] = array_counter[msg_id] + 1

def mirror(update, context):
    if update.message.text != '/start':       
        context.bot.send_message(chat_id=update.effective_chat.id, text=update.message.text, reply_markup=reply_markup)
        pass

start_handler = CommandHandler('start', start)
mirror_message = MessageHandler(Filters.all, mirror)
inline_btn_handler = CallbackQueryHandler(btn)
dispatcher.add_handler(start_handler)
dispatcher.add_handler(inline_btn_handler)
dispatcher.add_handler(mirror_message)

updater.start_polling()