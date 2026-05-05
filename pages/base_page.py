from selenium.webdriver.support import expected_conditions
import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver import ActionChains


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.timeout = 60
        self.wait = WebDriverWait(self.driver, self.timeout)
        self.url = driver.current_url
    
    def go_to_url(self, url):
        self.driver.get(url)
    
    def find_element_with_wait (self, locator):
        self.wait.until (expected_conditions.visibility_of_element_located(locator))
        return self.driver.find_element(*locator)
    
    
    def find_element(self, locator):
        element = self.wait.until (expected_conditions.presence_of_element_located(locator))
        return element
    

    def find_elements(self, locator):
        element = self.wait.until (expected_conditions.presence_of_all_elements_located(locator))
        return element

    def dissapear_element (self, locator):
        element = self.wait.until_not(expected_conditions.visibility_of_element_located(locator))
        return element
    
    def return_element (self, locator):
        element = self.wait.until(expected_conditions.visibility_of_element_located(locator)).text()
        return element
    
    def find_elements_with_wait (self, locator):
        self.wait.until (expected_conditions.visibility_of_element_located(locator))
        return self.driver.find_elements(*locator)
    
    
    def click_to_element(self,some):
        self.wait.until(expected_conditions.element_to_be_clickable(some))
        element = self.driver.find_element(*some)
        self.driver.execute_script("arguments[0].click();", element)
        

    def send_keys_to_element_with_click(self,some,info):
        element = self.wait.until(expected_conditions.element_to_be_clickable(some))
        self.driver.execute_script("arguments[0].click();", element)
        element.send_keys(info)

    def scroll_into_view(self,locator):
        element = self.find_element_with_wait(locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        
    def click_element_after_scroll(self,locator):
        element = self.find_element_with_wait(locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        self.driver.execute_script("arguments[0].click();", element)


    def get_text_from_element(self,locator):
        return self.find_element_with_wait(locator).get_attribute('innerText')
    
        

    def drag_and_drop(self, locator_from, locator_to):
        action = ActionChains(self.driver)
        elem_from = self.find_element_with_wait(locator_from)
        elem_to = self.find_element_with_wait(locator_to)

        action.drag_and_drop(elem_from,elem_to).perform()

    def user_login(self, locator, info):
        self.send_keys_to_element_with_click(locator, info)

    def refresh_for_orders(self,locator):
        self.driver.refresh()
        self.scroll_into_view(locator)