# логирование
import logging

import json
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import CallbackQueryHandler, Filters, MessageHandler, Updater

from app.messages import MessagesGenerator

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)

HEART_SYMBOL = "❤️"
reply_markup = InlineKeyboardMarkup([[InlineKeyboardButton(HEART_SYMBOL, callback_data="1")]])


def btn(update, context):
    # print('update', update)#.message.from_user.id)
    print('update', update.from)
    # print('user_id', update.message.from_user.id)
    context.bot.answer_callback_query(
        callback_query_id=update.callback_query.id, text="Hoooooiiisheee"
    )


def addHeart(update, context):
    print(update.channel_post)
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
