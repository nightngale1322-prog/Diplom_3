import pytest
import allure
from urls import TestURL
from pages.lk_page import PersonalPage
from pages.main_page import MainPage
import data

class TestMainPage:
    @allure.title ("Проверка, что клик по кнопке 'Конструктор' открывает страницу конструктора")
    def test_click_on_constructor_button_opens_constructor_page_success(self,driver):
        main_page = MainPage(driver)
        main_page.go_to_url(TestURL.orders_page_url)
        main_page.check_click_to_constructor_button_opens_main_page()
        assert main_page.check_being_on_main_constructor_page()

    @allure.title ("Проверка, что клик по кнопке 'Лента заказов' открывает страницу заказов")
    def test_click_on_orders_page_goes_to_orders_page(self, driver):
        main_page = MainPage(driver)
        main_page.go_to_url(TestURL.login_page_url)
        main_page.check_click_to_orders_button_opens_orders_page()
        assert main_page.check_being_on_orders_page()
        
    @allure.title ("Проверка появления попапа при клике на ингредиент")
    def test_click_on_ingredient_opens_ingredient_popup(self, driver):
        main_page = MainPage(driver)
        main_page.go_to_url(TestURL.main_constructor_page_url)
        main_page.check_click_on_ingredient()
        assert main_page.check_popup_opens_after_click_on_ingredient()

    @allure.title ("Проверка закрытия попапа при клике на крестик попапа")
    def test_click_on_ingredient_popup_cross_closes_popup(self, driver):
        main_page = MainPage(driver)
        main_page.go_to_url(TestURL.main_constructor_page_url)
        main_page.check_click_on_ingredient()
        main_page.check_popup_opens_after_click_on_ingredient()
        main_page.check_popup_closes_after_pressing_cross()
        assert main_page.check_being_on_main_constructor_page()

    @allure.title ("Проверка увеличения каунтера ингредиента при добавлении в заказ")
    def test_counter_adds_value_after_adding_ingredient_to_order(self, driver):
        main_page = MainPage(driver)
        main_page.go_to_url(TestURL.main_constructor_page_url)
        main_page.check_adding_ingredient()
        assert main_page.check_counter_of_ingredient_after_adding_ingredient()

    @allure.title ("Проверка заказа залогином")
    def test_order_logged_in_user_success(self, driver):
        main_page = MainPage(driver)
        main_page.go_to_url(TestURL.login_page_url)
        main_page.check_login_acc_for_order()
        main_page.check_adding_ingredient()
        main_page.check_click_to_order_button_user_logged_in()
        assert main_page.check_modal_order_window_pops_up()

    @allure.title ("Проверка, что при заказе без логина кнопка отправляет на страницу входа")
    def test_order_not_logged_in_user_opens_login_page(self, driver):
        main_page = MainPage(driver)
        main_page.go_to_url(TestURL.main_constructor_page_url)
        main_page.check_adding_ingredient()
        main_page.check_click_to_order_button_user_not_logged_in()
        assert main_page.check_current_url() == TestURL.login_page_url