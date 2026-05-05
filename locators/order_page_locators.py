from selenium.webdriver.common.by import By

class OrderPageLocators: #"Лента заказов"
    ORDER_BUTTON = By.CLASS_NAME, 'OrderHistory_link__1iNby'
    ORDER_INFO_POPUP = By.CLASS_NAME, 'Modal_list__2sHWc'
    BURGER_ORDERED_LIST = By.XPATH, './/a/div/p[@class="text text_type_digits-default"]'
    ORDERS_COUNT = By.XPATH, "//p[text()='Выполнено за все время:']""/following-sibling::p[contains(@class, 'OrderFeed_number')]"
    ORDERS_TODAY_COUNT = By.XPATH,"//p[text()='Выполнено за сегодня:']""/following-sibling::p[contains(@class, 'OrderFeed_number')]"
    ORDERS_IN_PROGRESS = By.XPATH, './/div/div/div[1]/ul[@class = "OrderFeed_orderListReady__1YFem OrderFeed_orderList__cBvyi"]/li'
    ORDER_PAGE_HEADER = By.CSS_SELECTOR, 'h1.text'
    ORDER_POPUP_WINDOW = By.CSS_SELECTOR, 'html body div#root div.App_App__aOmNj section.Modal_modal_opened__3ISw4.Modal_modal__P3_V5 div.Modal_modal__container__Wo2l_'
    ORDERS_IN_WORK_NUMBER = By.XPATH, './/div/div[1]/ul[2]/li[starts-with(text(), "0")]'

