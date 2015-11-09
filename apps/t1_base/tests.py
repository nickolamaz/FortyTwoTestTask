from django.test import TestCase
from models import Contact
from fortytwo_test_task import views
from django.core.urlresolvers import reverse

# Create your tests here.


class ModelTest(TestCase):
    def setUp(self):
        """Create new person"""
        self._contact = {
            "name": "Nikolay",
            "last_name": "Mazurenko",
            "date_of_birth": "2015-09-08",
            "bio": "Here must be my bio",
            "contacts": "my_contacts",
            "email": "nickola_90@list.ru",
            "jabber": "nickolamaz",
            "skype": "nickolamaz",
            "other_contacts": "Mazurenko"
        }

        self.contact = Contact.objects.create(**self._contact)

    def test_fields(self):
        """Testing created fields"""
        for k in self._contact.keys():
            self.assertEquals(self._contact[k], getattr(self.contact, k))

    def test_get_request(self):
        """Testing get request for index page"""
        request = self.client.get(reverse(views.index))
        self.assertEqual(request.status_code, 200)

    def test_get_client_info(self):
        """Testing all fields in response"""
        request = self.client.get(reverse(views.index))
        print request
        self.assertContains(request, self.contact.bio)
        self.assertContains(request, self.contact.name)
        self.assertContains(request, self.contact.contacts)
        self.assertContains(request, self.contact.last_name)
        self.assertContains(request, self.contact.other_contacts)
        self.assertContains(request, self.contact.skype)

