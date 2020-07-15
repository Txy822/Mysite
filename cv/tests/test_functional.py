from django.test import TestCase,Client
from selenium import webdriver
import unittest

class FunctionalTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        print("setUpTestData: Run once to set up non-modified data for all class methods.")
        pass

    def setUp(self):
        self.browser = webdriver.Firefox()

    def test_cv_page(self):
        response = self.client.get('/cv')
        self.assertEqual(response.status_code, 301)

    def test_title_cv_page(self):
        self.browser.get('http://localhost:8000/cv')
        self.assertIn('Tesfahun Curriculum Vitae',self.browser.title)

    def test_there_is_cv_page_name(self):
        self.browser.get('http://localhost:8000/cv')
        self.assertIn('Curriculum Vitae(CV)',self.browser.page_source)

    def tearDown(self):
        self.browser.quit()

if __name__ == '__main__':
    unittest.main(warnings='ignore')
