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

driver.get("https://demo.opencart.com/")
driver.maximize_window()

'''Move to Element'''

# lap_netbooks = driver.find_element(By.XPATH, "//a[normalize-space()='Laptops & Notebooks']")
# action_spiceClubBtn = ActionChains(driver)
# action_spiceClubBtn.move_to_element(lap_netbooks).perform()
#
# windowsIcon = driver.find_element(By.XPATH, "//a[normalize-space()='Windows (0)']")
# action_spiceClubBtn.move_to_element(windowsIcon).click().perform()

# components = driver.find_element(By.XPATH, "//a[normalize-space()='Components']")
# mouseHover = ActionChains(driver)
# mouseHover.move_to_element(components).perform()
#
# printer_icon = driver.find_element(By.XPATH, "//a[normalize-space()='Printers (0)']")
# mouseHover.move_to_element(printer_icon).click().perform()

def mouse_hoverMethod(element1, element2):
    mouseHover = ActionChains(driver)
    mouseHover.move_to_element(element1).perform()
    mouseHover.move_to_element(element2).click().perform()

components = driver.find_element(By.XPATH, "//a[normalize-space()='Components']")
printer_icon = driver.find_element(By.XPATH, "//a[normalize-space()='Printers (0)']")

mouse_hoverMethod(components, printer_icon)











