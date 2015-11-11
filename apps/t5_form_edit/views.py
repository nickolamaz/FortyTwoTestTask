from django.shortcuts import render, HttpResponse, get_object_or_404
from django.contrib.auth.decorators import login_required
from apps.t1_base.models import Contact
from forms import ContactForm
import json


@login_required
def edit(request):
    if request.method == 'POST':
        form = ContactForm(request.POST, request.FILES)
        if form.is_valid():
            response_data = {'form_saved': True, 'data': 'somedata'}
            return HttpResponse(json.dumps(response_data),
                                mimetype='multipart/form-data')
        else:
            response_data = {'form_saved': False, 'errors': form.errors}
            return HttpResponse(json.dumps(response_data),
                                mimetype='multipart/form-data')
    else:
        contact = Contact.objects.first()
        form = ContactForm(instance=contact)

    return render(request, 't5_form_edit/edit.html',
                  {'form': form, 'contact': contact})
