from django.test import TestCase
from apps.t1_base.models import Contact
from apps.t1_base.views import index as index_view
from apps.t5_form_edit.forms import ContactForm
from apps.t5_form_edit import views
from django.core.urlresolvers import reverse
import json
from datetime import date


class FormEditTest(TestCase):
    fixtures = ['initial_data.json']

    def test_edit_link(self):
        """Edit link should show only for registered user"""
        response = self.client.get(reverse(index_view))
        self.assertNotContains(response, '<a href="/edit/">Edit</a>')
        self.assertContains(response, '<a href="/accounts/login/">Login</a>')
        self.assertContains(response,
                            '<a href="/accounts/register/">Register</a>')

        self.client.login(username='admin', password='123')
        response = self.client.get(reverse(index_view))
        self.assertContains(response, '<a href="/edit/">Edit</a>')
        self.assertContains(response, '<a href="/accounts/logout/">Logout</a>')

    def test_get_edit_page(self):
        """Testing get response edit page"""
        self.client.login(username='admin', password='123')
        response = self.client.get(reverse(views.edit))
        self.assertEquals(response.status_code, 200)

    def test_form(self):
        """Testing form presented on edit page"""
        self.client.login(username='admin', password='123')
        response = self.client.get(reverse(views.edit))
        form = response.context['form']
        self.assertIsInstance(form, ContactForm)

    def test_form_post(self):
        """Testing form ajax post request without image"""
        self.client.login(username='admin', password='123')
        response = self.client.get(reverse(views.edit))
        form = response.context['form']
        data = form.initial
        data['name'] = 'New name'
        data['photo'] = None
        for obj in data.values():
            if isinstance(obj, date):
                return obj.isoformat()
        data = json.dumps(data)
        self.client.post(reverse(views.edit), data)
        response = self.client.get(reverse(views.edit))
        print response
        self.assertContains(response, 'New Name')

    def test_image_post(self):
        """Testing image upload with form"""
        self.client.login(username='admin', password='123')
        contact = Contact.objects.first()
        data = {
            'name': 'name',
            'last_name': 'last name',
            'date_of_birth': '1990-01-18',
            'bio': 'bio',
            'contacts': 'contacts',
            'email': 'email@test.test',
            'jabber': 'jabber@test.test',
            'skype': 'skype',
            'other_contacts': 'other_contacts',
        }
        form = ContactForm(data, instance=contact)
        self.assertTrue(form.is_valid())
        form.save()
        response = self.client.post(reverse(views.edit), data)
        self.assertEqual(response.status_code, 200)

    def test_invalid_data(self):
        """Testing requests with invalid data"""
        self.client.login(username='admin', password='123')
        response = self.client.get(reverse(views.edit))
        form = response.context['form']
        data = form.initial
        data['email'] = 'foo'
        data['photo'] = None
        for obj in data.values():
            if isinstance(obj, date):
                return obj.isoformat()
        data = json.dumps(data)
        self.client.post(reverse(views.edit), data)
        response = self.client.get(reverse(views.edit))
        self.assertContains(json.loads(response.content)
                            ['err_msg']['email'][0],
                            'Enter a valid email address.')
