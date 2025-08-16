import pytest

from PageObjects.addEmployeePage import AddEmployeePage
from PageObjects.loginPage import LoginPage
from Utilities import XLutils
from Utilities.logger import logGen
from Utilities.readproperties import ReadConfig


class Test_AddEmployee_DDT:
    Url = ReadConfig.get_url()
    username = ReadConfig.get_username()
    password = ReadConfig.get_password()
    log = logGen.loggen()

    def test_AddEmployeeDDT_004(self, setup):
        self.driver = setup
        self.driver.get(self.Url)
        self.log.info("get url" + self.Url)
        self.lp = LoginPage(self.driver)
        self.lp.enterUsername(self.username)
        self.log.info("enter username" + self.username)
        self.lp.enterPassword(self.password)
        self.log.info("enter password" + self.password)
        self.lp.clickLoginButton()
        self.log.info("click on login button")
        self.ae = AddEmployeePage(self.driver)
        self.ae.clickPIM()
        self.log.info("click PIM")
        self.driver.implicitly_wait(5)
        self.ae.clickAddButton()
        self.log.info("Click AddButton")
        self.path = ".\\TestData\\ddt_testdata.xlsx"
        self.rows = XLutils.getrRowCount(self.path, "Sheet1")
        status_list = []
        for r in range(2, self.rows+1):
            self.firstname = XLutils.readData(self.path, "Sheet1", r, 2)
            self.middlename = XLutils.readData(self.path, "Sheet1", r, 3)
            self.lastname = XLutils.readData(self.path, "Sheet1", r, 4)
            self.ae.enterFirstName(self.firstname)
            self.log.info("enter firstname " + self.firstname)
            self.ae.enterMiddleName(self.middlename)
            self.log.info("enter middletname " + self.middlename)
            self.ae.enterLastName(self.lastname)
            self.log.info("enter lastname " + self.lastname)
            # self.ae.enteremployeeID()
            self.ae.clickSaveButton()
            self.log.info("click save Button")
            status_list = []
            if self.ae.employee_add_status() == True:
                self.log.info("entry pass")
                status_list.append("pass")
                self.ae.clickAddEmployee()
                self.log.info("click Add Employee")
                XLutils.writeData(self.path, "Sheet1", r, 5, "pass")
            else:
                self.log.info("entry fail")
                status_list.append("fail")
                XLutils.writeData(self.path, "Sheet1", r, 5, "fail")
                self.driver.save_screenshot(".\\Screenshots\\test_AddEmployeeDDT_004.png")
        if "fail" not in status_list:
            self.log.info("test_AddEmployeeDDT_004 pass")
            self.lp.clickLogoutButton()
            self.log.info("click logout")
            assert True
        else:
            self.log.info("test_AddEmployeeDDT_004 fail")
            self.lp.clickLogoutButton()
            self.log.info("click logout")
            assert False




