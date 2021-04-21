import time

from telegram.ext import Updater, MessageHandler, Filters
from telegram.ext import CommandHandler
from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove

reply_keyboard = [['/start', '/time', '/date']]
markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=False)


def echo(update, context):
    update.message.reply_text(f"Я получил сообщение {update.message.text}")


def time_reply(update, context):
    update.message.reply_text(
        f"{time.asctime(time.localtime())}"[11:-4]
        , reply_markup=markup)


def date_reply(update, context):
    update.message.reply_text(
        f"{time.asctime(time.localtime())}"[:10]
        , reply_markup=markup)


def start(update, context):
    update.message.reply_text(
        "Начало работы", reply_markup=markup)


def helpp(update, context):
    pass


def main():
    updater = Updater("1719971237:AAF77V693V1ShI8PojErPcmTij-18H0L9rs", use_context=True)
    dp = updater.dispatcher

    text_handler = MessageHandler(Filters.text, echo)
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", helpp))
    dp.add_handler(CommandHandler("time", time_reply))
    dp.add_handler(CommandHandler("date", date_reply))

    dp.add_handler(text_handler)

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
