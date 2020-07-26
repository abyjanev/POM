from POM.locators.Locators import locators
class phsearch():

    def __init__(self,driver):
        self.driver=driver
        self.searchboxid=locators.searchboxid
        self.searchbuttonid=locators.searchbuttonid
    def enter_keyword(self,keyword):
        self.driver.find_element_by_id(locators.searchboxid).send_keys(keyword)
    def click_search(self):
        self.driver.find_element_by_id(locators.searchbuttonid).click()




