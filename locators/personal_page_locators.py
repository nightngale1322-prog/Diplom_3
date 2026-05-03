from selenium.webdriver.common.by import By

class PersonalPageLocators:
    LK_BUTTON = By.XPATH, './/div/header/nav/a[@class="AppHeader_header__link__3D_hX"]'
    ORDERS_HISTORY_BUTTON = By.XPATH, './/ul/li/a[contains(text(), "История заказов")]'
    LOGOUT_BUTTON = By.XPATH, './/li/button[contains(text(),"Выход")]'
    EMAIL_LOGIN_FIELD = By.XPATH, './/fieldset/div/div/input'
    PASSWORD_LOGIN_FIELD = By.XPATH, './/div/div/input[@name="Пароль"]'
    LOGIN_BUTTON = By.XPATH, './/form/button[contains(text(),"Войти")]'
    PROFILE_BUTTON = By.XPATH, './/nav/ul/li/a[@href="/account/profile"]'
    PROFILE_ORDER = By.XPATH, './/ul/li/a/div/p[contains(text(),"#0377126")]'