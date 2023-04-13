from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
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
driver.find_element(By.XPATH, '//input[@placeholder="Username"]').send_keys("admin")
driver.find_element(By.XPATH, '//input[@placeholder="Password"]').send_keys("admin123")
driver.find_element(By.XPATH, '//button[@type="submit"]').click();

time.sleep(4)
print(driver.title)

print("Successful logged !!!")

driver.quit()


