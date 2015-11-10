from models import HttpRequestStore
from django.shortcuts import render


def request(request):
    requests = HttpRequestStore.objects.all().order_by('-date')[:10]
    return render(request, 't3_middleware/requests.html', {'requests': requests})
