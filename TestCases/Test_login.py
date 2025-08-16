import pytest

from PageObjects.loginPage import LoginPage
from Utilities.readproperties import ReadConfig
from Utilities.logger import logGen


class Test_login:
    Url = ReadConfig.get_url()
    username = ReadConfig.get_username()
    password = ReadConfig.get_password()
    log = logGen.loggen()

    # @pytest.mark.skip
    def test_title_001(self, setup):
        self.driver = setup
        self.log.info("getting url" + self.Url)
        self.driver.get(self.Url)
        actual_title = self.driver.title
        self.log.info("checking PageTitle")
        if actual_title == "OrangeHRM":
            self.log.info("test_title_001 Passed")
            assert True
        else:
            self.log.info("test_title_001 Failed")
            self.driver.save_screenshot(".\\Screenshots\\test_title_001.png")
            assert False

    # @pytest.mark.skip
    def test_login002(self, setup):
        self.driver = setup
        self.driver.get(self.Url)
        self.log.info("getting url" + self.Url)
        self.lp = LoginPage(self.driver)
        self.log.info("entering username" + self.username)
        self.lp.enterUsername(self.username)
        self.log.info("entering password" + self.password)
        self.lp.enterPassword(self.password)
        self.log.info("clicking on login button")
        self.lp.clickLoginButton()
        self.log.info("checking login status")
        login = self.lp.loginStatus()
        if login == True:
            self.log.info("clicking on logout")
            self.lp.clickLogoutButton()
            self.log.info("test_loginWithValidCredentials_002 Passed")
            assert True
        else:
            self.log.info("test_loginWithValidCredentials_002 Failed")
            self.driver.save_screenshot(".\\Screenshots\\test_loginWithValidCredentials_002.png")
            assert False

