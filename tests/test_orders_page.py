import pytest
import allure
from urls import TestURL
from pages.orders_page import OrdersPage
import data

class TestOrdersPage:

    @allure.title ("Проверка, что заказ пользователя есть в ленте 'В работе'") #может таймаутнуть из-за долгого появления номера заказа (проблема сайта)
    def test_new_order_is_in_orders_list(self,driver):
        orders_page = OrdersPage(driver)
        orders_page.go_to_url(TestURL.main_constructor_page_url)
        orders_page.check_order_after_log_in()
        order_number = orders_page.check_order_number_in_popup()
        orders_page.go_to_url(TestURL.orders_page_url)
        orders_page.check_refresh_for_orders()
        all_orders = orders_page.check_return_orders_list()
        assert order_number in all_orders


    @allure.title ("Проверка, что нажатие на заказ открывает всплывающее окно с заказом")
    def test_click_on_order_opens_order_popup(self,driver):
        orders_page = OrdersPage(driver)
        orders_page.go_to_url(TestURL.orders_page_url)
        orders_page.check_click_on_order()
        assert orders_page.check_order_popup_after_click()
        
     

    @allure.title ("Проверка увеличения счетчика 'Выполнено за все время' после заказа")
    def test_order_created_goes_to_all_orders_count(self,driver):
        orders_page = OrdersPage(driver)
        orders_page.go_to_url(TestURL.orders_page_url)

        counter_all_beginning = orders_page.check_all_count_going_up()
        orders_page.go_to_url(TestURL.main_constructor_page_url)
        orders_page.check_order_after_log_in()
        orders_page.go_to_url(TestURL.orders_page_url)
        orders_page.check_refresh_for_orders()
        new_counter = orders_page.check_all_count_going_up(previous_value=counter_all_beginning)
        assert new_counter > counter_all_beginning  


    @allure.title ("Проверка увеличения счетчика 'Выполнено за сегодня' после заказа")
    def test_order_created_goes_to_today_orders_count(self,driver):
        orders_page = OrdersPage(driver)
        orders_page.go_to_url(TestURL.orders_page_url)
        counter_today_beginning = orders_page.check_today_count_going_up()
        orders_page.go_to_url(TestURL.main_constructor_page_url)
        orders_page.check_order_after_log_in()
        orders_page.go_to_url(TestURL.orders_page_url)
        orders_page.check_refresh_for_orders()
        new_counter = orders_page.check_today_count_going_up(previous_value=counter_today_beginning)
        assert orders_page.check_today_count_going_up() > counter_today_beginning

    @allure.title ("Проверка нахождения номера из истории пользователя в завершенных заказа")
    def test_order_from_history_goes_to_all_orders(self,driver):
        orders_page = OrdersPage(driver)
        orders_page.go_to_url(TestURL.login_page_url)
        order_number = orders_page.check_go_to_history_find_order()
        new_order_number = '#' + order_number
        orders_page.go_to_url(TestURL.orders_page_url)
        orders = orders_page.check_return_orders_list()
        assert new_order_number in orders