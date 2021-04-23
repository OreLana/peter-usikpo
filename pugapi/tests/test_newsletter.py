from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status


ALL_NEWSLETTER = reverse('pugapi:all_newsletter')
DETAIL_NEWSLETTER = reverse('pugapi:detail_newsletter')



class TestNewsletter(TestCase):

    def test_all_newsletter(self):
        res = self.client.get(ALL_NEWSLETTER) 
        self.assertEqual(len(res.json()), 0)

    def test_detail_newsletter(self):
        res = self.client.get(DETAIL_NEWSLETTER, 1)
        self.assertEqual(len(res.json()), 1)

        