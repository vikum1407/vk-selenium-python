'''

    They are two types of wait:-

        1. Static Wait
            - time.sleep(5) this mean all will wait only 5s

        2. Dynamic Wait
            - This is on a particular element and tell to wait until visible or something happening.
            eg: allocate 10s to check the element, element visible in 5s then continue the rest of the test with
                canceling the rest 5s.

        There are mainly two dynamic waits
            01. Implicitly wait
            02. Explicitly wait(webdriver wait)

        Implicit Wait Conditions:-
            * This is a dynamic wait
            * Act as global wait
            * Apply for both 'find_element' and 'find_elements'
            * Only apply for all the web elements not the none web elements
                - not the url loading, alerts, print(driver.title) ...etc (apply for explicit wait).

            Common cons in Implicit Wait:-
                * Due to the global wait, script will wait the given amount of time to each web element load.
                  this can overcome with overriding the imp wait. but it's not good.
                * Can't manage the url loadings, alerts, web titles getting ...etc



'''

from selenium import webdriver
from selenium.webdriver.common.by import By

browserName = "firefox"

options = webdriver.FirefoxOptions()
options.add_argument("--headless")

if browserName == "chrome":
    driver = webdriver.Chrome(options=options)
elif browserName == "firefox":
    driver = webdriver.Firefox(options=options)
else:
    print("Please pass the current browser name")

driver.implicitly_wait(10)

driver.get("https://orangehrm-demo")
driver.maximize_window()

driver.find_element(By.ID, "username").send_keys("admin")

driver.implicitly_wait(5)  #this is called implicit wait overriding
driver.find_element(By.ID, "password").send_keys("admin123")

driver.implicitly_wait(0) #nullify of implicit wait
driver.find_element(By.ID, "submit").click()