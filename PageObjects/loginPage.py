import time

from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait


class LoginPage:
    TXT_UserName_Xpath = (By.XPATH, "//input[@placeholder='Username']")
    TXT_Password_Xpath = (By.XPATH, "//input[@placeholder='Password']")
    BTN_Login_Xpath = (By.XPATH, "//button[@type='submit']")
    Text_Dashboard_Xpath = (By.XPATH, "//h6[contains(.,'Dashboard')]")
    DRP_account_Xpath = (By.XPATH, "//i[@class='oxd-icon bi-caret-down-fill oxd-userdropdown-icon']")
    BTN_logout_Xpath = (By.XPATH, "//a[normalize-space()='Logout']")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def enterUsername(self, username):
        self.wait.until(ec.presence_of_element_located(self.TXT_UserName_Xpath))
        self.driver.find_element(*LoginPage.TXT_UserName_Xpath).clear()
        self.driver.find_element(*LoginPage.TXT_UserName_Xpath).send_keys(username)

    def enterPassword(self, password):
        self.driver.find_element(*LoginPage.TXT_Password_Xpath).clear()
        self.driver.find_element(*LoginPage.TXT_Password_Xpath).send_keys(password)

    def clickLoginButton(self):
        self.driver.find_element(*LoginPage.BTN_Login_Xpath).click()

    def loginStatus(self):
        try:
            time.sleep(3)
            self.driver.find_element(*LoginPage.Text_Dashboard_Xpath)
            return True
        except NoSuchElementException:
            return False

    def clickLogoutButton(self):
        self.driver.find_element(*LoginPage.DRP_account_Xpath).click()
        self.driver.find_element(*LoginPage.BTN_logout_Xpath).click()
