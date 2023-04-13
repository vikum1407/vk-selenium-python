from selenium.webdriver.common.by import By

from PythonPOM.Pages.BasePage import BasePage


class HomePage(BasePage):

    HEADER = (By.XPATH, "//h6[@class='oxd-text oxd-text--h6 oxd-topbar-header-breadcrumb-module']")
    ACCOUNT_NAME = (By.XPATH, "//p[@class='oxd-userdropdown-name']")
    TIME_WORK = (By.XPATH, "//p[normalize-space()='Time at Work']")
    MY_ACTIONS = (By.XPATH, "//p[normalize-space()='My Actions']")
    QUICK_LAUNCH = (By.XPATH, "//p[normalize-space()='Quick Launch']")
    ADMIN_PANEL_BUTTON = (By.XPATH, "//a[normalize-space()='']")

    def __init__(self, driver):
        super().__init__(driver)

    """Page Actions"""

    def get_home_page_title(self, title):
        return self.get_title(title)

    def is_Dashboard_icon_visile(self):
        return self.is_vidibles(self.TIME_WORK)

    def get_header_value(self):
        if self.is_vidibles(self.HEADER):
            return self.get_element_text(self.HEADER)

    def get_myAction_value(self):
        if self.is_vidibles(self.MY_ACTIONS):
            return self.get_element_text(self.MY_ACTIONS)

    def get_quick_launch_value(self):
        if self.is_vidibles(self.QUICK_LAUNCH):
            return self.get_element_text(self.QUICK_LAUNCH)