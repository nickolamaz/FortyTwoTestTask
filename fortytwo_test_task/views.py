from django.template import loader, Context
from django.http import HttpResponseRedirect
from t1_base.models import Contact, ContactForm
from t3_middleware.models import HttpRequestStore
from django.shortcuts import render


def index(request):
    info = Contact.objects.get(pk=1)
    return render(request, 'index.html', {'info': info})

def request(request):
    requests = HttpRequestStore.objects.all().order_by('-date')[:10]
    return render(request, 'requests.html', {'requests': requests})