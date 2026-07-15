import allure
import pytest
from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage
from pages.menu_page import MenuPage
from test_data.users import STANDARD_USERNAME, STANDARD_PASSWORD
from utilities.logger import Logger

logger = Logger.get_logger()

#-------------------------------------TC10 - VALIDATE RESET APP STATE FUNCTIONALITY ------------------------------------

@allure.feature("Reset App State")
@pytest.mark.reset
class TestResetAppState:
    def test_reset_app_state(self, setup):
        driver = setup

        login = LoginPage(driver)
        inventory = InventoryPage(driver)
        menu = MenuPage(driver)

        logger.info("Starting to Validate Reset App State functionality")
        login.open_application()
        login.login(STANDARD_USERNAME, STANDARD_PASSWORD)

        inventory.get_random_products()

        assert inventory.get_cart_count() == "4"

        logger.info("4 products added successfully")

        menu.open_menu()
        menu.reset_app()

        logger.info("Reset App State clicked")

        assert not inventory.is_cart_badge_displayed()

        logger.info("Cart Badge Removed successfully")