import pytest
from selenium import webdriver
from pages.login_page import LoginPage
from utils.config import URL, USERNAME, PASSWORD

@pytest.fixture(scope="function")
def logged_in_driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(10)

    login_page = LoginPage(driver)
    login_page.open_page(URL)
    login_page.login(USERNAME, PASSWORD)

    yield driver
    driver.quit()
