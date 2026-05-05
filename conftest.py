import pytest
from selenium import webdriver
import data
from selenium.webdriver.firefox.options import Options


@pytest.fixture(params=["chrome", "firefox"])
def driver(request):
    if request.param == 'firefox':
        options = webdriver.FirefoxOptions()

        # Отключаем все виды кэша
        options.set_preference('browser.cache.disk.enable', False)
        options.set_preference('browser.cache.memory.enable', False)
        options.set_preference('browser.cache.offline.enable', False)
        options.set_preference('network.http.use-cache', False)

        # Настройки JavaScript
        options.set_preference('javascript.enabled', True)
        options.set_preference('dom.max_script_run_time', 30)
        options.set_preference('dom.min_background_timeout_value', 100)

        # Настройки сети
        options.set_preference('network.http.connection-timeout', 30)
        options.set_preference('network.http.response.timeout', 60)
        options.set_preference('network.dns.disablePrefetch', True)
        options.set_preference('network.prefetch-next', False)

        # Режим инкогнито
        options.add_argument('-private')
        options.add_argument('--width=1920')
        options.add_argument('--height=1080')
        

        # Дополнительные оптимизации
        options.set_preference('toolkit.cosmeticAnimations.enabled', False)  # Отключить анимации
        driver = webdriver.Firefox(options=options)

    elif request.param == 'chrome':
        options = webdriver.ChromeOptions()

        # Отключаем кэш и оптимизируем для тестов
        options.add_argument('--disable-cache')
        options.add_argument('--disk-cache-size=0')
        options.add_argument('--media-cache-size=0')

        # Режим инкогнито и общие оптимизации
        options.add_argument('--incognito')
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')
        options.add_argument('--disable-gpu')
        options.add_argument('--window-size=1920,1080')

        # Отключение уведомлений и лишних функций
        prefs = {
            'profile.default_content_setting_values.notifications': 2,
            'download.prompt_for_download': False,
            'download.directory_upgrade': True,
        }
        options.add_experimental_option('prefs', prefs)

        driver = webdriver.Chrome(options=options)

    # Устанавливаем общие настройки для всех браузеров
    driver.implicitly_wait(10)  # Неявное ожидание элементов
    driver.set_page_load_timeout(30)  # Таймаут загрузки страницы

    data.DRIVER_NAME = request.param  # Исправлена опечатка: DRIVER → DRIVER

    yield driver
    driver.quit()
