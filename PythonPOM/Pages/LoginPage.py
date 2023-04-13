from selenium.webdriver.common.by import By

from PythonPOM.Conf.config import TestData
from PythonPOM.Pages.BasePage import BasePage
from PythonPOM.Pages.HomePage import HomePage


class LoginPage(BasePage):

    ''' By locators - OR'''
    USERNAME = (By.XPATH, "//input[@placeholder='Username']")
    PASSWORD = (By.XPATH, "//input[@placeholder='Password']")
    LOGIN_BUTTON = (By.XPATH, "//button[@type='submit']")
    ORNAGEHRM_LINK = (By.XPATH, "//a[normalize-space()='OrangeHRM, Inc']")

    ''' constructor of the page class'''
    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(TestData.BASE_URL)

    '''Page Actions'''
    def get_login_page_title(self, title):
        return self.get_title(title)

    def is_orangeHRM_link_exist(self):
        return self.is_vidibles(self.ORNAGEHRM_LINK)

    def do_login(self, username, password):
        self.do_send_keys(self.USERNAME, username)
        self.do_send_keys(self.PASSWORD, password)
        self.do_click(self.LOGIN_BUTTON)

        return HomePage(self.driver)


