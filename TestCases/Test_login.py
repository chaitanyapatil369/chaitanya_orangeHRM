from selenium import webdriver

from PageObjects.loginPage import LoginPage


class Test_login:
    Url = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
    username = "Admin"
    password = "admin123"

    def test_title_001(self):
        self.driver = webdriver.Chrome()
        self.driver.get(self.Url)
        actual_title = self.driver.title
        if actual_title == "OrangeHRM":
            assert True
        else:
            assert False

    def test_loginWithValidCredentials_002(self):
        self.driver = webdriver.Chrome()
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

