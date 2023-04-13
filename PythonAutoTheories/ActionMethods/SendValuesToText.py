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

driver.get("https://opensource-demo.orangehrmlive.com/")
driver.maximize_window()

username = driver.find_element(By.XPATH, '//input[@placeholder="Username"]')
password = driver.find_element(By.XPATH, '//input[@placeholder="Password"]')
loginbtn = driver.find_element(By.XPATH, '//button[@type="submit"]')

mouseMethod = ActionChains(driver)
mouseMethod.send_keys_to_element(username).send_keys("admin").perform()
mouseMethod.send_keys_to_element(password).send_keys("admin123").perform()
mouseMethod.send_keys_to_element(loginbtn).click().perform()

