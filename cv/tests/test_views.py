from django.test import TestCase,Client
from django.urls import reverse
from cv.views import cv_section_list

class TestViews(TestCase):

    def test_root_url_resolves_to_cv_page_view(self):
        found = resolve('/cv')
        self.assertEqual(found.func, cv_section_list)
