import allure
import pytest
from pages.login_page import LoginPage
from pages.menu_page import MenuPage
from utilities.logger import Logger
from test_data.users import STANDARD_PASSWORD, STANDARD_USERNAME
logger = Logger.get_logger()

#----------------------------------TC03 - VALIDATE LOGOUT FUNCTIONALITY ------------------------------------------------

@allure.feature("Login")
@pytest.mark.login
class TestLogout:
    def test_logout(self, setup):
        driver = setup
        login = LoginPage(driver)
        menu = MenuPage(driver)

        logger.info("Starting Logout Test")

        login.open_application()

        login.login(STANDARD_USERNAME, STANDARD_PASSWORD)

        logger.info("Login successful")

        menu.open_menu()

        logger.info("Menu opened")

        menu.logout()

        logger.info("Logout Clicked")

        assert login._is_login_page_displayed()

        logger.info("Logout verified successfully")