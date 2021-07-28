from selenium.webdriver.common.by import By


# class MainPageLocators():
    # LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")



class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTRATION_FORM = (By.CSS_SELECTOR, "#register_form")


class ProductPageLocators():
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, ".btn.btn-lg.btn-primary.btn-add-to-basket")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".alert-success")
    INFO_MESSAGE = (By.CSS_SELECTOR, ".alert-info")
    NAME_OF_BOOK = (By.CSS_SELECTOR, ".col-sm-6.product_main h1")
    PRICE_OF_BOOK = (By.CSS_SELECTOR, ".col-sm-6.product_main .price_color")


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    # LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc") Потом удалить если нигде не понадобится (Или раскомментить просто?)
    BASKET_BUTTON = (By.CSS_SELECTOR, ".btn-group .btn.btn-default")


class BasketPageLocators:
    BASKET_ITEMS = (By.CSS_SELECTOR, ".basket-items")
    MESSAGE_EMPTY_BASKET = (By.CSS_SELECTOR, "#content_inner > p")



