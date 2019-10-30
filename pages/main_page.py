from selenium import webdriver
import time

browser = webdriver.Chrome(executable_path='C:/Users/ХХХ/Desktop/Учеба/Сафаров/Python/chromedriver.exe')
link = "http://selenium1py.pythonanywhere.com/"
def should_be_login_link(self):
    self.browser.find_element(By.CSS_SELECTOR, "#login_link_invalid")

def test_guest_should_see_login_link(browser):


    page = MainPage(browser, link)
    page.open()
    page.should_be_login_link()