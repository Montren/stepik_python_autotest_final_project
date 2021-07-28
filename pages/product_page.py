from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_to_basket(self):
        button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        button.click()

    def name_of_book_is_correct(self):
        window_of_messages = self.browser.find_element(*ProductPageLocators.SUCCESS_MESSAGE)
        name_of_book = self.browser.find_element(*ProductPageLocators.NAME_OF_BOOK)
        assert name_of_book.text + " " + "has been added to your basket." in window_of_messages.text, "Name of book is incorrect"

    def price_of_book_is_correct(self):
        window_of_messages = self.browser.find_element(*ProductPageLocators.INFO_MESSAGE)
        price_of_book = self.browser.find_element(*ProductPageLocators.PRICE_OF_BOOK)
        assert "Your basket total is now " + price_of_book.text in window_of_messages.text, "Price of book is incorrect"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def should_disappeared_message(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Message is not disappeared, but should be"
