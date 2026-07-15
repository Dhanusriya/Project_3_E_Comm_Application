import allure
import pytest
from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage
from test_data.users import STANDARD_USERNAME, STANDARD_PASSWORD
from utilities.logger import Logger

logger = Logger.get_logger()
#-----------------------------------------TC06 - ADD SELECTED PRODUCTS TO CART AND VALIDATE ----------------------------

@allure.feature("Cart")
@pytest.mark.cart
class TestAddToCart:
    def test_add_random_products_to_cart(self, setup):
        driver = setup

        login = LoginPage(driver)
        inventory = InventoryPage(driver)

        logger.info("Starting to add random products to cart")

        login.open_application()
        login.login(STANDARD_USERNAME, STANDARD_PASSWORD)

        selected_products = inventory.get_random_products()

        logger.info("Selected Products:")

        for product in selected_products:
            logger.info(f"{product['name']} - {product['price']}")

        assert inventory.get_cart_count() == "4"

        logger.info("Cart Badge Count verified successfully")