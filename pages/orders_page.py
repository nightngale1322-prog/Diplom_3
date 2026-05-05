from selenium.webdriver.common.by import By
import pytest
import allure
import data
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
    def check_today_count_going_up(self, previous_value=None):
        if previous_value is not None:
            self.wait.until(lambda driver: self.get_text_from_element(OrderPageLocators.ORDERS_TODAY_COUNT) > str(previous_value))
        count_number = self.get_text_from_element(OrderPageLocators.ORDERS_TODAY_COUNT)
        return int(count_number)
    
    @allure.step('Проверка счетчика заказов за все время')
    def check_all_count_going_up(self, previous_value=None):
        if previous_value is not None:
            self.wait.until(lambda driver: self.get_text_from_element(OrderPageLocators.ORDERS_COUNT) > str(previous_value))
        count_number = self.get_text_from_element(OrderPageLocators.ORDERS_COUNT)
        return int(count_number)

    @allure.step('Создание заказа с залогином')
    def check_order_after_log_in(self):
        if data.DRIVER_NAME == 'firefox':
            self.drag_and_drop_java(MainPageLocators.INGREDIENT_BUTTON_1,MainPageLocators.ORDER_INGREDIENT_FIELD)
            self.click_to_element(MainPageLocators.ORDER_BUTTON_NO_LOGIN)
            self.user_login(PersonalPageLocators.EMAIL_LOGIN_FIELD, '555@email.com')
            self.user_login(PersonalPageLocators.PASSWORD_LOGIN_FIELD, '12345Q')
            self.click_to_element(PersonalPageLocators.LOGIN_BUTTON)
            self.click_to_element(MainPageLocators.ORDER_PROGRESS_BUTTON)
        elif data.DRIVER_NAME == 'chrome':
            self.drag_and_drop(MainPageLocators.INGREDIENT_BUTTON_2,MainPageLocators.ORDER_INGREDIENT_FIELD)
            self.click_to_element(MainPageLocators.ORDER_BUTTON_NO_LOGIN)
            self.user_login(PersonalPageLocators.EMAIL_LOGIN_FIELD, '999@email.com')
            self.user_login(PersonalPageLocators.PASSWORD_LOGIN_FIELD, '54321Q')
            self.click_to_element(PersonalPageLocators.LOGIN_BUTTON)
            self.click_to_element(MainPageLocators.ORDER_PROGRESS_BUTTON)
        else:
            pass
    
    @allure.step('Возврат номера заказа из попапа')
    def check_order_number_in_popup(self):
        profile_order = self.find_element_with_wait(MainPageLocators.ORDER_POPUP_ORDER_NUMBER).text
        if profile_order != "9999":
            return profile_order
        else:
            self.wait.until (lambda driver: driver.find_element(*MainPageLocators.ORDER_POPUP_ORDER_NUMBER).text != "9999")
        real_profile_order = self.find_element_with_wait(MainPageLocators.ORDER_POPUP_ORDER_NUMBER).text
        formated_new_number = '#0' + real_profile_order
        return formated_new_number
        
    
    @allure.step ('Поиск номеров заказов на странице заказов')
    def check_return_orders_list(self):
        orders_el = self.find_elements(OrderPageLocators.ORDERS_IN_WORK_NUMBER)
        orders_list = []
        for element in orders_el:
            order_number = element.text.strip().lstrip('#').lstrip('0')
            if not order_number:
                order_number = '0'
            orders_list.append(order_number)
        return orders_list
        

    @allure.step ('Поиск номеров завершенных заказов на странице заказов')
    def check_return_orders_list(self):
        orders_el = self.find_elements(OrderPageLocators.BURGER_ORDERED_LIST)
        orders_list = []
        for element in orders_el:
            order_number = element.text.strip()
            if not order_number:
                order_number = '0'
            orders_list.append(order_number)
        return orders_list

    
      
        
    @allure.step('Получение номера заказа из истории заказа')
    def check_go_to_history_find_order(self):
        self.check_login_no_order()
        self.go_to_url(TestURL.orders_page_url)
        self.go_to_url(TestURL.lk_url)
        self.click_to_element(PersonalPageLocators.ORDERS_HISTORY_BUTTON)
        orders_el = self.find_elements(PersonalPageLocators.PROFILE_ORDER)
        orders_list = []
        for element in orders_el:
            order_number = element.text.strip().lstrip('#')
            orders_list.append(order_number)
            if not order_number:
                order_number = '0'
                orders_list.append(order_number)
        return orders_list[-1]
    
    @allure.step("Логин через кнопку заказа без заказа")
    def check_login_no_order(self):
        if data.DRIVER_NAME == 'chrome':
            self.go_to_url(TestURL.main_constructor_page_url)
            self.drag_and_drop(MainPageLocators.INGREDIENT_BUTTON_2,MainPageLocators.ORDER_INGREDIENT_FIELD)
            self.click_to_element(MainPageLocators.ORDER_BUTTON_NO_LOGIN)
            self.user_login(PersonalPageLocators.EMAIL_LOGIN_FIELD, '999@email.com')
            self.user_login(PersonalPageLocators.PASSWORD_LOGIN_FIELD, '54321Q')
            self.click_to_element(PersonalPageLocators.LOGIN_BUTTON)
            self.find_element_with_wait(MainPageLocators.INGREDIENT_BUTTON_1)
        else:
            self.go_to_url(TestURL.main_constructor_page_url)
            self.drag_and_drop_java(MainPageLocators.INGREDIENT_BUTTON_2,MainPageLocators.ORDER_INGREDIENT_FIELD)
            self.click_to_element(MainPageLocators.ORDER_BUTTON_NO_LOGIN)
            self.user_login(PersonalPageLocators.EMAIL_LOGIN_FIELD, '999@email.com')
            self.user_login(PersonalPageLocators.PASSWORD_LOGIN_FIELD, '54321Q')
            self.click_to_element(PersonalPageLocators.LOGIN_BUTTON)
            self.find_element_with_wait(MainPageLocators.INGREDIENT_BUTTON_1)