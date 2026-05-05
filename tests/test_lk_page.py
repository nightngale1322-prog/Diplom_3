import pytest
import allure
from urls import TestURL
from pages.lk_page import PersonalPage
import data
from locators.personal_page_locators import PersonalPageLocators

class TestPersonalPage:
    @allure.title ("Проверка, что нажатие на кнопку личного кабинета незалогином открывает страницу входа")
    def test_click_on_lk_button_non_login_user_goes_to_login_page(self,driver):
        lk_page = PersonalPage(driver)
        lk_page.go_to_url(TestURL.orders_page_url)
        lk_page.check_click_to_go_to_lk()
        assert lk_page.check_click_goes_to_login_page()

    @allure.title ("Проверка, что нажатие на кнопку личного кабинета залогином открывает ЛК")
    def test_click_on_lk_button_login_user_goes_to_lk(self,driver):
        lk_page = PersonalPage(driver)
        lk_page.go_to_url(TestURL.login_page_url)
        lk_page.check_login_acc()
        lk_page.go_to_url(TestURL.orders_page_url) # иначе кнопка личного кабинета некликабельная
        lk_page.check_click_to_go_to_lk()
        assert lk_page.check_click_goes_to_personal_page()

    @allure.title ("Проверка, что нажатие на кнопку истории заказов в личном кабинете залогина открывает страницу заказов")
    def test_click_on_order_history_button_login_goes_to_user_orders(self,driver):
        lk_page = PersonalPage(driver)
        lk_page.go_to_url(TestURL.login_page_url)
        lk_page.check_login_acc()
        lk_page.go_to_url(TestURL.orders_page_url) # иначе кнопка личного кабинета некликабельная
        lk_page.check_click_to_go_to_lk()
        lk_page.check_click_goes_to_order_history_on_lk_page()
        assert 'account/order-history' in lk_page.check_current_url()

    @allure.title ("Проверка, что нажатие на кнопку выхода из личного кабинета залогином ведет на страницу входа")
    def test_click_on_lk_exit_button_goes_to_login_page(self,driver):
        lk_page = PersonalPage(driver)
        lk_page.go_to_url(TestURL.login_page_url)
        lk_page.check_login_acc()
        lk_page.go_to_url(TestURL.orders_page_url) # иначе кнопка личного кабинета некликабельная
        lk_page.check_click_to_go_to_lk()
        lk_page.check_click_on_exit_lk_button()
        assert lk_page.check_click_goes_to_login_page()