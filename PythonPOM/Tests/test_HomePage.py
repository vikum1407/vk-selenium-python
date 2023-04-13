from Pytest.Fixtures.test_fixtureWithParams import BaseTest
from PythonPOM.Conf.config import TestData
from PythonPOM.Pages.LoginPage import LoginPage


class Test_Home(BaseTest):

    def test_homepage_title(self):
        #''' to validate the home page, you need to login first. So need to call to the 'login' method'''
        self.loginPage = LoginPage(self.driver)
        homePage = self.loginPage.do_login(TestData.USERNAME, TestData.PASSWORD)
        home_page_title = homePage.get_home_page_title(TestData.HOME_PAGE_TITLE)
        assert home_page_title == TestData.HOME_PAGE_TITLE

    def test_home_page_header(self):
        self.loginPage = LoginPage(self.driver)
        homePage = self.loginPage.do_login(TestData.USERNAME, TestData.PASSWORD)
        home_page_header = homePage.get_header_value()
        assert home_page_header == TestData.HOME_PAGE_HEADER

    def test_account_name(self):
        self.loginPage = LoginPage(self.driver)
        homePage = self.loginPage.do_login(TestData.USERNAME, TestData.PASSWORD)
        account_name = homePage.get_myAction_value()
        assert account_name == TestData.ACCOUNT_NAME

    def test_quick_launch_value(self):
        self.loginPage = LoginPage(self.driver)
        homePage = self.loginPage.do_login(TestData.USERNAME, TestData.PASSWORD)
        quick_lauch = homePage.get_quick_launch_value()
        assert quick_lauch == TestData.QUICK_LAUNCH_VALUE
