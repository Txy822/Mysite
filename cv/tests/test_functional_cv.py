from django.test import LiveServerTestCase,Client
from selenium import webdriver
import unittest

class FunctionalTestCase(LiveServerTestCase):

    #set up  is going to run before each method
    def setUp(self):
        self.browser = webdriver.Firefox()

   # Recruiter  is looking employees and need to see cv.
   #He opens the blog post section and found cv page icon
   # test there is cv page icon to be clicked on my blog
    def test_there_is_cv_page(self):

       self.browser.get(self.live_server_url)
       self.assertIn('Curriculum Vitae(CV)',self.browser.page_source)
    #He opened the cv and can see different sections of cv
    #test the existence of  cv page  status code
    def test_cv_page(self):
        response = self.client.get('/cv')
        self.assertEqual(response.status_code, 301)

    # He notices the cv page title and header mention Tesfahun Curriculum Vitae
    # test  there is cv page title
    def test_title_cv_page(self):
        self.browser.get('%s%s' % (self.live_server_url, '/cv/'))
        self.assertIn('Tesfahun Curriculum Vitae',self.browser.title)

    # When he clicked each section of cv he can see the cv section in detail
    # He clicked the Curriculum Vitae icon and he goes back.
    # When he hit personal blog he can see the blog posts as well.
    # He gets  more works about the employee
    # He get back to other office works
    #tear down  is going to run after  each method
    def tearDown(self):
        self.browser.quit()

if __name__ == '__main__':
    unittest.main(warnings='ignore')
