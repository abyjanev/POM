import unittest
import HtmlTestRunner
from selenium import webdriver
import time
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
from POM.Page.fbloginpage import fblogin
from POM.Page.fbsearchpage import fbsearch
from POM.Page.fblogoutpage import fblogout
class MyTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver=webdriver.Chrome('C:/Users/abyja/PycharmProjects/test/drivers/chromedriver.exe')
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(10)
    def test_facebooklogin(self):
        self.driver.get('https:/facebook.com')
        time.sleep(2)
        login=fblogin(self.driver)
        login.enteremail('')
        #self.driver.find_element_by_id('email').send_keys('aby.jane@gmail.com')
        time.sleep(2)
        login.enterpassword('')
        #self.driver.find_element_by_id('pass').send_keys('molootty1991')
        time.sleep(2)
        login.loginclick()
        #self.driver.find_element_by_xpath('//*[@id="u_0_b"]').click()
        time.sleep(2)
        q=self.driver.title
        print(q)
        self.assertEqual(q,'Facebook')
    def test_facebooksearch(self):
         self.driver.get('https:/facebook.com')
         time.sleep(2)
         search=fbsearch(self.driver)
         search.enterkeyword('Neethu George')
         #self.driver.find_element_by_name('q').send_keys('Neethu George')
         time.sleep(2)
         search.searchbuttonclick()
         #self.driver.find_element_by_css_selector('#bluebarRoot > div > div > div > div._2t-e > div._4kny._50tm > div > form > button').click()
         time.sleep(2)
         w=self.driver.title
         print(w)
         self.assertEqual(w,'Neethu George – Facebook Search')
    def test_zlogout(self):
        self.driver.get('https:/facebook.com')
        self.driver.implicitly_wait(10)
        logout=fblogout(self.driver)
        logout.dropdownclick()
        time.sleep(2)
        logout.logoutbuttonclick()
        #self.driver.find_element_by_xpath('//*[@id="userNavigationLabel"]').click()
        time.sleep(2)
        #self.driver.find_element_by_xpath('//div[@id='u_d_1']/div/div/div/div/div/ul/li[12]/a/span/span').click()
        e=self.driver.title
        print(e)
        self.assertEqual(e,'Facebook – log in or sign up')
    @classmethod
    def tearDownClass(cls):
        time.sleep(2)
        cls.driver.close()
        cls.driver.quit()

if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='C:/Users/abyja/PycharmProjects/test/reports'))
