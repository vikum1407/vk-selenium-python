from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import time
import pytest

@pytest.fixture(scope='class')
def init_chrome_driver(request):
    chrome_driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    request.cls.driver = chrome_driver
    yield
    chrome_driver.quit()

@pytest.fixture(scope='class')
def init_firefox_driver(request):
    firefox_driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
    request.cls.driver = firefox_driver
    yield
    firefox_driver.quit()

'''For Chrome'''

@pytest.mark.usefixtures("init_chrome_driver")
class Base_Chrome_test:
    pass

class Test_Google_chrome(Base_Chrome_test):

    def test_google_title_chrome(self):
        self.driver.get("https://www.google.com")
        assert self.driver.title == "Google"

'''For FireFox'''

@pytest.mark.usefixtures("init_firefox_driver")
class Base_Firefox_test:
    pass


class Test_Google_firefox(Base_Firefox_test):

    def test_google_title_firefox(self):
        self.driver.get("https://www.google.com")
        assert self.driver.title == "Google"