from selenium import webdriver

browser=webdriver.Firefox()
browser.get('http://localhost:8000/cv')

assert 'Tesfahun Curriculum Vitae' in browser.title
