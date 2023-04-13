from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import time
import pytest

driver = None

@pytest.fixture(scope='module')
def init_driver():
    global driver
    print("--------------- setup -----------------------")
    driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
    driver.implicitly_wait(10)
    #driver.delete_cookie()
    driver.get("https://www.google.com")


    yield #this is using for execute after running all the test method
    print("--------------- teardown -----------------------")
    driver.quit()

''' Approach 01 '''
# def test_google_title(init_driver):
#     assert driver.title == "Google"
#
# def test_google_url(init_driver):
#     assert driver.current_url == "https://www.google.com1/"

@pytest.mark.usefixtures("init_driver")
def test_google_title():
    assert driver.title == "Google"

@pytest.mark.usefixtures("init_driver")
def test_google_url():
    assert driver.current_url == "https://www.google.com/"