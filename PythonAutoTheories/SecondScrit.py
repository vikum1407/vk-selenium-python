from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

server_obj = Service("D:\\Vikum\\SDET\\Python\\Python-Selenium\\chromedriver_win32\\chromedriver.exe")
driver = webdriver.Chrome(service=server_obj)
driver.implicitly_wait(5000)
driver.get("https://opensource-demo.orangehrmlive.com/")
driver.implicitly_wait(5000)
driver.maximize_window()


driver.implicitly_wait(10)
