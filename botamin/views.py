from typing import List

import telebot
from django.conf import settings
from django.http import JsonResponse
from django.views import View

from .models import Word

API_TOKEN = settings.API_TOKEN
TG_GROUP = settings.TG_GROUP

bot = telebot.TeleBot(API_TOKEN)


class UpdateBot(View):
    def post(self, request):
        json_str = request.body.decode('UTF-8')
        update = telebot.types.Update.de_json(json_str)
        bot.process_new_updates([update])

        return JsonResponse({'code': 200})


@bot.message_handler(func=lambda message: True, content_types=['text'])
def echo_message(message):
    if user_in_group(message.from_user.id):
        links = get_camera_list(message.text)
        if len(links):
            reply = ("\n".join(links))
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


def get_camera_list(request) -> List:
    links = []
    words = Word.objects.filter(word__icontains=request)
    for word in words:
        for link in word.link_set.all():
            links.append(link.link)
    return links
