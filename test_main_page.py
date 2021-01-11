from .pages.main_page import MainPage
from .pages.login_page import LoginPage
from .pages.basket_page import BasketPage
import pytest


@pytest.mark.login_guest
class TestLoginFromMainPage():
    def test_guest_can_see_login_url(self, browser):
        link = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"
        page = LoginPage(browser, link)
        page.open()
        page.should_be_login_url()

    def test_guest_can_see_login_form(self, browser):
        link = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"
        page = LoginPage(browser, link)
        page.open()
        page.should_be_login_form()


#def test_guest_should_see_login_link(browser):
#    link = "http://selenium1py.pythonanywhere.com/"
#    page = MainPage(browser, link) # инициализируем Page Object, передаем в конструктор #экземпляр драйвера и url адрес
#    page.open()
#    page.should_be_login_link()



def test_guest_can_see_register_form(browser):
    link = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"
    page = LoginPage(browser, link)
    page.open()
    page.should_be_register_form()

def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = BasketPage(browser, link)
    page.open()
    page.checking_basket()


@pytest.mark.xfail(reason="Basket [button] present in the header, but it shouldn't be")
def test_guest_cant_see_basket_button_at_main_page_in_head(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = BasketPage(browser, link)
    page.open()
    page.cant_see_basket_button_in_header()
