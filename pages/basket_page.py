from .base_page import BasePage
from .locators import BasketPageLocators

class BasketPage(BasePage):
    def checking_basket(self):
        self.go_to_basket()
        self.no_items_in_basket()
        self.can_see_message_empty_basket()

    def no_items_in_basket(self):
        assert self.is_element_present(*BasketPageLocators.EMPTY_BASKET_TEXT), \
            "Basket NOT empty, but must be"

    def can_see_message_empty_basket(self):
        assert self.is_element_present(*BasketPageLocators.EMPTY_BASKET_TEXT), \
        "Text: 'Your basket is empty.' - not present at the basket page"

    def cant_see_basket_button_in_header(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_BUTTON_IN_HEADER), \
        "Basket [button] present in the header, but it shouldn't be"