from selenium.webdriver.common.by import By

class PersonalPageLocators:
    LK_BUTTON = By.XPATH, './/div/header/nav/a[@class="AppHeader_header__link__3D_hX"]'
    ORDERS_HISTORY_BUTTON = By.XPATH, './/ul/li/a[contains(text(), "История заказов")]'
    LOGOUT_BUTTON = By.XPATH, './/li/button[contains(text(),"Выход")]'
    EMAIL_LOGIN_FIELD = By.XPATH, './/fieldset/div/div/input'
    PASSWORD_LOGIN_FIELD = By.XPATH, './/div/div/input[@name="Пароль"]'
    LOGIN_BUTTON = By.CSS_SELECTOR, '.button_button__33qZ0'
    PROFILE_BUTTON = By.XPATH, './/nav/ul/li/a[@href="/account/profile"]'
    PROFILE_ORDER = By.XPATH, './/div/ul/li/a/div[@class="OrderHistory_textBox__3lgbs mb-6"]/p[starts-with(text(), "#")]'
