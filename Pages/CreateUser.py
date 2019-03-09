class CreateUser:
    def __init__(self,driver):
        self.driver=driver
        self.users="//*[@id='topnav']/tbody/tr[1]/td[5]/a"

    def click_on_users_btn(self):
        self.driver.find_element_by_xpath(self.users).click()

