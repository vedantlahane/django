from django.test import TestCase

# Create your tests here.
from django.urls import reverse

class GreetingTests(TestCase):
    def test_dynamic_greeting_page_status_code(self):
        response = self.client.get(reverse('greet',args=['TestUser']))
        self.assertEqual(response.status_code,200)