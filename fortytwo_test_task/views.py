from django.template import loader, Context
from django.http import HttpResponseRedirect
from t1_base.models import Contact, ContactForm
from t3_middleware.models import HttpRequestStore
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout as _logout

def index(request):
    contact = Contact.objects.get(pk=1)
    return render(request, 'index.html', {'contact': contact})

def request(request):
    requests = HttpRequestStore.objects.all().order_by('-date')[:10]
    return render(request, 'requests.html', {'requests': requests})

@login_required
def edit(request, template_name='edit.html'):
    contact = get_object_or_404(Contact)
    if request.method == 'POST':
            form = ContactForm(request.POST, request.FILES, instance=contact)
            if request.POST.get('is_ajaxForm') == '1':
                if form.is_valid():
                    form.save()
                    form = ContactForm(instance=contact)
                return render(request, 'contact.html', {'form':form, 'contact':contact})
            if form.is_valid():
                form.save()
                return redirect('index')
            return render(request, template_name, {'form':form, 'contact':contact})
    form = ContactForm(instance=contact)
    return render(request, template_name, {'form':form, 'contact':contact})

def logout(request):
    _logout(request)
    return redirect('index')