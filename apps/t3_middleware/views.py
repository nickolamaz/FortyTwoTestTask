from models import HttpRequestStore
from django.shortcuts import render, HttpResponse
from django.template.loader import render_to_string
import json


def requests_view(request):
    requests = HttpRequestStore.objects.order_by('-priority', '-date')[:10]
    if request.is_ajax():
        if request.method == 'POST':
            HttpRequestStore.objects.update(is_viewed=True)
        elif request.method == 'GET':
            data = {
                'count': HttpRequestStore.objects.filter(
                    is_viewed=False).count(),
                'content': render_to_string('t3_middleware/request_list.html',
                                            {'requests': requests}),
                'content_count': requests.count()
                }
            return HttpResponse(json.dumps(data),
                                content_type='application/json')
    return render(request, 't3_middleware/requests.html')
