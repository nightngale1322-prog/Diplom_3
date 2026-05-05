from selenium.webdriver.common.by import By
import pytest
import allure
from urls import TestURL
from pages.base_page import BasePage
from locators.password_page_locators import PasswordPageLocators
from locators.main_page_locators import MainPageLocators
import data
from selenium.webdriver.support import expected_conditions

class PasswordPage (BasePage):
    
    @allure.step('Переход на страницу восстановления пароля со страницы личного кабинета')
    def check_click_to_reset_password(self):
        if data.DRIVER_NAME == 'firefox':
            self.wait.until(expected_conditions.invisibility_of_element_located(MainPageLocators.OVERLAY))
        else: 
            pass
        self.click_element_after_scroll(PasswordPageLocators.PASSWORD_BUTTON_LOGIN_PAGE)
    
    @allure.step('Ввод email')
    def check_send_email(self):
        if data.DRIVER_NAME == 'firefox':
            self.wait.until(expected_conditions.invisibility_of_element_located(MainPageLocators.OVERLAY))
        else: 
            pass
        self.send_keys_to_element_with_click(PasswordPageLocators.PASSWORD_RESET_EMAIL_FIELD, '1@email.com')

    @allure.step ('Клик на кнопку "Восстановить')
    def check_click_reset_password_button(self):
        if data.DRIVER_NAME == 'firefox':
            self.wait.until(expected_conditions.invisibility_of_element_located(MainPageLocators.OVERLAY))
        else: 
            pass
        self.click_element_after_scroll(PasswordPageLocators.PASSWORD_RESET_BUTTON)

    @allure.step ('Проверка перехода на страницу восстановления пароля')
    def check_password_reset_window(self):
        if data.DRIVER_NAME == 'firefox':
            self.wait.until(expected_conditions.invisibility_of_element_located(MainPageLocators.OVERLAY))
        else: 
            pass
        password_page = self.find_element_with_wait(PasswordPageLocators.PASSWORD_PAGE_HEADER)
        return password_page

    @allure.step ('Проверка перехода на страницу восстановления пароля после ввода почты')
    def check_password_reset_window_after_email(self):
        if data.DRIVER_NAME == 'firefox':
            self.wait.until(expected_conditions.invisibility_of_element_located(MainPageLocators.OVERLAY))
        else: 
            pass
        password_page = self.find_element_with_wait(PasswordPageLocators.PASSWORD_PAGE_AFTER_EMAIL)
        return password_page

    @allure.step('Проверка активности поля по клику на "глазик"')
    def check_click_on_eye_icon_active_field(self):
        if data.DRIVER_NAME == 'firefox' and self.find_element(MainPageLocators.OVERLAY) == True:
            self.wait.until(expected_conditions.invisibility_of_element_located(MainPageLocators.OVERLAY))
        else: 
            pass
        self.click_to_element(PasswordPageLocators.PASSWORD_EYE_BUTTON)
        

    @allure.step('Проверка активности поля')
    def check_active_password_field(self):
        if data.DRIVER_NAME == 'firefox':
            self.wait.until(expected_conditions.invisibility_of_element_located(MainPageLocators.OVERLAY))
        else: 
            pass
        password_active = self.find_element_with_wait(PasswordPageLocators.PASSWORD_FIELD_FOCUS_STATE)
        return password_active 