import allure
import pytest
from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage
from test_data.users import STANDARD_USERNAME, STANDARD_PASSWORD
from utilities.logger import Logger

logger = Logger.get_logger()

#-----------------------------------------TC05- SELECT RANDOM PRODUCTS AND EXTRACT THEIR DATA --------------------------

@allure.feature("Cart")
@pytest.mark.cart
class TestRandomProducts():
    def test_random_product_selection(self, setup):
        driver = setup

        login = LoginPage(driver)
        inventory = InventoryPage(driver)

        logger.info("Stating to select random products and its data")

        login.open_application()
        login.login(STANDARD_USERNAME, STANDARD_PASSWORD)

        selected_products = inventory.get_random_products()

        logger.info("Randomly selected products")

        for product in selected_products:
            logger.info(
                f"Product Name: {product['name']} - Price: {product['price']}")
            print(product["name"], product["price"])

        assert len(selected_products) == 4

        logger.info("Verified the data for all the randomly selected products")