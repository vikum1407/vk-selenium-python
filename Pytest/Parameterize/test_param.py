from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import time
import pytest

@pytest.mark.usefixtures("init_driver")
class BaseTest:
    pass

class TestHubSpot(BaseTest):

    @pytest.mark.parametrize(
                                "username, password",
                            [
                                ("admin123@gmail.com", "admin123"),
                                ("viku345@gmail.com", "vikum456")
                            ]

                             )

    def test_login(self, username, password):
        """
        This method is writing to log the application

        :param username:
        :param passowrd:
        :return:
        """
        self.driver.get("https://app.hubspot.com/login")
        self.driver.find_element(By.ID, 'username').send_keys(username)
        time.sleep(1)
        self.driver.find_element(By.ID, 'password').send_keys(password)
        time.sleep(4)

