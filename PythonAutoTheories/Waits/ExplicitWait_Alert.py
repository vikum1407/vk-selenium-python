from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as ec
import time

browserName = "chrome"

options = webdriver.ChromeOptions()
options.add_argument("--incognito")
# driver = webdriver.Chrome(options=options) #This is applying for without webdrivermanager

if browserName == "chrome":
    driver = webdriver.Chrome(options=options)
elif browserName == "firefox":
    driver = webdriver.Firefox(options=options)
else:
    print("Please pass the current browser name")

driver.implicitly_wait(5)

driver.get("https://mail.rediff.com/cgi -bin/login.cgi") #this url is not working but think there is an alert to get
# username and password with submit button
driver.maximize_window()

driver.find_element(By.NAME, 'proceed').click()

wait = WebDriverWait(driver, 10)
alert = wait.until(ec.alert_is_present()) # this method automatically switch to the alert
print(alert.text) #then get the text of the alert
alert.accept()
driver.close()