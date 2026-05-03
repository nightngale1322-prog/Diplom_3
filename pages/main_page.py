from selenium.webdriver.common.by import By
import pytest
import allure
from urls import TestURL
from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators
from locators.order_page_locators import OrderPageLocators
from selenium.webdriver.support import expected_conditions
from locators.personal_page_locators import PersonalPageLocators

class MainPage (BasePage):
    
    @allure.step('Переход на главную страницу через клик по "Конструктор"')
    def check_click_to_constructor_button_opens_main_page(self):
        self.click_to_element(MainPageLocators.CONSTRUCTION_BUTTON)

    @allure.step('Проверка нахождения на странице конструктора')
    def check_being_on_main_constructor_page(self):
        elem = self.find_element_with_wait(MainPageLocators.INGREDIENT_BUTTON_1)
        return elem
    
    @allure.step('Переход на страницу "Лента заказов" кликом на кнопку "Лента заказов"')
    def check_click_to_orders_button_opens_orders_page(self):
        self.go_to_url('https://qa-stellarburgers.education-services.ru/login')
        self.click_to_element(MainPageLocators.CONSTRUCTION_BUTTON)

    @allure.step('Проверка нахождения на странице заказов')
    def check_being_on_orders_page(self):
        orders = self.find_element_with_wait(OrderPageLocators.ORDER_PAGE_HEADER)
        return orders
    
    @allure.step('Проверка клика на ингредиент')
    def check_click_on_ingredient(self):
        self.click_to_element(MainPageLocators.INGREDIENT_BUTTON_1)

    @allure.step('Проверка клика на ингредиент и открытие попапа')
    def check_popup_opens_after_click_on_ingredient(self):
        popup = self.find_element_with_wait(MainPageLocators.INGREDIENT_POPUP)
        return popup
    
    @allure.step('Закрытие попапа об ингредиенте')
    def check_popup_closes_after_pressing_cross(self):
        self.click_to_element(MainPageLocators.POPUP_CLOSE_BUTTON)
        
    @allure.step('Перетаскивание ингредиента')
    def check_adding_ingredient(self):
        self.drag_and_drop (MainPageLocators.INGREDIENT_BUTTON_1, MainPageLocators.ORDER_INGREDIENT_FIELD)

    @allure.step('Проверка каунтера ингредиента после добавления ингредиента')
    def check_counter_of_ingredient_after_adding_ingredient(self):
        counter = self.find_element_with_wait(MainPageLocators.INGREDIENT_COUNTER)
        return counter

    @allure.step('Клик по кнопке "Оформить заказ" залогином')
    def check_click_to_order_button_user_logged_in(self):
        self.click_to_element(MainPageLocators.ORDER_PROGRESS_BUTTON)

    @allure.step('Проверка появления окна после оформления заказа')
    def check_modal_order_window_pops_up(self):
        window = self.find_element_with_wait(MainPageLocators.ORDER_POPUP_IDENTIFICATOR)
        return window
    
    @allure.step('Клик по кнопке "Войти в аккаунт" справа незалогином')
    def check_click_to_order_button_user_not_logged_in(self):
        self.click_to_element(MainPageLocators.ORDER_BUTTON_NO_LOGIN)
    
    @allure.step('Возврат адреса текущей страницы')
    def check_current_url(self):
        return self.driver.current_url
    
    @allure.step('Залогин пользователем в ЛК')
    def check_login_acc_for_order(self):
        self.user_login(PersonalPageLocators.EMAIL_LOGIN_FIELD, '555@email.com')
        self.user_login(PersonalPageLocators.PASSWORD_LOGIN_FIELD, '12345Q')
        self.click_to_element(PersonalPageLocators.LOGIN_BUTTON)
        self.find_element_with_wait(MainPageLocators.INGREDIENT_BUTTON_1) #ожидание прогрузки страницы