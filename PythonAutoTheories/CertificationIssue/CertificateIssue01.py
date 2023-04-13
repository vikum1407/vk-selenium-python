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

'''Approach 01'''
#this is for chrome
options = Options()
options.add_argument('--allow--running-insecure-content')
options.add_argument('--ignore--certificate-errors')

#this is for firfox
profile = webdriver.FirefoxProfile()
profile.accept_untrusted_certs = True

if browserName == "chrome":
    driver = webdriver.Chrome(options=options)
elif browserName == "firefox":
    driver = webdriver.Firefox(firefox_profile=profile)
else:
    print("Please pass the current browser name")

driver.implicitly_wait(10)



driver.get("https://am.axp.com/slate")

driver.quit()