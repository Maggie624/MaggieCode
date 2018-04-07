import unittest

import time
from selenium import webdriver
from selenium.common.exceptions import UnexpectedAlertPresentException

from TBtestProject.case.models.mytestcase import MyTestCase
from TBtestProject.case.pages.loginpage import LoginPage
from TBtestProject.case.pages.mytbpage import MyTbPage
import TBtestProject.case.models.func as Func


class Login(MyTestCase):
    """登录功能测试"""
    # username = 'xxxxxxxxxx'
    # password = 'xxxxxxxxxx'

    @classmethod
    def setUpClass(cls):
        pass

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.logindriver = LoginPage(self.driver)
        self.mytbdriver = MyTbPage(self.driver)
        self.logindriver.open('https://login.taobao.com')

    def test_01_login_user_psw_null(self):
        '用户名、密码为空，登录'
        self.logindriver.send_user_psw('', '')
        self.logindriver.click_login_btn()
        a = self.assertEqual('请输入账户名和密码',
                             self.logindriver.get_error_hint(),
                             msg=Func.get_current_func_name())
        print(a)

    def test_02_login_psw_null(self):
        '密码为空,登录'
        self.logindriver.send_user_psw('18000000000', '')
        self.logindriver.login()
        self.assertEqual('请输入密码',
                         self.logindriver.get_error_hint(),
                         msg=Func.get_current_func_name())

    def test_03_login_user_null(self):
        '用户名为空，登录'
        self.logindriver.send_user_psw('', 'qazwsxedcrfv180000')
        self.logindriver.login()
        self.assertEqual('请填写账户名',
                         self.logindriver.get_error_hint(),
                         msg=Func.get_current_func_name())

    def test_04_login_fail(self):
        '用户名和密码不匹配'
        self.logindriver.send_user_psw('18000000000', 'qazwsxedcrfv180000')
        self.logindriver.login()
        self.assertEqual('你输入的密码和账户名不匹配，是否忘记密码或忘记会员名',
                         self.logindriver.get_error_hint(),
                         msg=Func.get_current_func_name())

    def test_05_login_success(self):
        '输入账号密码，登录'
        username = 'xxxxxxxxxx'
        password = 'xxxxxxxxxx'
        self.logindriver.send_user_psw(username, password)
        self.logindriver.login()
        self.assertTrue(self.mytbdriver.islogin(),
                        msg=Func.get_current_func_name())

    def tearDown(self):
        self.driver.quit()

    @classmethod
    def tearDownClass(cls):
        #cls.driver.quit()
        pass


if __name__ == '__main__':
    unittest.main()