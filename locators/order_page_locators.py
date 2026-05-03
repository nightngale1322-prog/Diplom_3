from selenium.webdriver.common.by import By

class OrderPageLocators: #"Лента заказов"
    ORDER_BUTTON = By.CLASS_NAME, 'OrderHistory_link__1iNby'
    ORDER_INFO_POPUP = By.CLASS_NAME, 'Modal_list__2sHWc'
    BURGER_ORDERED_LIST = By.XPATH, './/a/div/p[@class="text text_type_digits-default"]'
    ORDERS_COUNT = By.XPATH, './/div/div/div/p[starts-with(text(), "377")]'
    ORDERS_TODAY_COUNT = By.XPATH, './/div/div/div/p[@class = "OrderFeed_number__2MbrQ text text_type_digits-large"]'
    ORDERS_IN_PROGRESS = By.XPATH, './/div/div/ul/li[contains(text(), "Все текущие заказы готовы!")]'
    ORDER_PAGE_HEADER = By.CSS_SELECTOR, 'h1.text'
    ORDER_POPUP_WINDOW = By.CSS_SELECTOR, 'html body div#root div.App_App__aOmNj section.Modal_modal_opened__3ISw4.Modal_modal__P3_V5 div.Modal_modal__container__Wo2l_'
    ORDER_FROM_HISTORY_NUMBER = By.XPATH, './/div/div/ul[@class ="OrderFeed_orderListReady__1YFem OrderFeed_orderList__cBvyi"]/li[starts-with(text(), "3")]'