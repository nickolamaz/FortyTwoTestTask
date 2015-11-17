from models import HttpRequestStore
from django.shortcuts import render, HttpResponse
from django.template.loader import render_to_string
from forms import RequestsFormset
from django.views.decorators.csrf import csrf_exempt
import json


@csrf_exempt
def requests_view(request):
    requests = HttpRequestStore.objects.order_by('-priority', '-date')[:10]
    if request.method == 'POST':
        if request.is_ajax():
            HttpRequestStore.objects.update(is_viewed=True)
        else:
            formset = RequestsFormset(request.POST)
            if formset.is_valid():
                formset.save()
            else:
                print formset.errors

    elif request.method == 'GET' and request.is_ajax():
        formset = RequestsFormset(queryset=requests)
        obj = zip(requests, formset)
        data = {
            'count': HttpRequestStore.objects.filter(
                is_viewed=False).count(),
            'content': render_to_string('t3_middleware/request_list.html',
                                        {'requests': requests,
                                         'formset': formset,
                                         'obj': obj
                                         }
                                        ),
            'content_count': requests.count()
            }
        return HttpResponse(json.dumps(data),
                            content_type='application/json')
    return render(request, 't3_middleware/requests.html')
