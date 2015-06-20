from django.db import models
from django.forms import ModelForm
from datetime import datetime
# Create your models here.

class Contact(models.Model):
    name = models.CharField('Name', max_length=50)
    last_name = models.CharField('Last name', max_length=50)
    date_of_birth = models.DateField('Date of birth',db_index=True)
    bio = models.TextField('Bio', null=1, blank=1)
    contacts = models.CharField('Contacts', max_length=200)
    email = models.EmailField('Email')
    jabber = models.EmailField('Jabber ID')
    skype = models.CharField('Skype ID', max_length=50, null=1, blank=1)
    other_contacts = models.TextField('Other contacts', null=1, blank=1)
    photo = models.ImageField(upload_to='photo', null=1, blank=1)

class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'

class HttpRequestStore(models.Model):
    date = models.DateTimeField('Request date/time', default=datetime.now())
    method = models.CharField('Method', max_length=6)
    path = models.CharField(max_length=256)
    host = models.CharField(max_length=256)
    priority = models.IntegerField(default=0, db_index=True)
    def __unicode__(self):
        return u'%d %s %s %s' % (
                    self.priority,
                    self.date.strftime('%Y-%m-%d %H:%M:%S'),
                    self.method,
                    self.path
                )