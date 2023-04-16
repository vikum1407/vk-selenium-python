from selenium.webdriver.common.by import By

from PythonPOM.Conf.config import TestData
from PythonPOM.Pages.BasePage import BasePage


class LoginPage(BasePage):

    HOMEPAGE_LOGIN_ICON = (By.XPATH, "//a[@class='ico-login']")
    LOGIN_PAGE_HEADER = (By.XPATH, "//strong[normalize-space()='New Customer']")
    LOGIN_PAGE_SECOND_TITLE = (By.XPATH, "//strong[normalize-space()='Returning Customer']")
    EMAIL = (By.XPATH, "//input[@id='Email']")
    PASSWORD = (By.XPATH, "//input[@id='Password']")
    LOGIN_BUTTON = (By.XPATH, "//button[normalize-space()='Log in']")
    LOGINPAGE_REGISTER_BUTTON = (By, "//button[normalize-space()='Register']")
    FORGET_BUTTON = (By.XPATH, "//a[normalize-space()='Forgot password?']")
    LOGINPAGE_REMEMBER_ME = (By.XPATH, "//label[@for='RememberMe']")


    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(TestData.BASE_URL)


    def click_homepage_login_button(self):
        self.do_click(self.HOMEPAGE_LOGIN_ICON)

    def get_loginpage_title(self, title):
        return self.get_title(title)

    def is_login_page_header(self, header1):
        return self.is_vidibles(self.LOGIN_PAGE_HEADER, header1)

    def is_login_lage_second_header(self, header2):
        return self.is_vidibles(self.LOGIN_PAGE_SECOND_TITLE, header2)

    def is_register_button(self):
        return self.is_vidibles(self.LOGINPAGE_REGISTER_BUTTON)

    def is_forgotbutn(self):
        return self.is_vidibles(self.FORGET_BUTTON)

    def is_remember_me(self):
        return self.is_vidibles(self.LOGINPAGE_REMEMBER_ME)

    def login_testboxes(self, email, password):
        self.do_send_keys(self.EMAIL, email)
        self.do_send_keys(self.PASSWORD, password)
        self.do_click(self.LOGIN_BUTTON)



