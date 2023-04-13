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

driver.get("https://jqueryui.com/resources/demos/droppable/default.html")
driver.maximize_window()

binicon = driver.find_element(By.ID, '#droppable')
drag = driver.find_element(By.ID, '#draggable')

#This is a way of using single method for drag and drop
dragAction = ActionChains(driver)
dragAction.drag_and_drop(binicon,drag).perform()

#Without using drag and drop method, how we can do

dragAction.click_and_hold(drag).move_to_element(binicon).release().perform()