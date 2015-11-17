from django.forms import ModelForm
from django.forms.models import modelformset_factory
from models import HttpRequestStore


class PriorityForm(ModelForm):
    class Meta:
        model = HttpRequestStore
        fields = ('priority',)


RequestsFormset = modelformset_factory(
    HttpRequestStore,
    form=PriorityForm,
    fields=('priority',),
    extra=0
)
