from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

class Layout2Page:
    def __init__(self, driver):
        self.driver = driver
        self.first_name_textbox= (By.ID,"fname")
        self.last_name_textbox= (By.XPATH,"//input[@name='lname']")
        self.gender_radiobutton =(By.XPATH,"//label[@for='male']")
        self.option_dropdown =(By.ID,"option")
        self.date=(By.ID,"day")
        self.select_file_button=(By.ID,"myfile")


    def select_fname_lname(self,fname,lname):
        self.driver.find_element(*self.first_name_textbox).send_keys(fname)
        self.driver.find_element(*self.last_name_textbox).send_keys(lname)

    def select_gender(self):
        self.driver.find_element(*self.gender_radiobutton).click()

    def select_option(self,visible_text):
        select = Select(self.driver.find_element(*self.option_dropdown))
        select.select_by_visible_text(visible_text)

    def select_date(self,date_string):
        self.driver.find_element(*self.date).send_keys(date_string)

    def upload_file(self,file_path):
        self.driver.find_element(*self.select_file_button).send_keys(file_path)



