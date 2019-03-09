import time
import pytest
from Pages.LoginPageUtils import LoginPage
from Pages.HomePage import HomePage
from Pages.CreateUser import CreateUser

@pytest.mark.usefixtures("test_set_up")
class TestLogin:

    def test_login(self):
        driver = self.driver
        lp = LoginPage(driver)
        lp.enter_user_name()
        lp.enter_password()
        lp.click_on_login_btn()

    def test_create_user(self):
        driver = self.driver
        us = CreateUser(driver)
        us.click_on_users_btn()

    def test_logout(self):
        driver = self.driver
        time.sleep(3)
        lo=HomePage(driver)
        lo.click_on_logout_btn()
        time.sleep(2)