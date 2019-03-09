from Utils.Constants import *
import time
import pytest
from selenium import webdriver
from Pages.LoginPageUtils import LoginPage
from Pages.HomePage import HomePage

class TestLogin:
    @pytest.fixture(scope='class')
    def test_launch_browser(self):
        global driver
        driver=webdriver.Chrome(executable_path="C:/Users/ADMIN/PycharmProjects/12Th_Class_3_3_2018_AutomationFramework/Drivers/chromedriver.exe")
        driver.maximize_window()
        driver.get(URL)
        driver.implicitly_wait(30)
        yield
        driver.quit()


    def test_login(self,test_launch_browser):
        lp = LoginPage(driver)
        lp.enter_user_name()
        lp.enter_password()
        lp.click_on_login_btn()

    def test_logout(self,test_launch_browser):
        time.sleep(3)
        lo=HomePage(driver)
        lo.click_on_logout_btn()
        time.sleep(2)