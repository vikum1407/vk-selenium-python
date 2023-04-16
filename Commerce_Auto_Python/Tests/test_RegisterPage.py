from Commerce_Auto_Python.Conf.config import TestData
from Commerce_Auto_Python.Pages.RegisterPage import RegisterPage
from Commerce_Auto_Python.Tests.test_BaseTest import TestBase


class Test_Register(TestBase):

    def test_register_button(self):
        self.registerPage = RegisterPage(self.driver)
        self.do_click_register()

    def test_page_title(self):
        self.registerPage = RegisterPage(self.driver)
        title = self.is_check_regidter_header(TestData.REGISTERPAGE_TITLE)
        assert title

    def test_register_header(self):
        self.registerPage = RegisterPage(self.driver)
        personal = self.is_check_personalDetails()
        assert personal

    def test_register(self):
        self.registerPage = RegisterPage(self.driver)
        self.registerPage.do_click_male()
        self.registerPage.send_firstname(TestData.FIRSTNAME)
        self.registerPage.send_lastname(TestData.LASTNAME)
        self.registerPage.date_click(TestData.DATE, TestData.MONTH, TestData.YEAR)
        self.registerPage.send_email(TestData.EMAIL)
        self.registerPage.send_company(TestData.COMPANY)
        self.registerPage.send_password(TestData.PASSWORD)
        self.registerPage.send_confirm_password(TestData.CONFIRMPASSWORD)
        self.registerPage.click_register_button()
