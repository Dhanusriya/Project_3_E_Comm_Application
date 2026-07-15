from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class LoginPage(BasePage):
    username = (By.ID, "user-name")
    password = (By.ID, "password")
    login_button = (By.ID, "login-button")
    error_message = (By.XPATH, "//h3[@data-test='error']")

    def open_application(self):
        self.driver.get("https://www.saucedemo.com/")

    def login(self, username, password):
        self.send_keys(self.username, username)
        self.send_keys(self.password, password)
        self.click(self.login_button)

    def get_error_message(self):
        return self.get_text(self.error_message)

    def is_error_message_displayed(self):
        return self.is_displayed(self.error_message)

    def _is_login_page_displayed(self):
        return self.is_displayed(self.login_button)