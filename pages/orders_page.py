from selenium.webdriver.common.by import By
import pytest
import allure
from urls import TestURL
from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators
from locators.order_page_locators import OrderPageLocators
from selenium.webdriver.support import expected_conditions
from locators.personal_page_locators import PersonalPageLocators

class OrdersPage (BasePage):
    
    @allure.step('Клик на заказ')
    def check_click_on_order(self):
        self.click_to_element(OrderPageLocators.BURGER_ORDERED_LIST)

    @allure.step('Проверка наличия всплывающего окна')
    def check_order_popup_after_click(self):
        popup = self.find_element_with_wait(OrderPageLocators.ORDER_POPUP_WINDOW)
        return popup
    
    @allure.step('Проверка счетчика сегодняшних заказов')
    def check_today_count_going_up(self):
        count_number = self.get_text_from_element(OrderPageLocators.ORDERS_TODAY_COUNT)
        count_number_int = int (count_number)
        return count_number_int
    
    @allure.step('Проверка счетчика заказов за все время')
    def check_all_count_going_up(self):
        count_number = self.get_text_from_element(OrderPageLocators.ORDERS_COUNT)
        count_number_int = int (count_number)
        return count_number_int

    @allure.step('Создание заказа с залогином')
    def check_order_after_log_in(self):
        self.drag_and_drop(MainPageLocators.INGREDIENT_BUTTON,MainPageLocators.ORDER_INGREDIENT_FIELD)
        self.click_to_element(MainPageLocators.ORDER_BUTTON_NO_LOGIN)
        self.user_login(PersonalPageLocators.EMAIL_LOGIN_FIELD, '555@email.com')
        self.user_login(PersonalPageLocators.PASSWORD_LOGIN_FIELD, '12345Q')
        self.click_to_element(PersonalPageLocators.LOGIN_BUTTON)
        self.click_to_element(MainPageLocators.ORDER_PROGRESS_BUTTON)

    @allure.step('Поиск номера заказа в "В работе"')
    def check_find_order_number_in_list_awaiting_orders(self):
        self.dissapear_element(OrderPageLocators.ORDERS_IN_PROGRESS)
        list = self.find_elements_with_wait(OrderPageLocators.ORDERS_IN_PROGRESS_NUMBER)
        order = list[0]
        return order
    
    @allure.step('Поиск номера заказа в ленте заказа')
    def check_find_order_number_in_list_orders_feed(self):
        list_of_working_orders = self.find_elements_with_wait(OrderPageLocators.ORDERS_IN_PROGRESS)
        order = list_of_working_orders[0]
        order_text = order.text.strip()
        locator = (By.XPATH, f"//div[contains(text(), '{order_text}')]")
        feed_orders = self.find_elements_with_wait(locator)

        return feed_orders