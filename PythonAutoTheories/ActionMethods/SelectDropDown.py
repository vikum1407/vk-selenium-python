from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

browserName = "firefox"

if browserName == "chrome":
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
elif browserName == "firefox":
    driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
else:
    print("Please pass the current browser name")

driver.implicitly_wait(5)

driver.get("https://www.orangehrm.com/contact-sales/")
driver.maximize_window()

driver.find_element(By.XPATH, "//input[@id='Form_getForm_FullName']").send_keys("vikum")
driver.find_element(By.XPATH, "//input[@id='Form_getForm_Contact']").send_keys("91233484722")
driver.find_element(By.XPATH, "//input[@id='Form_getForm_Email']").send_keys("viku@gmail.com")

time.sleep(3)

# Dropdown common method
def dropdown_common(element, value):
    selct = Select(element)
    selct.select_by_visible_text(value)

def dropdown_list_common(elementList, value):
    for ele in elementList:
        if ele.text == value:
            ele.click()
            break

countrydrp = driver.find_element(By.XPATH, "//select[@id='Form_getForm_Country']")
# select = Select(countrydrp)
# select.select_by_visible_text("Sweden")

#dropdown using common method
# dropdown_common(countrydrp,"Sweden")
#
# noOfEmp = driver.find_element(By.XPATH, "//select[@id='Form_getForm_NoOfEmployees']")
# select = Select(noOfEmp)
# list = select.options
#
# for i in list:
#     print(i.text)
#     if i.text == '0 - 10':
#         i.click()
#         break

#dropdown using common method
#dropdown_common(noOfEmp, "0 - 10")

# without select method

countryList = driver.find_elements(By.XPATH, "//select[@id='Form_getForm_Country']/option")
for ele in countryList:
    if ele.text=="Sweden":
        ele.click()
        break

driver.find_element(By.XPATH, "//input[@id='Form_getForm_JobTitle']").send_keys("Mr.")
driver.find_element(By.XPATH, "//textarea[@id='Form_getForm_Comment']").send_keys("no commen at all for this man !!!")

