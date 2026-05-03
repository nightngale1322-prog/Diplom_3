import pytest
from selenium import webdriver
import data


@pytest.fixture(params=["chrome", "firefox"])
def driver(request):
        if request.param == 'firefox':
            driver = webdriver.Firefox()
            data.DRIVER_NAME = 'firefox'
            yield driver
            driver.quit()
        else:
            driver = webdriver.Chrome()
            data.DRIVER_NAME = 'chrome'
            yield driver
            driver.quit()
        
