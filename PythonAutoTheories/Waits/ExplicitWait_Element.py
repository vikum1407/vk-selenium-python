'''

    Explicit Wait( Webdriver wait ) :-

            This wait basically apply for particular targeted element on the web page.




'''

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec #here expected_conditions too big so tell to use ec instead of that
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.chrome.service import Service as ChromeService

browserName = "firefox"

if browserName == "chrome":
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
elif browserName == "firefox":
    driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
else:
    print("Please pass the current browser name")

driver.get("https://app.hubspot.com/login")
driver.maximize_window()

'''Explicit wait initializing'''
wait = WebDriverWait(driver, 10)

'''If I need to get the page title - here also have to use the explicit wait'''
# titleWait = wait.until(ec.title_contains('HubSpot')) # using ['title_contains' method]
titleWait = wait.until(ec.title_is('HubSpot Login'))
print(driver.title)

'''wait added to the element '''
usernameBox = wait.until(ec.presence_of_element_located((By.ID, 'username')))
usernameBox.send_keys("test@gmail.com")

#after adding wait for the username, no need to apply for the password field because page is already loaded

driver.quit()


