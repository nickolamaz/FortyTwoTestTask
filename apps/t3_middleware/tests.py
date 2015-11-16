from django.test import TestCase
from models import HttpRequestStore
from apps.t1_base.views import index as index_view
from apps.t3_middleware import views
from django.core.urlresolvers import reverse
from django.core.serializers import serialize
import json
import re


class MiddlewareTest(TestCase):
    fixtures = ['initial_data.json']

    def test_get_request(self):
        """Check page is responsing"""
        response = self.client.get(reverse(views.requests_view))
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
        response = self.client.get(
            reverse(views.requests_view),
            HTTP_X_REQUESTED_WITH='XMLHttpRequest'
        )
        data = json.loads(response.content)
        requests = json.loads(serialize('json', requests))
        for elem in data:
            self.assertNotIn(elem, requests)

    def test_ajax_get(self):
        """Testing get ajax request. New requests should not be viewed"""
        for request in range(10):
            self.client.get(reverse(index_view))
        request_objects = HttpRequestStore.objects.all().order_by('-date')[:10]
        response = self.client.get(
            reverse(views.requests_view),
            HTTP_X_REQUESTED_WITH='XMLHttpRequest'
        )
        self.assertEqual(response.status_code, 200)

        for elem in request_objects:
            assert not elem.is_viewed
        data = json.loads(response.content)
        self.assertEqual(data['count'], 10)

    def test_ajax_post(self):
        """
        Testing post ajax request.
        After post request all data should be viewed
        """
        for request in range(10):
            self.client.get(reverse(index_view))
        request_objects = HttpRequestStore.objects.all().order_by('-date')[:10]
        response_post = self.client.post(
            reverse(views.requests_view),
            HTTP_X_REQUESTED_WITH='XMLHttpRequest'
        )
        response_get = self.client.get(
            reverse(views.requests_view),
            HTTP_X_REQUESTED_WITH='XMLHttpRequest'
        )
        self.assertEqual(response_post.status_code, 200)

        for elem in request_objects:
            assert elem.is_viewed
        data = json.loads(response_get.content)
        self.assertEqual(data['count'], 0)

    def test_count_requests(self):
        """Test displaying no more than 10 objects at the page"""
        for request in range(15):
            self.client.get(reverse(index_view))
        response_get = self.client.get(
            reverse(views.requests_view),
            HTTP_X_REQUESTED_WITH='XMLHttpRequest'
        )
        data = json.loads(response_get.content)
        self.assertLessEqual(data['content_count'], 10)

    def test_template_usage(self):
        """Testing template usage"""
        response = self.client.get(reverse(views.requests_view))
        self.assertTemplateUsed(response, 't3_middleware/requests.html')

    def check_requests_link(self):
        """Testing requests link is present on index page"""
        response = self.client.get(reverse(index_view))
        self.assertContains(response, '<a href="/requests/">requests</a>')


class TestPriority(TestCase):
    def test_priority_create(self):
        """Testing creation of default priority field"""
        self.client.get(reverse(index_view))
        request = HttpRequestStore.objects.last()
        self.assertEqual(request.priority, 1)

    def test_priority_ordering(self):
        """Testing ordering by priority field"""
        self.client.get(reverse(views.requests_view))
        request = HttpRequestStore.objects.last()
        request.priority = 50
        request.save()
        for i in range(10):
            self.client.get(reverse(index_view))
        self.assertEqual('/requests/', request.path)

        response_get = self.client.get(
            reverse(views.requests_view),
            HTTP_X_REQUESTED_WITH='XMLHttpRequest'
        )
        data = json.loads(response_get.content)
        resp = re.compile(r'priority">\n\s+(\d+)')
        result = re.findall(resp, data['content'])
        self.assertEqual(int(result[0]), request.priority)
