from POM.locators.Locators import locators
class phlogout():
    def __init__(self,driver):
        self.driver=driver
        self.dropdownmenuid=locators.dropdownmenuid
        self.logoutcssselector=locators.logoutcssselector
    def clickondropdown(self):
        self.driver.find_element_by_id(locators.dropdownmenuid).click()
    def clicklogout(self):
        self.driver.find_element_by_css_selector(locators.logoutcssselector).click()

