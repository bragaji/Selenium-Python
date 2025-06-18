import time

from selenium import webdriver
from utils.base_test import logged_in_driver
from pages.layout2_page import Layout2Page



def test_fname_lname(logged_in_driver):
    driver = logged_in_driver
    layout2 = Layout2Page(driver)
    layout2.select_fname_lname("Prashant","Gautam")

def test_gender(logged_in_driver):
    driver = logged_in_driver
    layout2 = Layout2Page(driver)
    layout2.select_gender()

def test_options(logged_in_driver):
    driver = logged_in_driver
    layout2 = Layout2Page(driver)
    layout2.select_option("Option 1")

def test_date(logged_in_driver):
    driver = logged_in_driver
    layout2 = Layout2Page(driver)
    layout2.select_date("06-11-2024")
    time.sleep(10)

def test_upload(logged_in_driver):
    driver = logged_in_driver
    layout2 = Layout2Page(driver)
    layout2.upload_file(file_path=r'C:\Users\pspra\PycharmProjects\Selenium-Python\Input_data\Test_Plan_Template.docx')
    time.sleep(10)

