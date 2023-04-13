from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import time
import pytest

def test_facebook():
    driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
    driver.implicitly_wait(10)
    driver.get("https://www.facebook.com")
    print(driver.title)
    assert driver.title == "Facebook - log in or sign up"
    driver.quit()

def test_gogle():
    driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
    driver.implicitly_wait(10)
    driver.get("https://www.google.com")
    print(driver.title)
    assert driver.title == "Google"
    driver.quit()

def test_classic():
    driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
    driver.implicitly_wait(10)
    driver.get("https://classic.crmpro.com/")
    print(driver.title)
    assert driver.title == "Free CRM - CRM software for customer relationship management, sales, and support."
    driver.quit()

def test_orangehrm():
    driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
    driver.implicitly_wait(10)
    driver.get("https://www.orangehrm.com/")
    print(driver.title)
    assert driver.title == "OrangeHRM HR Software | Free & Open Source HR Software | HRMS | HRIS | OrangeHRM"
    driver.quit()

def test_amazon():
    driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
    driver.implicitly_wait(10)
    driver.get("https://www.amazon.in/")
    print(driver.title)
    assert driver.title == "Online Shopping site in India: Shop Online for Mobiles, Books, Watches, Shoes and More - Amazon.in"
    driver.quit()