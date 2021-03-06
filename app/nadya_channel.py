
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import CallbackQueryHandler, Filters, MessageHandler, Updater

from app.messages import MessagesGenerator
from app.storage import get_likes_count_by_post, increase_likes_count_by_post
import logging
import os

HEART_SYMBOL = "💛"
NICE_HEART_SYMBOL = "🧡"
AWESAME_HEART_SYMBOL = "❤️"
BRILIANT_HEART_SYMBOL = "💖"
reply_markup = InlineKeyboardMarkup([[InlineKeyboardButton(HEART_SYMBOL, callback_data=1)]])
msggen_by_user_id = {}

def get_msggen_by_user_id(user_id):
    gen = msggen_by_user_id.get(user_id)
    if not gen:
       gen = MessagesGenerator()
       msggen_by_user_id[user_id] = gen
    return gen

def heart_lvl(count):
    lvl = {        
        count==15: '🧡',
        count==30: '❤️',
        count==50: '💖',        
    }
    if True in lvl:
        return lvl[True]
    else:
        return False
    

def make_new_reply_markup(message_id):
    count = get_likes_count_by_post(message_id)
    logging.info(f'count {count}')    
    new_heart = heart_lvl(int(count))
    if new_heart:
        reply_markup = InlineKeyboardMarkup([[InlineKeyboardButton(new_heart, callback_data=1)]])
        return reply_markup
    else:
        return False

def btn(update, context):
    print('btn call')
    callback_query = update.callback_query
    message = callback_query.message
    message_id = message.message_id
    
    logging.info(f'Message id {message_id}')
    user = callback_query.from_user
    user_id = user.id
    logging.info(f'Received click on button from {user.name} ({user_id})')
    increase_likes_count_by_post(message_id) # write counter to json 
    
    new_reply_markup = make_new_reply_markup(message_id)
    logging.info(f'new_reply_markup {new_reply_markup}')
    if new_reply_markup:
        logging.info(f'done')
        message.edit_reply_markup(
        reply_markup=new_reply_markup
    )
    user_ckick = get_msggen_by_user_id(user_id)
    msg = user_ckick.get_msg()    
    context.bot.answer_callback_query(
        callback_query_id=callback_query.id, text=msg
    )


def addHeart(update, context):
    context.bot.edit_message_reply_markup(
        chat_id=update.effective_chat.id,
        message_id=update.channel_post.message_id,
        reply_markup=reply_markup,
    )


def start(token, use_webhooks:False):
    updater = Updater(
        token=token, use_context=True, request_kwargs={'read_timeout': 10, 'connect_timeout': 12}
    )
    TOKEN = token
    PORT = int(os.environ.get('PORT', '8443'))
    dispatcher = updater.dispatcher
    mirror_message = MessageHandler(Filters.photo, addHeart, channel_post_updates=True)
    inline_btn_handler = CallbackQueryHandler(btn)
    dispatcher.add_handler(inline_btn_handler)
    dispatcher.add_handler(mirror_message)
    # PUK
    # updater.start_polling()
    if use_webhooks:
        print('webhooks is using')
        updater.start_webhook(listen="0.0.0.0",
                                port=PORT,
                                url_path=TOKEN)
        updater.bot.set_webhook("https://nadya-onelove-bot.herokuapp.com/" + TOKEN)
        updater.idle()
    else:
        print('webhooks isn"t using')
        updater.start_polling()
