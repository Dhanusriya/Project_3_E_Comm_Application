from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class CheckoutPage(BasePage):
    checkout_button = (By.ID, "checkout")
    first_name = (By.ID, "first-name")
    last_name = (By.ID, "last-name")
    postal_code = (By.ID, "postal-code")
    continue_button = (By.ID, "continue")
    finish_button = (By.ID, "finish")
    complete_header = (By.CLASS_NAME, "complete-header")

    def click_checkout_button(self):
        self.click(self.checkout_button)

    def enter_checkout_details(self, first, last, zipcode):
        self.send_keys(self.first_name, first)
        self.send_keys(self.last_name, last)
        self.send_keys(self.postal_code, zipcode)

    def click_continue_button(self):
        self.click(self.continue_button)

    def click_finish_button(self):
        self.click(self.finish_button)

    def get_success_message(self):
        return self.get_text(self.complete_header)