import unittest
from django.test import TestCase
from selenium import webdriver
import requests


class BasicTestCase(TestCase):

    def test_server_works(self):
        response = requests.get('http://localhost:8000')
        self.assertEqual(response.status_code, 200)


class NewVisitorTest(TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome()

    def tearDown(self):
        self.browser.quit()

    def test_server_works(self):
        self.browser.get('http://localhost:8000')
        self.assertIn('Webex', self.browser.title)


if __name__ == "__main__":
    unittest.main()
