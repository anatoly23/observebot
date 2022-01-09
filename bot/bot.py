import os

import requests
import telebot
from dotenv import load_dotenv

load_dotenv()

API_TOKEN = os.getenv('TELEBOT_BOT_TOKEN')
TG_GROUP = os.getenv('GROUP_CHAT_ID')

bot = telebot.TeleBot(API_TOKEN)


@bot.message_handler(func=lambda message: True, content_types=['text'])
def echo_message(message):
    if user_in_group(message.from_user.id):
        req = requests.post('http://127.0.0.1:8000/webhooks/observebot/', json={"msg": message.text})
        links = req.json()
        if len(links['links']):
            reply = ("\n".join(links['links']))
            bot.send_message(message.chat.id, reply)
        else:
            bot.send_message(message.chat.id, 'К сожалению ничего не найдено, уточните запрос')
    else:
        bot.send_message(message.chat.id, 'Вы не подписаны на канал. Подпишитесь и повторите запрос')


def user_in_group(userid) -> bool:
    try:
        bot.get_chat_member(TG_GROUP, userid)
        return True
    except telebot.apihelper.ApiTelegramException:
        return False


bot.infinity_polling()
