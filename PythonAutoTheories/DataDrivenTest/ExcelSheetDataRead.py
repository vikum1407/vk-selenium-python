import xlrd
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

driver.get("https://opensource-demo.orangehrmlive.com/")

username = driver.find_elements(By.ID, 'username')
password = driver.find_elements(By.ID, 'password')


workbook = xlrd.open_workbook("DataFile.xlsx")
sheet = workbook.sheet_by_name("Login")

#Get the total number of rows
rowCount = sheet.nrows
colCount = sheet.ncols

print(colCount)
print(rowCount)

#read data from excel sheet
for courr_row in range(1,rowCount):
    username = sheet.cell_value(courr_row, 0)
    password = sheet.cell_value(courr_row, 1)

#print(username, " ", password)

#fill the data to the web UI

    username.send_keys(username)
    password.send_keys(password)


    time.sleep(4000)