from django.test import TestCase,Client
from django.urls import reverse,resolve
from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse, Http404
from cv.views import cv_section_list
from django.template.loader import render_to_string




class TestViews(TestCase):

    def test_url_resolves_to_cv_page_view(self):
        found = resolve('/cv/')
        self.assertEqual(found.func, cv_section_list)

    # def test_cv_page_returns_correct_html(self):
    #     request = HttpRequest()
    #     response = cv_section_list(request)
    #     html = response.content.decode('utf8')
    #     self.assertTrue(html.strip().startswith('<html>'))
    #     self.assertIn('<title>Tesfahun Curriculum Vitae</title>', html)
    #     #self.assertTrue(html.endswith('</html>'))
    #     self.assertTrue(html.strip().endswith('</html>'))
    # def test_home_returns_correct_html(self):
    #     request = HttpRequest()
    #     response = cv_section_list(request)
    #     html = response.content.decode('utf8')
    #     expected_html = render_to_string('cv_sections_list.html')
    #     self.assertEqual(html, expected_html)
    #     self.assertTrue(html.strip().startswith('<html>'))
    #     self.assertTrue(html.strip().endswith('</html>'))
    def test_me_page_returns_correct_html(self):
        response = self.client.get('/cv/')

        html = response.content.decode('utf8')
        #self.assertTrue(html.strip().startswith('<html>'))
        self.assertIn('<title>Tesfahun Curriculum Vitae</title>', html)
        self.assertTrue(html.strip().endswith('</html>'))
        expected_html = render_to_string('cv/cv_sections_list.html')
        self.assertEqual(html, expected_html)
        self.assertTemplateUsed(response, 'cv/cv_sections_list.html')
