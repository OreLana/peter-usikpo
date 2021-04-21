from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status


ALL_NEWSLETTER = reverse('pugapi:all_newsletter')



class TestAllNewsletter(TestCase):

    def test_all_newsletter(self):
        res = self.client.get(ALL_NEWSLETTER) 
        self.assertEqual(len(res.json()), 0)
        