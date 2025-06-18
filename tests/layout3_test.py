from selenium import webdriver
from utils.base_test import logged_in_driver
from pages.layout3_page import Layout3Page

def test_table_header(logged_in_driver):
    driver = logged_in_driver
    layout3 = Layout3Page(driver)
    layout3.fetch_table_header()

def test_table_data(logged_in_driver):
    driver = logged_in_driver
    layout3 = Layout3Page(driver)
    layout3.fetch_table_data()
    data = layout3.fetch_table_data()
    for row in data:
        print(row['Firstname'])