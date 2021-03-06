from test_final_task.pages.base_page import BasePage
from test_final_task.pages.locators import BasketPageLocators


class BasketPage(BasePage):

    def should_be_no_items_in_the_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_FORMSET, ),\
            "Basket formset is presented, but should not be"

    def should_be_text_that_basket_is_empty(self):
        assert self.is_element_present(*BasketPageLocators.BASKET_EMPTY_TEXT, ), \
            "Basket is not empty"


