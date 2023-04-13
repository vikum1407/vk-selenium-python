from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import time

browserName = "firefox"

if browserName == "chrome":
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
elif browserName == "firefox":
    driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
else:
    print("Please pass the current browser name")

driver.implicitly_wait(5)

driver.get("https://the-internet.herokuapp.com/javascript_alerts")
driver.maximize_window()

''' Alert Accept Method'''
driver.find_element(By.XPATH, "//button[@onclick='jsAlert()']").click()

alert = driver.switch_to.alert
print(alert.text)
alert.accept()

time.sleep(5)

''' Alert Dismiss Method '''

driver.find_element(By.XPATH, "//button[@onclick='jsConfirm()']").click()
cancelAlert = driver.switch_to.alert
cancelAlert.dismiss()

time.sleep(5)

''' Alert, pass text to the alert text box '''

driver.find_element(By.XPATH, "//button[@onclick='jsPrompt()']").click()
textAlert = driver.switch_to.alert
textAlert.send_keys("I'M VIKUM!!!")
driver.switch_to.alert.accept()
