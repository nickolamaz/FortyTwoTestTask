from django.test import TestCase
from models import Contact

# Create your tests here.
class ModelTest(TestCase):
    def setUp(self):
        self._contact = {
            "bio": "Lorem ipsum dolor sit amet, consectetuer adipiscing elit. \
            \r\nAenean commodo ligula eget dolor. Aenean massa. \
            \r\nCum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus.",
            "name": "Nikolay",
            "contacts": "Nikolaev",
            "last_name": "Mazurenko",
            "date_of_birth": "1990-01-18",
            "other_contacts": "https://github.com/nickolamaz/",
            "skype": "nickola2007",
            "jabber": "nickolamaz@jabber.ru",
            "email": "nickola_90@list.ru",
            "photo": None,
        }

        self.contact = Contact.objects.create(**self._contact)

    def test_fields(self):
        for k in self._contact.keys():
            self.assertEquals(self._contact[k], getattr(self.contact, k))