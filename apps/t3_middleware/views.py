from models import HttpRequestStore
from django.shortcuts import render, HttpResponse
from django.template.loader import render_to_string
import json


def request(request):
    HttpRequestStore.objects.filter(is_viewed=False).update(is_viewed=True)
    return render(request, 't3_middleware/requests.html')


def requests_get(request):
    requests = HttpRequestStore.objects.all().order_by('-date')[:10]
    data = {
        'count': HttpRequestStore.objects.filter(is_viewed=False).count(),
        'content': render_to_string('t3_middleware/request_list.html',
                                    {'requests': requests})
        }
    return HttpResponse(json.dumps(data), content_type='application/json')
