from django.test import TestCase,Client
from django.urls import reverse,resolve
from django.http import HttpResponse
from cv.views import cv_section_list

class TestViews(TestCase):

    def test_url_resolves_to_cv_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func, cv_section_list)

    def test_cv_page_returns_correct_html(self):
        request = HttpRequest()
        response = cv_section_list(request)
        html = response.content.decode('utf8')
        self.assertTrue(html.startswith('<html>'))
        self.assertIn('<title>To-Do lists</title>', html)
        self.assertTrue(html.endswith('</html>'))
