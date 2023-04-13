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

wait = WebDriverWait(driver, 10)

signup_link = wait.until(ec.element_to_be_clickable((By.XPATH, "//i18n-string[normalize-space()='Sign up']")))
print(signup_link.text)
signup_link.click()

firstName = wait.until(ec.visibility_of_element_located((By.XPATH, "//input[@id='UIFormControl-2']")))
firstName.send_keys("vikum")

#this is u can apply for multiple elements as well
# elementList = wait.until(ec.presence_of_all_elements_located(("<pass the list of element>")))
# frame = wait.until(ec.frame_to_be_available_and_switch_to_it(("<frame id>")))

driver.quit()