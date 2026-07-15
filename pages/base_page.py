from utilities.waits import Waits
from selenium.webdriver.support import expected_conditions as EC
class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = Waits(driver)

    def click(self, locator):
        self.wait.wait_for_clickable(locator).click()

    def send_keys(self, locator, value):
        element = self.wait.wait_for_visibility(locator)
        element.clear()
        element.send_keys(value)

    def get_text(self, locator):
        return self.wait.wait_for_visibility(locator).text

    def is_displayed(self, locator):
       return self.wait.wait_for_visibility(locator).is_displayed()

    def get_element(self, locator):
        return self.wait.wait_for_visibility(locator)

    def get_elements(self, locator):
        return self.driver.find_elements(*locator)

    def is_element_present(self, locator):
        return len(self.driver.find_elements(*locator)) > 0