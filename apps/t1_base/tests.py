# -*- coding: utf-8 -*-
from django.test import TestCase
from models import Contact
from . import views
from django.core.urlresolvers import reverse


class ModelTest(TestCase):
    fixtures = ['initial_data.json']
    contact = Contact.objects.first()

    def test_get_request(self):
        """Testing get request for index page"""
        request = self.client.get(reverse(views.index))
        self.assertEqual(request.status_code, 200)

    def test_get_client_info(self):
        """Testing all fields in response"""
        request = self.client.get(reverse(views.index))
        self.assertContains(request, self.contact.bio)
        self.assertContains(request, self.contact.name)
        self.assertContains(request, self.contact.last_name)
        self.assertContains(request, self.contact.other_contacts)
        self.assertContains(request, self.contact.skype)

    def test_unicode(self):
        """Testing unicode in response"""
        self.contact.name = 'Имя'
        self.contact.last_name = 'Фамилия'
        self.contact.save()
        unicode_name = u'Имя'
        unicode_last_name = u'Фамилия'
        request = self.client.get(reverse(views.index))
        self.assertContains(request, 'utf-8')
        self.assertContains(request, unicode_name)
        self.assertContains(request, unicode_last_name)

    def test_empty_db(self):
        """Testing empty database"""
        Contact.objects.all().delete()
        request = self.client.get(reverse(views.index))
        self.assertEqual(request.context['contact'], None)

    def test_many_db_rows(self):
        """Testing more than one row in database"""
        Contact.objects.create(name='First Name',
                               last_name='Last Name',
                               date_of_birth='1890-10-23')
        request = self.client.get(reverse(views.index))
        self.assertEqual(request.context['contact'], Contact.objects.first())
