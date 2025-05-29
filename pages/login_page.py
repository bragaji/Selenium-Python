from selenium.webdriver.common.by import By


class LoginPage:
    def __init__(self,driver):
        self.driver = driver
        self.username_textbox= (By.XPATH,'//input[@name="uname"]')
        self.password_textbox= (By.ID,'pwd')
        self.login_button=(By.XPATH,'//input[@value="Login"]')
        self.go_to_home=(By.XPATH,"/html/body/div[3]/h4/a")


    def open_page(self,url):
        self.driver.get(url)


    def login(self, username, password):
        self.driver.find_element(*self.username_textbox).send_keys(username)
        self.driver.find_element(*self.password_textbox).send_keys(password)
        self.driver.find_element(*self.login_button).click()
        self.driver.find_element(*self.go_to_home).click()
