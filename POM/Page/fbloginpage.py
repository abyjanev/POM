from POM.locators.fblocators import fblocators
class fblogin():
    def __init__(self,driver):
        self.driver=driver
        self.emailid=fblocators.emailid
        self.passwordid=fblocators.passwordid
        self.login=fblocators.login

    def enteremail(self,email):
        self.driver.find_element_by_id(self.emailid).send_keys(email)
    def enterpassword(self,password):
        self.driver.find_element_by_id(self.passwordid).send_keys(password)
    def loginclick(self):
        self.driver.find_element_by_xpath(self.login).click()
