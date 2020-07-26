from POM.locators.Locators import locators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
class phlogin():
    def __init__(self,driver):
        self.driver=driver
        self.loginbuttonid=locators.loginbuttonagainid
        self.usernameid=locators.usernameid
        self.passwordid=locators.passwordid
        self.loginbuttonagainid=locators.loginbuttonagainid
    def login(self):
        self.driver.find_element_by_id(locators.loginbuttonid).click()
    def enter_username(self,username):
         self.driver.find_element_by_id(locators.usernameid).send_keys(username)
    def enter_password(self,password):
        self.driver.find_element_by_id(locators.passwordid).send_keys(password)
    def loginbuttonclick(self):
        #wait = WebDriverWait(self.driver, 10)
        #element=wait.until(EC.element_to_be_clickable((By.ID,locators.loginbuttonagainid)))
        #element.click()
        self.driver.find_element_by_id(self.loginbuttonagainid).click()


