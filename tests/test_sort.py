import allure
import pytest
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from test_data.users import (STANDARD_USERNAME,STANDARD_PASSWORD)
from utilities.logger import Logger

logger = Logger.get_logger()

#-------------------------------------------TC09 - VALIDATE SORTING FUNCTIONALITY ON PRODUCTS PAGE ---------------------

@allure.feature("Sort")
@pytest.mark.sort
@pytest.mark.parametrize(
    "sort_option, sort_type, reverse",
    [
        ("Name (A to Z)", "name", False),
        ("Name (Z to A)", "name", True),
        ("Price (low to high)", "price", False),
        ("Price (high to low)", "price", True),
    ]
)
class TestSorting:
    def test_sort_products(self, setup, sort_option, sort_type, reverse):
        driver = setup

        login = LoginPage(driver)
        inventory = InventoryPage(driver)

        logger.info(f"Starting Sorting Test : {sort_option}")

        login.open_application()
        login.login(STANDARD_USERNAME, STANDARD_PASSWORD)

        inventory.select_sort_option(sort_option)

        if sort_type == "name":
            actual_list = inventory.get_all_product_names()
        else:
            actual_list = inventory.get_all_product_prices()

        expected_list = sorted(actual_list, reverse=reverse)

        assert actual_list == expected_list, (f"{sort_option} Sorting Failed")

        logger.info(f"{sort_option} Sorting Passed")