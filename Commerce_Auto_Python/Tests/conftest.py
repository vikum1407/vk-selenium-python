from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
import pytest

@pytest.fixture(params=["firefox"], scope="class")
def init_driver(request):
    if request.param == 'firefox':
        web_driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
    request.cls.driver = web_driver
    yield
    web_driver.quit()