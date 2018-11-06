import unittest
from selenium import webdriver


class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome()

    def tearDown(self):
        self.browser.quit()

    def test_server_works(self):
        self.browser.get('http://localhost:8000')
        self.assertIn('Webex', self.browser.title)


if __name__ == "__main__":
    unittest.main()
