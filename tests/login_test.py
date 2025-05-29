import time
import pytest
from selenium import webdriver
from pages.login_page import LoginPage
from utils.base_test import logged_in_driver


def test_login(logged_in_driver):
    driver= logged_in_driver
    login_page =LoginPage(driver)
    login_page.open_page("https://trytestingthis.netlify.app/")
    time.sleep(1)
    login_page.login("test", "test")
    time.sleep(1)


