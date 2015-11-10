from django.test import TestCase
from models import Contact
from . import views
from django.core.urlresolvers import reverse

# Create your tests here.


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
        self.assertContains(request, self.contact.contacts)
        self.assertContains(request, self.contact.last_name)
        self.assertContains(request, self.contact.other_contacts)
        self.assertContains(request, self.contact.skype)
