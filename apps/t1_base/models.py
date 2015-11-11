from django.db import models


class Contact(models.Model):
    name = models.CharField('Name', max_length=50)
    last_name = models.CharField('Last name', max_length=50)
    date_of_birth = models.DateField('Date of birth')
    bio = models.TextField('Bio')
    contacts = models.CharField('Contacts', max_length=200)
    email = models.EmailField('Email')
    jabber = models.EmailField('Jabber ID')
    skype = models.CharField('Skype ID', max_length=50)
    other_contacts = models.TextField('Other contacts')

    # photo_height = models.PositiveIntegerField(null=True,
    # blank=True, editable=False, default=200)
    # photo = models.ImageField(upload_to='photo')
