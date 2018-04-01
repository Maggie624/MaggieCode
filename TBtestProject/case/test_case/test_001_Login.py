import unittest

from selenium import webdriver

from TBtestProject.case.pages.loginpage import LoginPage
from TBtestProject.case.pages.mytbpage import MyTbPage


class Login(unittest.TestCase):
    """登录功能测试"""
    username = 'xxxxxxxxxx'
    password = 'xxxxxxxxxx'

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Firefox()
        cls.logindriver = LoginPage(cls.driver)
        cls.mytbdriver = MyTbPage(cls.driver)
        cls.logindriver.open('https://login.taobao.com')

    def setUp(self):
        pass

    def test_login(self):
        '登录功能测试'
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