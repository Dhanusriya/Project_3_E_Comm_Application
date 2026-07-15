import allure
import pytest
from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage
from utilities.excel_reader import ExcelReader
from utilities.logger import Logger

#------------------------------------- TC01 - LOGIN WITH PREDEFINED USERS ----------------------------------------------

login_data = ExcelReader.get_login_data("test_data/login_data.xlsx", "Sheet1")
logger = Logger.get_logger()

@allure.epic("SauceDemo Automation")
@allure.feature("Login")
@pytest.mark.login
@pytest.mark.parametrize("username,password,expected", login_data)
class TestLogin:
    @allure.story("Valid Login")
    def test_login(self, setup, username, password, expected):
        driver = setup
        login = LoginPage(driver)

        inventory = InventoryPage(driver)

        logger.info(f"Testing user : {username}")

        login.open_application()
        login.login(username, password)

        if expected == "pass":
            assert (inventory.inventory_displayed() == "Products")

            logger.info(f"{username} Login successful")
        else:
            error = login.get_error_message()
            assert "Epic sadface" in  error
            logger.info(f"{username} Login failed as expected")
