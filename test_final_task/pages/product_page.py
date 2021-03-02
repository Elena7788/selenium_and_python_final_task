from .base_page import BasePage
from .locators import LoginPageLocators, ProductPageLocators


class ProductPage(BasePage):
    def add_product_to_basket(self):
        button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_FORM)
        button.click()

    def should_be_product_name_in_basket(self):
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        added_product_name = self.browser.find_element(*ProductPageLocators.ADDED_NAME).text
        assert product_name == added_product_name, "Error name"

    def should_be_product_price_in_basket(self):
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        added_product_price = self.browser.find_element(*ProductPageLocators.ADDED_PRICE).text
        assert product_price == added_product_price, "Error price"





