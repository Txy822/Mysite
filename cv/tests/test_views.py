from django.test import TestCase,Client
from django.urls import reverse,resolve
from cv.models import Cv_section
from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.template.loader import render_to_string


class TestViews(TestCase):
    def setUp(self):
        self.client=Client()
        self.cv_section_list_url=reverse('cv_section_list')
        self.cv_section_detail_url=reverse('cv_section_detail',args=[1])

        Cv_section.objects.create(
        title='title',
        text='my text'
        )

    def test_cv_section_list_GET(self):
        response=self.client.get(self.cv_section_list_url)
        self.assertEquals(response.status_code,200)
        self.assertTemplateUsed(response,'cv/cv_sections_list.html')
    def test_cv_section_detail_GET(self):
        response=self.client.get(self.cv_section_detail_url)
        self.assertEquals(response.status_code,200)
        self.assertTemplateUsed(response,'cv/cv_section_detail.html')

    def test_uses_correct_template(self):
        response = self.client.get('/cv/')
        self.assertTemplateUsed(response, 'cv/cv_sections_list.html')

    # def test_cv_page_returns_correct_html(self):
    #     response = self.client.get('/cv/')
    #     html = response.content.decode('utf8')
    #     self.assertTrue(html.strip().startswith('<html>'))
    #     self.assertIn('<title>Tesfahun Curriculum Vitae</title>', html)
    #     self.assertTrue(html.strip().endswith('</html>'))
    #     expected_html = render_to_string('cv/cv_sections_list.html')
    #     self.assertEqual(html, expected_html)
