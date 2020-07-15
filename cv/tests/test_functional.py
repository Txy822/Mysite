from django.test import TestCase,Client
from selenium import webdriver
import unittest

class FunctionalTestCase(TestCase):
    #set up data for class based elements
    @classmethod
    def setUpTestData(cls):
        print("setUpTestData: Run once to set up non-modified data for all class methods.")
        pass

    #set up  is going to run before each method
    def setUp(self):
        self.browser = webdriver.Firefox()
        
    #testthe existence of  cv page  status code
    def test_cv_page(self):
        response = self.client.get('/cv')
        self.assertEqual(response.status_code, 301)

    # test  there is cv page title
    def test_title_cv_page(self):
        self.browser.get('http://localhost:8000/cv')
        self.assertIn('Tesfahun Curriculum Vitae',self.browser.title)

    # test there is cv page
    def test_there_is_cv_page(self):
        self.browser.get('http://localhost:8000/cv')
        self.assertIn('Curriculum Vitae(CV)',self.browser.page_source)

    #tear down  is going to run after  each method
    def tearDown(self):
        self.browser.quit()

if __name__ == '__main__':
    unittest.main(warnings='ignore')
