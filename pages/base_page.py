from selenium import webdriver
import time

browser = webdriver.Chrome(executable_path='C:/Users/ХХХ/Desktop/Ycheba/Safarov/Python/chromedriver.exe')
url = "http://selenium1py.pythonanywhere.com/"

class BasePage():
    def __init__(self, browser, url):
        self.browser = browser
        self.url = url

    def open(self):
        self.get(browser, url)
        url.get(url)
