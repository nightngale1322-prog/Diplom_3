import pytest
import allure
from urls import TestURL
from pages.password_page import PasswordPage
import data

class TestPasswordPage:
    @allure.title ("Проверка, что переход по кнопке восстановления пароля открывает нужную страницу")
    def test_click_on_reset_password_gets_to_password_page_success(self,driver):
        password_page = PasswordPage(driver)
        password_page.go_to_url(TestURL.login_page_url)
        password_page.check_click_to_reset_password()
        assert password_page.check_password_reset_window()

    @allure.title ("Проверка, что ввод почты и клик по кнопке 'Восстановить' открывает нужную страницу")
    def test_password_page_email_input_forward_success(self,driver):
        password_page = PasswordPage(driver)
        password_page.go_to_url(TestURL.forget_password_url)
        password_page.check_send_email()
        password_page.check_click_reset_password_button()
        assert password_page.check_password_reset_window_after_email()

    @allure.title ("Проверка, что иконка глазика делает поле Пароль активным")
    def test_password_active_field_lights_up_success(self,driver):
        password_page = PasswordPage(driver)
        password_page.go_to_url(TestURL.login_page_url)
        password_page.check_click_to_reset_password()
        password_page.check_send_email()
        password_page.check_click_reset_password_button()
        password_page.check_click_on_eye_icon_active_field()
        assert password_page.check_active_password_field()