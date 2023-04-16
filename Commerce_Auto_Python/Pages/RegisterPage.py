from selenium.webdriver.common.by import By

from PythonPOM.Conf.config import TestData
from PythonPOM.Pages.BasePage import BasePage


class RegisterPage(BasePage):

    HOMEPAGE_REGISTER_BUTTON = "//a[@class='ico-register']"
    REGISTERPAGE_TITLE = (By.XPATH, "//h1[normalize-space()='Register']")
    PERSONAL_DETAILS = (By.XPATH, "//strong[normalize-space()='Your Personal Details']")
    MALE_GENDER = (By.XPATH, "//input[@id='gender-male']")
    FEMALE_GENDER = (By.XPATH, "//input[@id='gender-female']")
    FIRST_NAME = (By.XPATH, "//input[@id='FirstName']")
    LAST_NAME = (By.XPATH, "//input[@id='LastName']")
    DATE = (By.XPATH, "//select[@name='DateOfBirthDay']")
    MONTH = (By.XPATH, "//select[@name='DateOfBirthMonth']")
    YEAR = (By.XPATH, "//select[@name='DateOfBirthYear']")
    EMAIL = (By.XPATH, "//input[@id='Email']")
    COMPANY_DETAILS = (By.XPATH, "//strong[normalize-space()='Company Details']")
    COMPANY_NAME = (By.XPATH, "//input[@id='Company']")
    PASSWORD = (By.XPATH, "//input[@id='Password']")
    CONFIRM_PASSWORD = (By.XPATH, "//input[@id='ConfirmPassword']")
    REGISTER_BUTTON = (By.XPATH, "//button[@id='register-button']")

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(TestData.BASE_URL)

    def do_click_register(self):
        self.do_click(self.HOMEPAGE_REGISTER_BUTTON)

    def register_page_title(self, title):
        self.get_title(self.get_title(title))

    def is_check_regidter_header(self, title):
        return self.is_vidibles(self.REGISTERPAGE_TITLE, title)

    def is_check_personalDetails(self, personalDetails):
        return self.is_vidibles(self.PERSONAL_DETAILS, personalDetails)

    def do_click_male(self, male):
        self.do_click(self.MALE_GENDER, male)

    def send_firstname(self, firstname):
        self.do_send_keys(self.FIRST_NAME, firstname)

    def send_lastname(self, lastname):
        self.do_send_keys(self.LAST_NAME, lastname)

    def date_click(self, date, month, year):
        self.do_date_dropdown(self.DATE, date)
        self.do_date_dropdown(self.MONTH, month)
        self.do_date_dropdown(self.YEAR, year)

    def send_email(self, email):
        self.do_send_keys(self.EMAIL, email)

    def send_company(self, company):
        self.do_send_keys(self.COMPANY_NAME, company)

    def send_password(self, password):
        self.do_send_keys(self.PASSWORD, password)

    def send_confirm_password(self, confimpassword):
        self.do_send_keys(self.CONFIRM_PASSWORD, confimpassword)

    def click_register_button(self):
        self.do_click(self.REGISTER_BUTTON)
