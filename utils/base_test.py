import pytest
from selenium import webdriver
from pages.login_page import LoginPage
from utils.config import URL, USERNAME, PASSWORD
from utils.logger_config import get_logger


logger = get_logger("LoginPage")
@pytest.fixture()
def logged_in_driver():
    logger.info("Setup: Driver setup started")
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(10)

    logger.info("Login started...")
    login_page = LoginPage(driver)
    login_page.open_page(URL)
    login_page.login(USERNAME, PASSWORD)
    logger.info("Login Successful...")

    yield driver
    driver.quit()


