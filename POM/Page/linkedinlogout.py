from POM.locators.linkedinlocators import linkedinlocatorscollection
class linkedinlogout():
    def __init__(self,driver):
        self.driver=driver
        self.dropdowncss=linkedinlocatorscollection.dropdowncss
        self.logoutxpath=linkedinlocatorscollection.logoutxpath
    def dropdown(self):
        self.driver.find_element_by_css_selector(self.dropdowncss).click()
    def logout(self):
        self.driver.find_element_by_xpath(self.logoutxpath).click()


