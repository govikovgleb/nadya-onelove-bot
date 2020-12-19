
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import CallbackQueryHandler, Filters, MessageHandler, Updater

from app.messages import MessagesGenerator
import logging

HEART_SYMBOL = "❤️"
reply_markup = InlineKeyboardMarkup([[InlineKeyboardButton(HEART_SYMBOL, callback_data="1")]])
msggen_by_user_id = {}

def get_msggen_by_user_id(user_id):
    gen = msggen_by_user_id.get(user_id)
    if not gen:
       gen = MessagesGenerator()
       msggen_by_user_id[user_id] = gen
    return gen

def btn(update, context):
    callback_query = update.callback_query
    user = callback_query.from_user
    user_id = user.id
    logging.info(f'Received click on button from {user.name} ({user_id})')
    user_ckick = get_msggen_by_user_id(user_id)
    message = user_ckick.get_msg()
    context.bot.answer_callback_query(
        callback_query_id=callback_query.id, text=message
    )


def addHeart(update, context):
    context.bot.edit_message_reply_markup(
        chat_id=update.effective_chat.id,
        message_id=update.channel_post.message_id,
        reply_markup=reply_markup,
    )


def start(token):
    updater = Updater(
        token=token, use_context=True
    )
    dispatcher = updater.dispatcher
    mirror_message = MessageHandler(Filters.photo, addHeart, channel_post_updates=True)
    inline_btn_handler = CallbackQueryHandler(btn)
    dispatcher.add_handler(inline_btn_handler)
    dispatcher.add_handler(mirror_message)
    # PUK
    updater.start_polling()
