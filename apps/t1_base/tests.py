# -*- coding: utf-8 -*-
from django.test import TestCase


class ModelTest(TestCase):
    """Simple test"""
    def test(self):
        self.assertEqual(2 + 2, 4)
