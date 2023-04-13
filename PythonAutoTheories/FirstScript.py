from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

ser_obj = Service("D:\\Vikum\\SDET\\Python\\Python-Selenium\\chromedriver_win32\\chromedriver.exe")
driver = webdriver.Chrome(service=ser_obj)
driver.implicitly_wait(5)
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://opensource-demo.orangehrmlive.com/")


driver.find_element(By.XPATH, '//input[@placeholder="Username"]').send_keys("admin")
driver.find_element(By.XPATH, '//input[@placeholder="Password"]').send_keys("admin123")
driver.implicitly_wait(5)
driver.find_element(By.XPATH, '//button[@type="submit"]').click()

actualTitle = driver.title
exp_Title="OrangeHRM"

if actualTitle==exp_Title:
    print("Login Test Pass!!!")
else:
    print("Fail !!!")

driver.quit()