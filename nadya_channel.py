from telegram.ext import Updater
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
reply_markup = InlineKeyboardMarkup([[InlineKeyboardButton(heart, callback_data='1')]])

def btn(update, context):       
    context.bot.answer_callback_query(callback_query_id=update.callback_query.id, text="You are beautiful!")    

def addHeart(update, context):
    print(update.channel_post)
    context.bot.edit_message_reply_markup(chat_id=update.effective_chat.id, message_id=update.channel_post.message_id, reply_markup=reply_markup)

mirror_message = MessageHandler(Filters.photo, addHeart, channel_post_updates=True)
inline_btn_handler = CallbackQueryHandler(btn)
dispatcher.add_handler(inline_btn_handler)
dispatcher.add_handler(mirror_message)

updater.start_polling()