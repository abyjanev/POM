from POM.locators.fblocators import fblocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
class fblogout():
    def __init__(self,driver):
        self.driver=driver
        self.dropdownmenucssselector=fblocators.dropdownmenucssselector
        self.logoutbuttonrealclick=fblocators.logoutbuttonrealclick
    def dropdownclick(self):
        #wait = WebDriverWait(self.driver, 10)
        #element = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.dropdownmenucssselector)))
        #element.click()
        self.driver.find_element_by_css_selector(self.dropdownmenucssselector).click()
    def logoutbuttonclick(self):
        #wait=WebDriverWait(self.driver,10)
        #element=wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,self.logoutbuttonrealclick)))
        #element.click()
        self.driver.find_element_by_css_selector(self.logoutbuttonrealclick).click()
