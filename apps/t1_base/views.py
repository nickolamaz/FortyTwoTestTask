from models import Contact
from django.shortcuts import render


def index(request):
    contact = Contact.objects.first()
    return render(request, 't1_base/index.html', {'contact': contact})
