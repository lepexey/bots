import telebot
import time
bot = telebot.AsyncTeleBot('1719971237:AAF77V693V1ShI8PojErPcmTij-18H0L9rs')

users = {}


@bot.message_handler(content_types=['text'])
def get_message(message):
    alert = message.text
    idd = message.chat.id
    answer = f'{str(message.chat.first_name)}. Через сколько напомнить?'
    bot.send_message(message.chat.id, text=answer)
    bot.register_next_step_handler(message, timee)
    users[idd] = [alert]


def timee(message):
    timelaps = message.text
    idd = message.chat.id
    users[idd].insert(1, timelaps)
    trust(message)


def trust(message):
    idd = message.chat.id
    timelaps = users[idd][1]
    alert = users[idd][0]
    time.sleep(int(timelaps) * 60)
    bot.send_message(message.chat.id, text=alert)


bot.polling(none_stop=True, timeout=20)