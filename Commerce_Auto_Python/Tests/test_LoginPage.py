import pytest

from Commerce_Auto_Python.Conf.config import TestData
from Pytest.Fixtures.test_fixtureWithParams import BaseTest
from Commerce_Auto_Python.Pages import LoginPage

class Test_Login(BaseTest):

    def test_login_button(self):
        self.loginPage = LoginPage(self.driver)
        self.loginPage.click_homepage_login_button()

    def test_login_title(self):
        self.loginPage = LoginPage(self.driver)
        title = self.loginPage.get_title(TestData.LOGIN_PAGE_TITLE)
        assert title

    def test_login_page_header(self):
        self.loginPage = LoginPage(self.driver)
        header1 = self.loginPage.is_login_page_header(TestData.LOGIN_PAGE_HEADER1)
        assert header1

    def test_second_title_header(self):
        self.loginPage = LoginPage(self.driver)
        header2 = self.loginPage.is_login_lage_second_header(TestData.LOGIN_PAGE_HEADER2)
        assert header2

    def test_register_button(self):
        self.loginPage = LoginPage(self.driver)
        registerbtn = self.loginPage.is_register_button()
        assert registerbtn

    def test_forgetbtn(self):
        self.loginPage = LoginPage(self.driver)
        forgotbutton = self.loginPage.is_forgotbutn()
        assert forgotbutton

    def test_rememberme_button(self):
        self.loginPage = LoginPage(self.driver)
        remember = self.loginPage.is_remember_me()

    def test_login(self):
        self.loginPage = LoginPage(self.driver)
        self.loginPage.login_testboxes(TestData.USERNAME, TestData.PASSWORD)


