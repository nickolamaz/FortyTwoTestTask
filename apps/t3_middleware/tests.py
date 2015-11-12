from django.test import TestCase
from models import HttpRequestStore
from apps.t1_base.views import index as index_view
from apps.t3_middleware import views
from django.core.urlresolvers import reverse
from django.core.serializers import serialize
import json


class MiddlewareTest(TestCase):
    fixtures = ['initial_data.json']

    def test_get_request(self):
        """Check page is responsing"""
        response = self.client.get(reverse(views.request))
        self.assertEqual(response.status_code, 200)

    def test_requests_saved(self):
        """Check number of requests in DB"""
        requests = HttpRequestStore.objects.all()
        self.assertEqual(requests.count(), 0)
        for request in range(10):
            self.client.get(reverse(index_view))
        requests = HttpRequestStore.objects.all()
        self.assertEqual(len(requests), 10)

    def test_json_request(self):
        """Check json request are not saving to DB"""
        requests = HttpRequestStore.objects.all()[:10]
        self.assertEqual(requests.count(), 0)
        response = self.client.get(reverse(views.requests_get))
        data = json.loads(response.content)
        requests = json.loads(serialize('json', requests))
        for elem in data:
            self.assertNotIn(elem, requests)

