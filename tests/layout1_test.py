import time
import pytest
from selenium import webdriver
from pages.layout1_page import Layout1Page
from utils.base_test import logged_in_driver


def test_alert_button(logged_in_driver):
    driver=logged_in_driver
    layout1 = Layout1Page(driver)
    layout1.click_alert_button()
    time.sleep(1)
    layout1.accept_alert()
    time.sleep(1)
    layout1.get_alert()
    time.sleep(1)

def test_tool_tip(logged_in_driver):
    driver = logged_in_driver
    layout1 = Layout1Page(driver)
    layout1.get_tool_tip()
    assert layout1.tool_tip_text=="This is your sample Tooltip text"
