from django.db import models
from PIL import Image


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

    photo_height = models.PositiveIntegerField(null=True, blank=True,
                                               editable=False, default=200)
    photo_width = models.PositiveIntegerField(null=True, blank=True,
                                              editable=False, default=200)
    photo = models.ImageField('Profile Photo',
                              upload_to='photo', null=True, blank=True,
                              height_field='photo_height',
                              width_field='photo_width')

    def save(self, force_insert=False, force_update=False, using=None,  # NOQA
             update_fields=None, *args, **kwargs):
        if not self.photo:
            super(Contact, self).save(*args, **kwargs)
        else:
            super(Contact, self).save(*args, **kwargs)
            photo = Image.open(self.photo.path)
            (width, height) = photo.size
            size = (200, 200)
            photo = photo.resize(size, Image.ANTIALIAS)
            photo.save(self.photo.path)
