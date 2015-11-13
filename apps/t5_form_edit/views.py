from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from apps.t1_base.models import Contact
from forms import ContactForm
from django.http import HttpResponse, HttpResponseBadRequest
import apps.t8_template_tags.signals  # NOQA
import json


@login_required
def edit(request):
    if request.method == 'POST' and request.is_ajax():
        instance = Contact.objects.first()
        form = ContactForm(request.POST, request.FILES, instance=instance)
        if form.is_valid():
            form.save()
            response_data = {'form_saved': True}
            return HttpResponse(json.dumps(response_data),
                                content_type='application/json')
        else:
            response_data = {'form_saved': False, 'errors': form.errors}
            return HttpResponseBadRequest(json.dumps(response_data),
                                          content_type='application/json')
    else:
        contact = Contact.objects.first()
        form = ContactForm(instance=contact)

    return render(request, 't5_form_edit/edit.html',
                  {'form': form, 'contact': contact})
