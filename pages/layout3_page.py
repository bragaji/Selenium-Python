from selenium import webdriver
from selenium.webdriver.common.by import By

class Layout3Page:
    def __init__(self,driver):
        self.driver = driver
        self.table =(By.XPATH,"//legend[normalize-space()='This is your Sample Table:']/following::table[1]")

    def fetch_table_header(self):
        table=self.driver.find_element(*self.table)
        headers = [th.text.strip() for th in table.find_elements(By.TAG_NAME, "th")]
        return headers

    def fetch_table_data(self):
        headers=self.fetch_table_header()
        table=self.driver.find_element(*self.table)
        data = []
        for row in table.find_elements(By.XPATH, ".//tr[position() >1]"):  # skip header row
            cells = [td.text.strip() for td in row.find_elements(By.TAG_NAME, "td")]
            if cells:  # ignore empty separator rows, if any
                data.append(dict(zip(headers, cells)))

        return data

