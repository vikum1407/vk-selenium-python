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

'''Approach 03'''
options = Options()
options.set_capability('acceptInsecureCerts', True)

if browserName == "chrome":
    driver = webdriver.Chrome(chrome_options=options)

driver.implicitly_wait(10)

driver.quit()


driver.get("https://am.axp.com/slate")