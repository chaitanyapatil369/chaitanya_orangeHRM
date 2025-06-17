import time

from selenium.common import NoSuchElementException, TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains



class AddEmployeePage:
    BTN_PIM_Xpath = (By.XPATH, "//a[normalize-space()='PIM']")
    BTN_add_Xpath = (By.XPATH, "//button[normalize-space()='Add']")
    TXT_FirstName_Xpath = (By.XPATH, "//input[@placeholder='First Name']")
    TXT_MiddleName_Xpath = (By.XPATH, "//input[@placeholder='Middle Name']")
    TXT_LastName_Xpath = (By.XPATH, "//input[@placeholder='Last Name']")
    BTN_Save_Xpath = (By.XPATH, "//button[@type='submit']")
    Tag_PersonalDetails_Xpath = (By.XPATH, "//h6[normalize-space()='Personal Details']")
    # TXT_employeeID_Xpath = (By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[1]/div[2]/div/div/div[2]/input')
    Btn_addEmployee_Xpath = (By.XPATH, "//a[normalize-space()='Add Employee']")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)
        self.action = ActionChains(self.driver)

    def clickPIM(self):
        time.sleep(5)
        self.driver.find_element(*self.BTN_PIM_Xpath).click()

    def clickAddButton(self):
        time.sleep(5)
        # self.wait.until(ec.element_to_be_selected(*self.BTN_add_Xpath))
        self.driver.find_element(*AddEmployeePage.BTN_add_Xpath).click()

    def enterFirstName(self, firstname):
        # self.wait.until(ec.element_to_be_clickable(self.TXT_FirstName_Xpath))
        time.sleep(2)
        self.driver.find_element(*AddEmployeePage.TXT_FirstName_Xpath).send_keys(firstname)

    def enterMiddleName(self, middlename):
        self.driver.find_element(*AddEmployeePage.TXT_MiddleName_Xpath).send_keys(middlename)

    def enterLastName(self, lastname):
        self.driver.find_element(*AddEmployeePage.TXT_LastName_Xpath).send_keys(lastname)

    # def enteremployeeID(self):
    #     # time.sleep(5)
    #     self.wait.until(ec.presence_of_element_located(self.TXT_employeeID_Xpath))
    #     self.driver.find_element(*AddEmployeePage.TXT_employeeID_Xpath).click()

    def clickSaveButton(self):
        self.driver.find_element(*AddEmployeePage.BTN_Save_Xpath).click()

    def clickAddEmployee(self):
        time.sleep(4)
        self.driver.find_element(*AddEmployeePage.Btn_addEmployee_Xpath).click()

    def employee_add_status(self):
        try:
            self.wait.until(ec.presence_of_element_located(self.Tag_PersonalDetails_Xpath))
            return True
        except TimeoutException:
            return False
