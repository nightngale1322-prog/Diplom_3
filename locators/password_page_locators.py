from selenium.webdriver.common.by import By

class PasswordPageLocators:
    PASSWORD_BUTTON_LOGIN_PAGE = By.XPATH, './/div/p/a[contains(text(), "Восстановить пароль")]'
    PASSWORD_RESET_EMAIL_FIELD = By.XPATH, './/div/div/input'
    PASSWORD_RESET_BUTTON = By.XPATH, './/main/div/form/button'
    PASSWORD_EYE_BUTTON = By.CSS_SELECTOR, '.input__icon'
    PASSWORD_FIELD_FOCUS_STATE = By.XPATH, ".//div/input[@type='text']"
    PASSWORD_PAGE_HEADER = By.XPATH, './/div[@class="Auth_login__3hAey"]/h2[contains(text(), "Восстановление пароля")]'
    PASSWORD_PAGE_AFTER_EMAIL = By.XPATH, './/main/div/div/p[contains(text(), "Вспомнили пароль?")]'
