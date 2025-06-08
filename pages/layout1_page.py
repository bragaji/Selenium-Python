from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Layout1Page:
    def __init__(self,driver):
        self.driver=driver
        self.alert_button=(By.XPATH,'//button[text()=" Your Sample Alert Button!"]')
        self.alert_text=(By.ID,'demo')
        self.tool_tip=(By.XPATH,"//div[@class='tooltip']")
        self.tool_tip_text=(By.CLASS_NAME,'tooltiptext')

    def click_alert_button(self):
        WebDriverWait(self.driver,10).until(
            EC.element_to_be_clickable(self.alert_button)
        ).click()
        #self.driver.find_element(*self.alert_button).click()

    def accept_alert(self):
        alert = self.driver.switch_to.alert
        print("Alert text:", alert.text)
        alert.accept()

    def get_alert(self):
        element =self.driver.find_element(*self.alert_text)
        print(element.text)

    def get_tool_tip(self):
        tooltip_element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.tool_tip)
        )
        ActionChains(self.driver).move_to_element(tooltip_element).perform()

        tooltip_text = self.driver.find_element(*self.tool_tip_text).text
        print("Tooltip Text:", tooltip_text)
        self.tool_tip_text = tooltip_text

