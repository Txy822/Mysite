from django.test import TestCase,Client
from selenium import webdriver

browser=webdriver.Firefox()
browser.get('http://localhost:8000')

assert 'Tesfahun Curriculum Vitae' in browser.title

browser.quit()
