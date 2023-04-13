from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import time
import pytest

@pytest.fixture(params=["chrome", "firefox"], scope='class')
def init_driver(request):  #'''through 'request' it's like a context, we can get the method name, param name, xml variable name, clz name'''
    if request.param == "chrome":
        web_driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    if request.param == "firefox":
        web_driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
    request.cls.driver = web_driver
    yield
    web_driver.quit()