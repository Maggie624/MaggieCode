import time
from selenium import webdriver

from TBtestProject.case.models.MyTbPage import MyTbPage
from TBtestProject.case.pages.LoginPage import LoginPage
import unittest
from TBtestProject.case.models.publicFunc import Login as pF


class Login(unittest.TestCase):

    username = ''
    password = ''

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Firefox()
        cls.logindriver = LoginPage(cls.driver)
        cls.mytbdriver = MyTbPage(cls.driver)
        cls.logindriver.open('https://login.taobao.com')

    def setUp(self):
        pass

    def test_login(self):
        self.logindriver.send_name(Login.username)     # 输入用户名
        self.logindriver.send_psw(Login.password)      # 输入密码
        self.logindriver.login()
        self.assertTrue(self.mytbdriver.islogin())
        # 截图功能后续需要改进
        self.logindriver.get_screenshot(r'/Users/maoqi/MaggieCode/TBtestProject/report/test_login.png')

    def tearDown(self):
        pass

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()

if __name__ == '__main__':
    unittest.main()