import pytest
from Pytest.Fixtures.test_fixtureWithParams import BaseTest
from PythonPOM.Conf.config import TestData
from PythonPOM.Pages.LoginPage import LoginPage

class Test_Login(BaseTest):

    def test_orangeHRM_link_visible(self):
        self.loginPage = LoginPage(self.driver)
        flag = self.loginPage.is_orangeHRM_link_exist()
        assert flag

    def test_login_page_title(self):
        self.loginPage = LoginPage(self.driver)
        title = self.loginPage.get_title(TestData.LOGIN_PAGE_TITLE)
        assert title == TestData.LOGIN_PAGE_TITLE

    def test_login(self):
        self.loginPage = LoginPage(self.driver)
        self.loginPage.do_login(TestData.USERNAME, TestData.PASSWORD)

