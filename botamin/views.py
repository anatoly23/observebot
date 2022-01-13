import json
from typing import List

from django.conf import settings
from django.http import JsonResponse
from django.views import View

from .models import Word


class UpdateBot(View):
    def post(self, request):
        json_str = request.body.decode('UTF-8')
        req = json.loads(json_str)
        lst = get_camera_list(req['msg'])
        json_str = {'links': lst}
        return JsonResponse(json_str)


def get_camera_list(request) -> List:
    links = []
    words = Word.objects.filter(word__icontains=request)
    for word in words:
        for link in word.link_set.all():
            links.append(link.link)
    return links
