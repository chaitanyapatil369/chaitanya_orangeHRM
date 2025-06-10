import time

from PageObjects.loginPage import LoginPage
from Utilities.logger import logGen
from Utilities.readproperties import ReadConfig
from Utilities import XLutils
from selenium.common import NoSuchElementException


class Test_DDT:
    Url = ReadConfig.get_url()
    log = logGen.loggen()
    path = "D:\\Local Disk\\Automation PROJECTS\\chaitanya_orangeHRM\\TestData\\ddt_testdata.xlsx"

    def test_datadrivenTest_003(self, setup):
        self.driver = setup
        self.log.info(" test_datadrivenTest_003 --> started")
        self.log.info("getting url " + self.Url)
        self.driver.get(self.Url)
        self.lp = LoginPage(self.driver)
        self.rows = XLutils.getrRowCount(self.path, "Sheet1")
        result_list = []
        for r in range(2, self.rows + 1):
            self.username = XLutils.readData(self.path, "Sheet1", r, 2)
            self.password = XLutils.readData(self.path, "Sheet1", r, 3)
            self.log.info("entering username " + self.username)
            self.lp.enterUsername(self.username)
            self.log.info("entering password " + self.password)
            self.lp.enterPassword(self.password)
            self.log.info("clicking on login button")
            self.lp.clickLoginButton()
            self.log.info("checking login status")
            actual_result = self.lp.loginStatus()
            self.log.info("login status is " + actual_result)
            self.log.info("writing actual_result in exel file")
            XLutils.writeData(self.path, "Sheet1", r, 5, actual_result)
            expected_result = XLutils.readData(self.path, "Sheet1", r, 4)
            if actual_result == expected_result:
                result_list.append("pass")
            else:
                result_list.append("fail")
            try:
                self.log.info("clicking on logout ")
                self.lp.clickLogoutButton()
            except NoSuchElementException:
                pass
        if "fail" not in result_list:
            assert True
        else:
            assert False

