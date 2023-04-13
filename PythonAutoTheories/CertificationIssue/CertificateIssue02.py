from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.firefox.options import Options
from selenium.webdriver import ActionChains, DesiredCapabilities
import time

browserName = "firefox"

'''Approach 02'''
#this is for chrome
desired_capabilities = DesiredCapabilities().CHROME.copy()
desired_capabilities['acceptInsecureCerts'] = True

#this is for firfox
desired_capabilities = DesiredCapabilities().FIREFOX.copy()
desired_capabilities['acceptInsecureCerts'] = True

if browserName == "chrome":
    driver = webdriver.Chrome(desired_capabilities=desired_capabilities)
elif browserName == "firefox":
    driver = webdriver.Firefox(desired_capabilities=desired_capabilities)
else:
    print("Please pass the current browser name")

driver.implicitly_wait(10)

driver.quit()


driver.get("https://am.axp.com/slate")