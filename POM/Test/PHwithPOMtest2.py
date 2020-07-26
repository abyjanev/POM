import unittest
import HtmlTestRunner
import time
from selenium import webdriver
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.common.by import By
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
from POM.Page.PHsearchpage import phsearch
from POM.Page.PHloginpage import phlogin
from POM.Page.PHlogoutpage import phlogout
class MyTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print('This runs before all the tests')
        cls.driver = webdriver.Chrome(executable_path='C:/Users/abyja/PycharmProjects/test/drivers/chromedriver.exe')
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()
    def test_earch(self):
        self.driver.get('https://pornhub.com')
        search=phsearch(self.driver)
        search.enter_keyword('girls')
        search.click_search()
        # self.driver.find_element_by_id('searchInput').send_keys('girls')
        # self.driver.find_element_by_id('btnSearch').click()
        time.sleep(4)
        q = self.driver.title
        print(q)
        self.assertEqual(q,'Girls Porn Videos | Pornhub.com')
    def test_login(self):
        self.driver.get('https://pornhub.com')
        login=phlogin(self.driver)
        login.login()
        login.enter_username('')
        login.enter_password('')
        time.sleep(2)
        login.loginbuttonclick()
        # self.driver.find_element_by_id('headerLoginLink').click()
        # self.driver.find_element_by_id('username').send_keys('tubesfruitloop')
        # self.driver.find_element_by_id('password').send_keys('qwe123')
        # wait =WebDriverWait(self.driver, 10)
        # element=wait.until(EC.element_to_be_clickable((By.ID, 'submit')))
        # element.click()
        time.sleep(4)
        z=self.driver.title
        print(z)
        self.assertEqual(z,'Watch The Best Premium HD Porn Videos | Pornhub Premium home')
    def test_logout(self):
        self.driver.get('https://pornhub.com')
        logout=phlogout(self.driver)
        logout.clickondropdown()
        logout.clicklogout()
        # self.driver.find_element_by_id('profileMenuWrapper').click()
        # self.driver.find_element_by_css_selector('#profileMenuDropdown > li.signOut.omega > a').click()
        time.sleep(4)
        w=self.driver.title
        print(w)
        self.assertEqual(w,'Watch The Best Premium HD Porn Videos | Pornhub Premium home')
    @classmethod
    def tearDownClass(cls):
         print('This runs after all tests')
         time.sleep(2)
         cls.driver.close()
         cls.driver.quit()
if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='C:/Users/abyja/PycharmProjects/test/reports'))
