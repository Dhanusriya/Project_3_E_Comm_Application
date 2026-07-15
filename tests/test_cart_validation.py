import allure
import pytest

from pages.cart_page import CartPage
from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage
from test_data.users import STANDARD_USERNAME, STANDARD_PASSWORD
from utilities.logger import Logger

logger = Logger.get_logger()
#--------------------------------- TC07 - VALIDATE PRODUCT DETAILS INSIDE CART -----------------------------------------

@allure.feature("Cart")
@pytest.mark.cart
class TestAddToCartValidation:
    def test_validate_cart_products(self, setup):
        driver = setup

        login = LoginPage(driver)
        inventory = InventoryPage(driver)
        cart = CartPage(driver)

        logger.info("Starting to validate products in cart")

        login.open_application()

        login.login(STANDARD_USERNAME, STANDARD_PASSWORD)

        selected_products = inventory.get_random_products()

        cart.open_cart()
        cart_products = cart.get_cart_products()

        logger.info("Selected products")
        logger.info(selected_products)

        logger.info("Cart products")
        logger.info(cart_products)

        assert len(cart_products) == 4

        assert sorted(selected_products, key=lambda x:x["name"]) == sorted(cart_products, key=lambda x:x["name"])

        logger.info("Cart validation successful")