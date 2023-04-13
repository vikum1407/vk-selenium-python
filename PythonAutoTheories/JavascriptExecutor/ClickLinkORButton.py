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

''' click web element (button) '''
best_sellers = driver.find_element(By.XPATH, "//a[@href='/gp/bestsellers/?ref_=nav_cs_bestsellers']")
driver.execute_script("arguments[0].click();", best_sellers)

time.sleep(5)
'''border the element from a color''' #this will help you to put a bug for an specific element
driver.execute_script("arguments[0].style.border = '3px solid red'", best_sellers)

''' get the page title '''
page_title = driver.execute_script("return document.title;")
print(page_title)

time.sleep(3)
'''refresh the page'''
refresh_page = driver.execute_script("history.go[0];")

time.sleep(5)
'''generate alert on the page'''
alert_msg = driver.execute_script("alert('Hello Vikum!!!')")