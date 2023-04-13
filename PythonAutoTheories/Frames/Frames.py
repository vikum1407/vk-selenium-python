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

driver.get("http://www.londonfreelance.org/courses/frames/index.html")
driver.maximize_window()

'''Approach 01 - direct get it as a frame'''
driver.switch_to.frame(2) # this is the number of frame index(count frame from 0 starting)
# driver.switch_to.frame('main') # 'main' mean an attribute. this also working

''' Approach 02 - get it as an element then load it to the frame'''
frame_ele = driver.find_element(By.NAME, 'main')
driver.switch_to.frame(frame_ele)

headerValue = driver.find_element(By.CSS_SELECTOR, 'body > h2').text
print(headerValue)

''' when you went inside to the frame and if you need come back to the page, so you can use followings'''
driver.switch_to.default_content()

'''If you went two frames inside, and how to come back to the page'''
driver.switch_to.parent_frame()