import unittest
from POM.Page.linkedlogin import linkedlogin
from POM.Page.linkedinlogout import linkedinlogout
import time
from selenium import webdriver
class MyTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome('C:/Users/abyja/PycharmProjects/test/drivers/chromedriver.exe')
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(10)
    def test_login(self):
        self.driver.get('https:/linkedin.com')
        time.sleep(2)
        login=linkedlogin(self.driver)
        login.loginbutton()
        # self.driver.find_element_by_css_selector('body > nav > a.nav__button-secondary').click()
        time.sleep(2)
        login.enter_username('')
        # self.driver.find_element_by_id('username').send_keys('abyjanevarkey@gmail.com')
        # self.driver.find_element_by_id('password').send_keys('thankyou')
        self.driver.implicitly_wait(10)
        login.enter_password('')
        time.sleep(2)
        login.loginbuttonreal()
        # self.driver.find_element_by_css_selector('#app__container > main > div:nth-child(2) > form > div.login__form_action_container > button').click()
        q=self.driver.title
        print(q)
        self.assertEqual(q,'LinkedIn')
    def test_logout(self):
        self.driver.get('http:/linkedin.com')
        time.sleep(2)
        logout=linkedinlogout(self.driver)
        logout.dropdown()
        time.sleep(2)
        logout.logout()
        # self.driver.find_element_by_css_selector('#ember37').click()
        time.sleep(2)
        # self.driver.find_element_by_xpath('//*[@href="/m/logout/"]').click()
        w=self.driver.title
        print(w)
        self.assertEqual(w,'LinkedIn: Log In or Sign Up')
    @classmethod
    def tearDownClass(cls):
        time.sleep(2)
        cls.driver.close()
        cls.driver.quit()
if __name__ == '__main__':
    unittest.main()
