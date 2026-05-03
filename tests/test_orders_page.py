import pytest
import allure
from urls import TestURL
from pages.orders_page import OrdersPage
import data

class TestOrdersPage:
    @allure.title ("Проверка, что нажатие на заказ открывает всплывающее окно с заказом")
    def test_click_on_order_opens_order_popup(self,driver):
        orders_page = OrdersPage(driver)
        orders_page.go_to_url(TestURL.orders_page_url)
        orders_page.check_click_on_order()
        assert orders_page.check_order_popup_after_click()

    @allure.title ("Проверка, что заказ пользователя приходит в ленту 'В работе'") #может таймаутнуть из-за долгого появления номера заказа (проблема сайта)
    def test_order_created_goes_to_working_list(self,driver):
        orders_page = OrdersPage(driver)
        orders_page.go_to_url(TestURL.main_constructor_page_url)
        orders_page.check_order_after_log_in()
        orders_page.go_to_url(TestURL.orders_page_url)
        assert orders_page.check_find_order_number_in_list_awaiting_orders()


    @allure.title ("Проверка, что заказ пользователя приходит в ленту заказов") #может таймаутнуть из-за долгого появления номера заказа (проблема сайта)
    def test_order_created_goes_to_orders_list(self,driver):
        orders_page = OrdersPage(driver)
        orders_page.go_to_url(TestURL.main_constructor_page_url)
        orders_page.check_order_after_log_in()
        orders_page.go_to_url(TestURL.orders_page_url)
        assert orders_page.check_find_order_number_in_list_orders_feed()
        

    @allure.title ("Проверка увеличения счетчика 'Выполнено за все время' после заказа")
    def test_order_created_goes_to_all_orders_count(self,driver):
        orders_page = OrdersPage(driver)
        orders_page.go_to_url(TestURL.main_constructor_page_url)
        orders_page.check_order_after_log_in()
        orders_page.go_to_url(TestURL.orders_page_url)
        assert orders_page.check_today_count_going_up() > 377100


    @allure.title ("Проверка увеличения счетчика 'Выполнено за сегодня' после заказа")
    def test_order_created_goes_to_today_orders_count(self,driver):
        orders_page = OrdersPage(driver)
        orders_page.go_to_url(TestURL.main_constructor_page_url)
        orders_page.check_order_after_log_in()
        orders_page.go_to_url(TestURL.orders_page_url)
        assert orders_page.check_all_count_going_up() >= 1