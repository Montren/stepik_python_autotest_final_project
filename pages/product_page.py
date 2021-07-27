from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_to_basket(self):
        button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        button.click()

    def name_of_book_is_correct(self):
        window_of_messages = self.browser.find_element(*ProductPageLocators.WINDOW_OF_MESSAGES)
        name_of_book = self.browser.find_element(*ProductPageLocators.NAME_OF_BOOK)
        assert name_of_book.text + " " + "has been added to your basket." in window_of_messages.text, "Name of book is incorrect"

    def price_of_book_is_correct(self):
        window_of_messages = self.browser.find_element(*ProductPageLocators.WINDOW_OF_MESSAGES)
        price_of_book = self.browser.find_element(*ProductPageLocators.PRICE_OF_BOOK)
        assert "Your basket total is now " + price_of_book.text in window_of_messages.text, "Price of book is incorrect"


