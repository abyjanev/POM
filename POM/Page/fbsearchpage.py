from POM.locators.fblocators import fblocators
class fbsearch():
    def __init__(self,driver):
        self.driver=driver
        self.searchfieldname=fblocators.searchfieldname
        self.searchbutton=fblocators.searchbutton
    def enterkeyword(self,keyword):
        self.driver.find_element_by_name(self.searchfieldname).send_keys(keyword)
    def searchbuttonclick(self):
        self.driver.find_element_by_css_selector(self.searchbutton).click()