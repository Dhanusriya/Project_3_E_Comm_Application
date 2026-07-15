import random
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class InventoryPage(BasePage):
    title = (By.CLASS_NAME, "title")
    cart_icon = (By.CLASS_NAME, "shopping_cart_link")
    products = (By.CLASS_NAME, "inventory_item")
    product_name = (By.CLASS_NAME, "inventory_item_name")
    product_price = (By.CLASS_NAME, "inventory_item_price")
    cart_badge = (By.CLASS_NAME, "shopping_cart_badge")
    sort_dropdown = (By.CLASS_NAME, "product_sort_container")
    product_names = (By.CLASS_NAME, "inventory_item_name")
    product_prices = (By.CLASS_NAME, "inventory_item_price")

    def inventory_displayed(self):
        return self.get_text(self.title)

    def is_cart_icon_displayed(self):
        return self.is_displayed(self.cart_icon)

    def get_random_products(self):
        all_products = self.get_elements(self.products)
        random_products = random.sample(all_products, 4)
        selected_products = []

        for product in random_products:
            name = product.find_element(*self.product_name).text
            price = product.find_element(*self.product_price).text

            #Click add to cart
            product.find_element(By.TAG_NAME, "button").click()

            selected_products.append(
                {
                    "name": name,
                    "price": price
                }
            )
        return selected_products

    def get_cart_count(self):
        return self.get_text(self.cart_badge)

    def select_sort_option(self, option):
        dropdown = Select(self.get_element(self.sort_dropdown))
        dropdown.select_by_visible_text(option)

    def get_all_product_names(self):
        names =[]

        products = self.get_elements(self.product_names)

        for product in products:
            names.append(product.text)

        return names

    def get_all_product_prices(self):
        prices = []
        products = self.get_elements(self.product_prices)
        for product in products:
            prices.append(float(product.text.replace("$", "")))

        return prices

    def is_cart_badge_displayed(self):
        return self.is_element_present(self.cart_badge)