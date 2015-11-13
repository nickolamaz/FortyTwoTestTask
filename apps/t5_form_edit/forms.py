from django import forms
from apps.t1_base.models import Contact
from widgets import PreviewImage


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'
        widgets = {
            'photo': PreviewImage(),
            'bio': forms.Textarea(attrs={'rows': 5}),
            'other_contacts': forms.Textarea(attrs={'rows': 5})
        }
