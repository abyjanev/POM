from POM.locators.linkedinlocators import linkedinlocatorscollection
class linkedlogin():
    def __init__(self,driver):
        self.driver=driver
        self.logincss=linkedinlocatorscollection.logincss
        self.usernameid=linkedinlocatorscollection.usernameid
        self.passwordid=linkedinlocatorscollection.passwordid
        self.loginbuttoncss=linkedinlocatorscollection.loginbuttoncss
    def loginbutton(self):
        self.driver.find_element_by_css_selector(self.logincss).click()
    def enter_username(self,username):
        self.driver.find_element_by_id(self.usernameid).send_keys(username)
    def enter_password(self,password):
        self.driver.find_element_by_id(self.passwordid).send_keys(password)
    def loginbuttonreal(self):
        self.driver.find_element_by_css_selector('#app__container > main > div:nth-child(2) > form > div.login__form_action_container > button').click()



