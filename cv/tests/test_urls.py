from django.test i e
from django.urls import reverse,resolve
from cv.views import cv_section_list,cv_section_detail
from cv.models import Cv_section



class TestUrls(TestCase):

    def test_cv_section_list_url_is_resolved(self):
        url=reverse('cv_section_list')
        self.assertEqual(resolve(url).func,cv_section_list)

    def test_cv_section_detail_url_resolveded(self):
        url=reverse('cv_section_detail',args=[1])
        self.assertEqual(resolve(url).func,cv_section_detail)
        
    def test_cv_section_new_url_resolveded(self):
        url=reverse('cv_section_new')
        self.assertEqual(resolve(url).func,cv_section_new)
