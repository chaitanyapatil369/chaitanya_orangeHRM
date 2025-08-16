import pytest

from PageObjects.loginPage import LoginPage
from Utilities.logger import logGen
from Utilities.readproperties import ReadConfig


class Test_login_params:
    Url = ReadConfig.get_url()
    username = ReadConfig.get_username()
    password = ReadConfig.get_password()
    log = logGen.loggen()

    # @pytest.mark.skip
    def test_loginParams_003(self, setup, getdataforlogin):
        self.driver = setup
        self.driver.get(self.Url)
        self.log.info("getting url " + self.Url)
        self.lp = LoginPage(self.driver)
        self.log.info("entering username " + getdataforlogin[0])
        self.lp.enterUsername(getdataforlogin[0])
        self.log.info("entering password " + getdataforlogin[1])
        self.lp.enterPassword(getdataforlogin[1])
        self.log.info("clicking on login button")
        self.lp.clickLoginButton()
        self.log.info("checking login status")
        if self.lp.loginStatus() == True:
            if getdataforlogin[2] == "pass":
                self.log.info("login successful")
                self.log.info("clicking on logout")
                self.lp.clickLogoutButton()
                self.log.info("test_loginParams_003 Passed")
                assert True
            else:
                self.log.info("login failed")
                self.log.info("test_loginParams_003 Failed")
                self.driver.save_screenshot(
                    ".\\Screenshots\\test_loginParams_003.png")
                assert False
        else:
            if getdataforlogin[2] == "fail":
                self.log.info("login failed")
                assert True
            else:
                self.log.info("login successful")
                self.log.info("test_loginParams_003 Failed")
                assert False



