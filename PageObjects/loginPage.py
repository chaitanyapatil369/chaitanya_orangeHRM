import time

from selenium.webdriver.common.by import By


class LoginPage:
    TXT_UserName_Xpath = (By.XPATH, "//input[@placeholder='Username']")
    TXT_Password_Xpath = (By.XPATH, "//input[@placeholder='Password']")
    BTN_Login_Xpath = (By.XPATH, "//button[@type='submit']")
    Text_Dashboard_Xpath = (By.XPATH, "//h6[contains(.,'Dashboard')]")

    def __init__(self, driver):
        self.driver = driver

    def enterUsername(self, username):
        time.sleep(2)
        self.driver.find_element(*LoginPage.TXT_UserName_Xpath).clear()
        self.driver.find_element(*LoginPage.TXT_UserName_Xpath).send_keys(username)

    def enterPassword(self, password):
        self.driver.find_element(*LoginPage.TXT_Password_Xpath).clear()
        self.driver.find_element(*LoginPage.TXT_Password_Xpath).send_keys(password)

    def clickLoginButton(self):
        self.driver.find_element(*LoginPage.BTN_Login_Xpath).click()

    def loginStatus(self):
        time.sleep(2)
        if self.driver.find_element(*LoginPage.Text_Dashboard_Xpath).text == "Dashboard":
            login_status = "pass"
        else:
            login_status = "fail"
        return login_status



