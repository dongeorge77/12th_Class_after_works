from selenium import webdriver
import time
driver=webdriver.Chrome()
driver.maximize_window()
driver.get("http://localhost/login.do")
driver.find_element_by_name('username').send_keys("admin")
driver.find_element_by_name('pwd').send_keys("manager")
driver.find_element_by_xpath("//*[text()='Login ']").click()

time.sleep(3)
driver.find_element_by_xpath("//*[text()='USERS']").click()
driver.find_element_by_class_name("buttonText").click()

driver.find_element_by_xpath("//*[@id='userDataLightBox_firstNameField']").send_keys("abc")
driver.find_element_by_xpath("//*[@id='userDataLightBox_lastNameField']").send_keys("qwer")
driver.find_element_by_xpath("//*[@id='userDataLightBox_emailField']").send_keys("abcqwer@mail.com")

driver.find_element_by_id("userDataLightBox_usernameField").send_keys("qazxsw")
driver.find_element_by_id("userDataLightBox_passwordField").send_keys("123456")
driver.find_element_by_id("userDataLightBox_passwordCopyField").send_keys("123456")
time.sleep(2)

driver.find_element_by_xpath("//*[text()='Create User']").click()


time.sleep(5)
driver.quit()