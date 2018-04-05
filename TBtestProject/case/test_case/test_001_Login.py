import unittest

import time
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
        self.logindriver.refresh_()

    def test_01_login_user_psw_null(self):
        '用户名、密码为空，登录'
        self.logindriver.click_login_btn()
        self.assertEqual('请输入账户名和密码', self.logindriver.get_error_hint())

    def test_02_login_psw_null(self):
        '密码为空,登录'
        self.logindriver.send_name('18000000000')
        self.logindriver.send_psw('')
        self.logindriver.login()
        self.assertEqual('请输入密码', self.logindriver.get_error_hint())

    def test_03_login_user_null(self):
        '用户名为空，登录'
        self.logindriver.send_name('')
        self.logindriver.send_psw('qazwsxedcrfv180000')
        self.logindriver.login()
        self.assertEqual('请填写账户名', self.logindriver.get_error_hint())

    def test_04_login_fail(self):
        '用户名和密码不匹配'
        self.logindriver.send_name('18000000000')
        self.logindriver.send_psw('qazwsxedcrfv180000')
        self.logindriver.login()
        self.assertEqual('你输入的密码和账户名不匹配，是否忘记密码或忘记会员名', self.logindriver.get_error_hint())

    def test_05_login_success(self):
        '输入账号密码，登录'
        self.logindriver.send_name(Login.username)     # 输入用户名
        self.logindriver.send_psw(Login.password)      # 输入密码
        self.logindriver.login()
        self.assertTrue(self.mytbdriver.islogin())
        # 截图功能后续需要改进
        self.logindriver.get_screenshot(r'/Users/maoqi/MaggieCode/TBtestProject/report/test_login.png')

    def tearDown(self):
        pass

    def tearDownClass(cls):
        cls.driver.quit()


if __name__ == '__main__':
    unittest.main()