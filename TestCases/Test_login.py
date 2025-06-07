from selenium import webdriver
from PageObjects.loginPage import LoginPage
from Utilities.readproperties import ReadConfig
import pytest


class Test_login:
    Url = ReadConfig.get_url()
    username = ReadConfig.get_username()
    password = ReadConfig.get_password()

    def test_title_001(self, setup):
        self.driver = setup
        self.driver.get(self.Url)
        actual_title = self.driver.title
        if actual_title == "OrangeHRM":
            assert True
        else:
            assert False

    def test_loginWithValidCredentials_002(self, setup):
        self.driver = setup
        self.driver.get(self.Url)
        self.lp = LoginPage(self.driver)
        self.lp.enterUsername(self.username)
        self.lp.enterPassword(self.password)
        self.lp.clickLoginButton()
        login = self.lp.loginStatus()
        if login == "pass":
            assert True
        else:
            assert False

