from selenium.webdriver.common.by import By
import pytest
import allure
from urls import TestURL
from pages.base_page import BasePage
from locators.personal_page_locators import PersonalPageLocators
from locators.main_page_locators import MainPageLocators
from selenium.webdriver.support import expected_conditions

class PersonalPage(BasePage):

    @allure.step('Клик на личный кабинет')
    def check_click_to_go_to_lk(self):
        self.click_to_element(PersonalPageLocators.LK_BUTTON)

    @allure.step('Клик на кнопку истории заказов в личном кабинете')
    def check_click_on_order_history_button(self):
        self.click_to_element(PersonalPageLocators.ORDERS_HISTORY_BUTTON)

    @allure.step('Клик на кнопку выхода из аккаунта')
    def check_click_on_exit_lk_button(self):
        self.click_to_element(PersonalPageLocators.LOGOUT_BUTTON)
        self.find_element_with_wait(PersonalPageLocators.LOGIN_BUTTON) #ожидание прогрузки страницы

    @allure.step('Проверка нахождения на странице входа')
    def check_click_goes_to_login_page(self):
        button = self.find_element_with_wait(PersonalPageLocators.LOGIN_BUTTON)
        return button

    @allure.step('Проверка нахождения в личном кабинете')
    def check_click_goes_to_personal_page(self):
        button = self.find_element_with_wait(PersonalPageLocators.PROFILE_BUTTON)
        return button
    
    @allure.step('Проверка перехода в раздел Истории заказов в личном кабинете')
    def check_click_goes_to_order_history_on_lk_page(self):
        self.click_to_element(PersonalPageLocators.ORDERS_HISTORY_BUTTON)

    @allure.step('Проверка нахождения на странице истории заказов')
    def check_click_goes_to_order_history_page(self):
        button = self.find_element_with_wait(PersonalPageLocators.LOGIN_BUTTON)
        return button

    @allure.step('Залогин пользователем в ЛК')
    def check_login_acc(self):
        self.user_login(PersonalPageLocators.EMAIL_LOGIN_FIELD, '555@email.com')
        self.user_login(PersonalPageLocators.PASSWORD_LOGIN_FIELD, '12345Q')
        self.click_to_element(PersonalPageLocators.LOGIN_BUTTON)
        self.find_element_with_wait(MainPageLocators.INGREDIENT_BUTTON) #ожидание прогрузки страницы

    @allure.step('Возврат адреса текущей страницы')
    def check_current_url(self):
        return self.driver.current_url