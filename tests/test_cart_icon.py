import allure
import pytest
from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage
from test_data.users import STANDARD_USERNAME, STANDARD_PASSWORD
from utilities.logger import Logger

logger = Logger.get_logger()

#---------------------------------------TC04 - CART ICON VISIBILITY ----------------------------------------------------

@allure.feature("Cart")
@pytest.mark.cart
class TestCartIcon:
    def test_cart_icon_visibility(self, setup):
        driver = setup
        login = LoginPage(driver)
        inventory_page = InventoryPage(driver)

        logger.info("Starting cart icon visibility test")

        login.open_application()

        login.login(STANDARD_USERNAME, STANDARD_PASSWORD)

        logger.info("Login successful")

        assert inventory_page.is_cart_icon_displayed()

        logger.info("CartIcon is visible")