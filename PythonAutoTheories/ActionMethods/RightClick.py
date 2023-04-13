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

driver.get("http://swisnl.github.io/jQuery-contextMenu/demo.html")
driver.maximize_window()

rightClick = driver.find_element(By.XPATH, "//span[@class='context-menu-one btn btn-neutral']")
actionMoment = ActionChains(driver)
actionMoment.context_click(rightClick).perform()

allOptions = driver.find_elements(By.CSS_SELECTOR, '.context-menu-list > li >span')
for ele in allOptions:
    if ele.text == 'Delete':
        time.sleep(3)
        ele.click()

