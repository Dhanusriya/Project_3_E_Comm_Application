from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class MenuPage(BasePage):
    menu_button = (By.ID, 'react-burger-menu-btn')
    logout_button = (By.ID, 'logout_sidebar_link')
    reset_app_state = (By.ID, "reset_sidebar_link")

    def open_menu(self):
        self.click(self.menu_button)
        # Wait until Reset App State is visible
        self.wait.wait_for_visibility(self.reset_app_state)

    def logout(self):
        self.wait.wait_for_visibility(self.logout_button)
        self.click(self.logout_button)

    def reset_app(self):
        reset = self.wait.wait_for_clickable(self.reset_app_state)
        self.driver.execute_script("arguments[0].click();", reset)