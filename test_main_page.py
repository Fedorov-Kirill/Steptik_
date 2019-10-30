# -*- coding: utf-8 -*-
from selenium import webdriver
from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.basket_page import BasketPage
from pages.product_page import ProductPage
import pytest
import time

@pytest.mark.login_guest
class TestLoginFromMainPage(object):
    
    def test_guest_can_go_to_login_link(self, browser):     
        link = "http://selenium1py.pythonanywhere.com/"
        page = MainPage(browser, link)
        page.open()
        page.go_to_login_page()
        login_page = LoginPage(browser, browser.current_url)
        login_page.should_be_login_page()

    def test_guest_should_see_login_link(self, browser):
        link = "http://selenium1py.pythonanywhere.com/"
        page = MainPage(browser, link)
        page.open()
        page.should_be_login_link()
         
# def test_guest_can_go_to_login_page(browser):
    # link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209?promo=midsummer"
    # page = MainPage(browser, link)
    # page.open()
    # page.go_to_login_page()
    # login_page = LoginPage(browser, browser.current_url)
    # login_page.should_be_login_page()

# def test_guest_should_see_login_link(browser):
    # link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209?promo=midsummer"
    # page = MainPage(browser, link)
    # page.open()
    # page.should_be_login_link()

def test_guest_cant_see_product_in_cart_opened_from_main_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)
    page.open()
    page.go_to_basket_top()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_be_busket()
    basket_page.should_not_be_items_in_basket()
    basket_page.should_be_basket_is_empty_message()
    
    
# def test_login_page_is_ok(browser, timeout):
    # link = "http://selenium1py.pythonanywhere.com/accounts/login/"
    # page = LoginPage(browser, timeout, link)
    # page.open()
    # page.should_be_login_page()    
    
# link = "http://selenium1py.pythonanywhere.com/"

# def test_guest_can_go_to_login_page(browser):
    # link = "http://selenium1py.pythonanywhere.com/"
    # browser.get(link)
    # login_link = browser.find_element_by_css_selector("#login_link")
    # login_link.click()
    
# def go_to_login_page(browser):
    # link = browser.find_element_by_css_selector("#login_link")
    # link.click()

# def test_guest_can_go_to_login_page(browser): 
   # browser.get(link) 
   # go_to_login_page(browser)    