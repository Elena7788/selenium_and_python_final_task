import pytest
from .pages.main_page import MainPage
from .pages.login_page import LoginPage
from .pages.basket_page import BasketPage
import time


@pytest.mark.login_guest
class TestLoginFromMainPage:
    def test_guest_can_go_to_login_page(self, browser):
        link = "http://selenium1py.pythonanywhere.com"
        page = MainPage(browser, link)
        page.open()
        page.go_to_login_page()
        login_page = LoginPage(browser, browser.current_url)
        login_page.should_be_login_page()

    def test_guest_should_see_login_link(self, browser):
        link = "http://selenium1py.pythonanywhere.com/"
        page = MainPage(browser, link)
        page.open()
        page.should_be_login_link()

'''
def test_1_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()                      # открываем страницу
    page.go_to_login_page()          # выполняем метод страницы — переходим на страницу логина
'''

'''
def test_2_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com"
    page = MainPage(browser, link)
    page.open()
    login_page = page.go_to_login_page()
    login_page.should_be_login_page()
'''

'''
@pytest.mark.login
class TestLoginFromProductPage():
    @pytest.fixture(scope="function", autouse=True)
    def setup(self):
        self.product = ProductFactory(title = "Best book created by robot")
        # создаем по апи
        self.link = self.product.link
        yield
        # после этого ключевого слова начинается teardown
        # выполнится после каждого теста в классе
        # удаляем те данные, которые мы создали 
        self.product.delete()
        

    def test_guest_can_go_to_login_page_from_product_page(self, browser):
        page = ProductPage(browser, self.link)
        # дальше обычная реализация теста

    def test_guest_should_see_login_link(self, browser):
        page = ProductPage(browser, self.link)
        # дальше обычная реализация теста 
'''


def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)
    page.open()
    page.view_basket()
    time.sleep(5)
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_be_no_items_in_the_basket()
    basket_page.should_be_text_that_basket_is_empty()




