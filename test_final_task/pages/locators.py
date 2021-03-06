from selenium.webdriver.common.by import By


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")


class BasketPageLocators:
    VIEW_BASKET = (By.CSS_SELECTOR, ".basket-mini>span>a")
    BASKET_FORMSET = (By.CSS_SELECTOR, "#basket_formset")
    BASKET_EMPTY_TEXT = (By.CSS_SELECTOR, "#content_inner>p>a")

class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")


class ProductPageLocators:
    ADD_TO_BASKET_FORM = (By.CSS_SELECTOR, "#add_to_basket_form")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages .alert")
    PRODUCT_PRICE = (By.CSS_SELECTOR, "#content_inner>article>div>div>p.price_color")
    ADDED_PRICE = (By.CSS_SELECTOR, "#messages>div>div>p:nth-child(1)>strong")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main>h1")
    ADDED_NAME = (By.CSS_SELECTOR, "#messages>div:nth-child(1)>div>strong")
