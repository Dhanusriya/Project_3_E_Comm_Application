from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class CartPage(BasePage):
    cart_icon = (By.CLASS_NAME, "shopping_cart_link")
    cart_items = (By.CLASS_NAME, "cart_item")
    item_name = (By.CLASS_NAME, "inventory_item_name")
    item_price = (By.CLASS_NAME, "inventory_item_price")

    def open_cart(self):
        self.click(self.cart_icon)

    def get_cart_products(self):
        cart_products = []
        items = self.get_elements(self.cart_items)

        for item in items:
            name = item.find_element(By.CLASS_NAME, "inventory_item_name").text
            price = item.find_element(By.CLASS_NAME, "inventory_item_price").text
            cart_products.append(
                {
                    "name": name,
                    "price": price
                }
            )

        return cart_products