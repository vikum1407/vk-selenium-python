from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import time

options = webdriver.ChromeOptions()
options.add_argument("--headless")
driver = webdriver.Chrome(options=options)

driver.implicitly_wait(5)

driver.get("https://www.reddit.com")


time.sleep(2)

''' To Take full screenshot make sure you have to run the test in headless mode'''

S = lambda X: driver.execute_script('return document.body.parentNode.scroll'+X)
driver.set_window_size(S('Width'), S('Height'))
driver.find_element(By.TAG_NAME, 'body').screenshot('fullScreen_reddit.png')

print("Successfully Completed !!!!")

driver.quit()