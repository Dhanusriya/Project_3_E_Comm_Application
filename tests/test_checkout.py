import allure
import pytest
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage
from test_data.checkout_data import FIRST_NAME, LAST_NAME, POSTAL_CODE
from test_data.users import STANDARD_USERNAME, STANDARD_PASSWORD
from utilities.logger import Logger
from utilities.screenshot import Screenshot

logger = Logger.get_logger()
#--------------------------------------- TC08 - COMPLETE CHECKOUT AND VALIDATE ORDER -----------------------------------

@allure.feature("Checkout")
@pytest.mark.checkout
class TestCheckout:
    def test_checkout(self, setup):
        driver = setup

        login = LoginPage(driver)
        inventory = InventoryPage(driver)
        cart = CartPage(driver)
        checkout = CheckoutPage(driver)

        logger.info("Starting test for checkout functionality")

        login.open_application()
        login.login(STANDARD_USERNAME, STANDARD_PASSWORD)

        inventory.get_random_products()
        cart.open_cart()
        checkout.click_checkout_button()
        checkout.enter_checkout_details(FIRST_NAME, LAST_NAME, POSTAL_CODE)
        checkout.click_continue_button()

        Screenshot.capture(driver, "Checkout_Overview")

        checkout.click_finish_button()

        assert (checkout.get_success_message() == "Thank you for your order!")

        logger.info("Checkout completed successfully")