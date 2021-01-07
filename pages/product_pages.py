from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_product_to_basket(self):
        button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET)
        button.click()

    def product_comparison_actual_and_added_in_basket(self):
        actual_product = self.browser.find_element(*ProductPageLocators.PRODUCT_WE_BOUGHT).text
        added_product = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_IN_BASKET).text
        assert actual_product == added_product, "Product name is not same"

    def cost_basket_is_same_as_price_item(self):
        cost_basket = self.browser.find_element(*ProductPageLocators.BASKET_VALUE).text
        price_item = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        assert cost_basket == price_item, "Different basket and product prices"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def check_success_message_is_disappeared(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is not disappeared"
