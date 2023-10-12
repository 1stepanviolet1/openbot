from telebot import TeleBot
from telebot.types import (
    InlineKeyboardMarkup,
    InlineKeyboardButton,
    ReplyKeyboardMarkup,
    ReplyKeyboardRemove,
    KeyboardButton
)

from translator import _trans_en_ru, _trans_ru_en
from users import Users
from crypto_parse import tickers

from constant.consts import (
    DATA_DELETE_FILE,
    DATA_TRANS_EN_RU,
    DATA_TRANS_RU_EN,
    ACT_FLAG,
    NONE,
    FLAG_TRANS_EN_RU,
    FLAG_TRANS_RU_EN
)

from constant.messages import *

from loguru import logger as log

_trans_vars = {
    FLAG_TRANS_EN_RU: _trans_en_ru,
    FLAG_TRANS_RU_EN: _trans_ru_en
}


def start(bot: TeleBot, session):
    _chat = session.chat.id
    bot.send_message(_chat, MESSAGE_START)
    Users.check_username_id(session.from_user.username, _chat)


def help(bot: TeleBot, session):
    _chat = session.chat.id
    bot.send_message(_chat, MESSAGE_HELP)
    Users.check_username_id(session.from_user.username, _chat)


def some_text(bot: TeleBot, session):
    _act_flag = ACT_FLAG.get(session.from_user.username)

    if _act_flag in _trans_vars:
        trans(bot, session)
    else:
        unknown_text(bot, session)


def unknown_text(bot: TeleBot, session):
    bot.send_message(session.chat.id, MESSAGE_UNKNOWN_TEXT)


def some_file(bot: TeleBot, session):
    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton('Забыть об этом', callback_data=DATA_DELETE_FILE))

    bot.send_message(session.chat.id, MESSAGE_SOME_FILE, reply_markup=markup)


def delete_some_file(bot: TeleBot, callback):
    _chat = callback.message.chat.id
    _id_msg = callback.message.message_id

    bot.delete_message(_chat, _id_msg - 1)
    bot.delete_message(_chat, _id_msg)


def get_tg_id(bot: TeleBot, session):
    _chat = session.chat.id

    bot.send_message(_chat, MESSAGE_TG_ID_GET % _chat)


def translate(bot: TeleBot, session):
    markup = InlineKeyboardMarkup()
    btn1 = InlineKeyboardButton('en-ru', callback_data=DATA_TRANS_EN_RU)
    btn2 = InlineKeyboardButton('ru-en', callback_data=DATA_TRANS_RU_EN)
    markup.row(btn1, btn2)

    bot.send_message(session.chat.id, MESSAGE_TRANSLATE, reply_markup=markup)


def __get_markup_stop():
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(KeyboardButton('/stop'))
    return markup


def send_trans(bot: TeleBot, callback):
    session = callback.message
    username = callback.from_user.username
    _chat = session.chat.id
    _id_msg = session.message_id

    bot.delete_message(_chat, _id_msg)

    if callback.data == DATA_TRANS_EN_RU:
        ACT_FLAG.set(username, FLAG_TRANS_EN_RU)
        _lang = FLAG_TRANS_EN_RU
    else:
        ACT_FLAG.set(username, FLAG_TRANS_RU_EN)
        _lang = FLAG_TRANS_RU_EN

    bot.send_message(_chat, MESSAGE_SEND_TRANS_GET % _lang, reply_markup=__get_markup_stop(), parse_mode='html')
    # bot.register_next_step_handler(session, lambda session: trans(bot, session))


def _trans_end(bot: TeleBot, session):
    ACT_FLAG.set(session.from_user.username, NONE)
    markup_remove = ReplyKeyboardRemove()

    bot.send_message(session.chat.id, MESSAGE_END_TRANS, reply_markup=markup_remove)


def trans(bot: TeleBot, session):
    _word = session.text

    if _word == '/stop':
        return _trans_end(bot, session)

    _chat = session.chat.id
    _act_flag = ACT_FLAG.get(session.from_user.username)
    markup = __get_markup_stop()

    try:
        word = _trans_vars.get(_act_flag)(_word)
    except Exception as err:
        log.error(err)
    else:
        MESSAGE_TRANS = word
    
    bot.send_message(_chat, MESSAGE_TRANS, reply_markup=markup)


def crypto_info(bot: TeleBot, session):
    _chat = session.chat.id
    
    _coins = tickers.get_valid_coin_info()
    USDT = tickers.get_USDT(_coins)
    _coins.remove(USDT)

    bot.send_message(_chat, MESSAGE_CRYPTO)

    for _coin in _coins:
        _ticker = _coin.get('ticker')
        _price = _coin.get('price')
        _marketcap = _coin.get('marketCap')
        msg = f"{_ticker} - {_price} - {_marketcap}"
        bot.send_message(_chat, msg)
    
    bot.send_message(
        _chat,
        MESSAGE_ABOUT_USDT.format(
            USDT.get('price'),
            USDT.get('marketCap')
        )
    )
