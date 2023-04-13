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

browserName = "firefox"

if browserName == "chrome":
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
elif browserName == "firefox":
    driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
else:
    print("Please pass the current browser name")

driver.implicitly_wait(5)

driver.get("https://www.amazon.in")
driver.maximize_window()

time.sleep(3)
'''scrolling to the bottom of the page'''
driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")

time.sleep(5)
'''scrol to an element'''
best_seller = driver.find_element(By.XPATH, "//span[normalize-space()='Best Sellers in Home & Kitchen']")
driver.execute_script("arguments[0].scrollIntoView(true);", best_seller)