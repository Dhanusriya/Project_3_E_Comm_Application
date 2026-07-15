import allure
import pytest
from pages.login_page import LoginPage
from utilities.logger import Logger

logger = Logger.get_logger()
#-------------------------------------TC02 - INVALID LOGIN CREDENTIALS -------------------------------------------------

@allure.feature("Login")
@pytest.mark.login
class TestInvalidLogin:
    def test_invalid_login_error_message(self, setup):
        driver = setup
        login = LoginPage(driver)

        logger.info("Starting Invalid Login Test")

        login.open_application()

        login.login("invalid_username", "invalid_password")

        assert login.is_error_message_displayed()

        expected_message = ("Epic sadface: Username and password"
                            " do not match any user in this service")

        assert login.get_error_message() == expected_message

        logger.info("Invalid Login Error Message Verified Successfully")

