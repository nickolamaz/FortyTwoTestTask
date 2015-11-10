from django.forms import ModelForm
from apps.t1_base.models import Contact


class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'
