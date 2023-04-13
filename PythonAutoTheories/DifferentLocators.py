import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

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
driver.find_element(By.XPATH, '//input[@placeholder="Username"]').send_keys("admin")
driver.find_element(By.XPATH, '//input[@placeholder="Password"]').send_keys("admin123")
driver.find_element(By.XPATH, '//button[@type="submit"]').click();

print(driver.title)


print("Successful logged !!!")

driver.find_element(By.XPATH, '//li[1]//a[1]//span[1]').click();
sys_users_username = driver.find_element(By.XPATH, '(//input[@class="oxd-input oxd-input--active"])[2]')
sys_users_role = driver.find_element(By.XPATH, '(//div)[37]')
sys_users_name = driver.find_element(By.XPATH, '//input[@placeholder="Type for hints..."]')

sys_users_username.send_keys('vikum')
sys_users_role.send_keys('Admin')
sys_users_name.send_keys('viku')
