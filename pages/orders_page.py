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
        if data.DRIVER_NAME == 'firefox':
            self.drag_and_drop(MainPageLocators.INGREDIENT_BUTTON_1,MainPageLocators.ORDER_INGREDIENT_FIELD)
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
    
    @allure.step('Проверка, что заказ пользователя есть в ленте заказов')
    def check_order_in_orders_feed(self):
        profile_order = self.find_element_with_wait(MainPageLocators.ORDER_POPUP_ORDER_NUMBER)
        order_text = profile_order.text.strip()  
        self.go_to_url(TestURL.orders_page_url)

        locator = (
            By.XPATH,
            f".//div/div/ul[@class = 'OrderFeed_orderListReady__1YFem OrderFeed_orderList__cBvyi']/li[contains(text(), '{order_text}')]"
    )
    
        feed_orders = self.find_element_with_wait(locator)

        return feed_orders
