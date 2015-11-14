from django.test import TestCase
from apps.t1_base.models import Contact
from apps.t1_base.views import index as index_view
from apps.t8_template_tags.templatetags.links_admin import admin_edit
from apps.t8_template_tags.models import ModelSignal
from django.core.urlresolvers import reverse
from django.core import management
from django.db.models import get_models
import StringIO


class TemplateTagsTest(TestCase):
    fixtures = ['initial_data.json']

    def test_admin_link_valid(self):
        """"
        Testing link to edit contact at admin.
        There is contact instance presents in database
        """
        response = self.client.get(reverse(index_view))
        self.assertContains(response,
                            '<a href="/admin/t1_base/contact/1/">(Admin)</a>')
        contact = Contact.objects.first()
        admin_link = admin_edit(contact)
        self.assertEqual(admin_link, '/admin/t1_base/contact/1/')
        response = self.client.get(admin_link)
        self.assertContains(response, 'Log in')
        self.client.login(username='admin', password='123')
        response = self.client.get(admin_link)
        self.assertContains(response, 't1_base-contact change-form')

    def test_admin_link_invalid(self):
        """"
        Testing link to edit contact at admin.
        There is no contact instance presents in database
        """
        Contact.objects.all().delete()
        self.client.login(username='admin', password='123')
        response = self.client.get(reverse(index_view))
        self.assertNotContains(response, '/admin/t1_base/contact/1/')


class TestCommands(TestCase):
    fixtures = ['initial_data.json']

    def test_models_count(self):
        """Testing printing models with count of objects in them"""
        out = StringIO.StringIO()
        management.call_command('models_list', stdout=out)

        models = get_models()
        for model in models:
            self.assertIn(
                '%s - objects: %d' % (model.__name__, model.objects.count()),
                out.getvalue())


class TestSignals(TestCase):
    fixtures = ['initial_data.json']

    def test_create_signal(self):
        """Testing signal saving create statement to DB"""
        init_count = ModelSignal.objects.count()
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
        Contact.objects.create(**data)
        signals = ModelSignal.objects.count()
        signal = ModelSignal.objects.last()
        self.assertGreater(signals, init_count)
        self.assertEqual(Contact.__name__, signal.model)
        self.assertEqual(signal.action, 'create')

    def test_edit_signal(self):
        """Testing signal editing statement to DB"""
        contact = Contact.objects.first()
        contact.name = 'Name'
        contact.save()
        signal = ModelSignal.objects.last()
        self.assertEqual(Contact.__name__, signal.model)
        self.assertEqual(signal.action, 'edit')

    def test_delete_signal(self):
        """Testing signal deleting statement to DB"""
        Contact.objects.first().delete()
        signal = ModelSignal.objects.last()
        self.assertEqual(Contact.__name__, signal.model)
        self.assertEqual(signal.action, 'delete')
