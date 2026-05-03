from selenium.webdriver.common.by import By

class MainPageLocators: # все,что находится на "Конструктор"е
    OVERLAY = By.XPATH, './/div[@class="Modal_modal_overlay__x2ZCr"]' 
    CONSTRUCTION_BUTTON = By.XPATH, './/li/a/p[contains(text(), "Конструктор")]'
    ORDER_PAGE_BUTTON = By.CLASS_NAME, 'AppHeader_header__link__3D_hX'
    INGREDIENT_BUTTON_1 = By.XPATH, './/a/img[@alt="Флюоресцентная булка R2-D3"]'
    INGREDIENT_BUTTON_2 = By.XPATH, './/a/img[@alt="Краторная булка N-200i"]' 
    INGREDIENT_POPUP = By.XPATH, './/div/div/h2[contains(text(),"Детали ингредиента")]'
    POPUP_CLOSE_BUTTON = By.CSS_SELECTOR, '.Modal_modal_opened__3ISw4'
    INGREDIENT_COUNTER = By.XPATH, './/div/p[contains(text(),"2")]'
    ORDER_PROGRESS_BUTTON = By.XPATH, './/section/div/button[contains(text(),"Оформить заказ")]'
    ORDER_POPUP_IDENTIFICATOR = By.XPATH, './/div/div/p[contains(text(),"идентификатор заказа")]'
    ORDER_POPUP_ORDER_NUMBER = By.XPATH, './/section/div/div/h2'
    ORDER_BUTTON_NO_LOGIN = By.XPATH, './/div/button[contains(text(),"Войти в аккаунт")]'
    ORDER_INGREDIENT_FIELD = By.XPATH, './/div/span/span[contains(text(),"Перетяните булочку сюда (верх)")]'