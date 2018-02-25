from selenium import webdriver

from case.models.MyTbPage import MyTbPage
from case.pages.LoginPage import LoginPage
import unittest


class Login(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.logindriver = LoginPage(self.driver)
        self.mytbdriver = MyTbPage(self.driver)
        self.logindriver.open('https://login.taobao.com')

    def test_login(self):
        self.logindriver.send_name('')
        self.logindriver.send_psw('')
        self.logindriver.login()
        self.assertTrue(self.mytbdriver.islogin())
        # 截图功能后续需要改进
        self.logindriver.get_screenshot(r'/Users/maoqi/MaggieCode/TBtestProject/report/test_login.png')

    def tearDown(self):
        self.driver.close()

if __name__ == '__main__':
    unittest.main()