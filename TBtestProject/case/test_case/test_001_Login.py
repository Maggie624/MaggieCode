import unittest
import ddt
import time
from selenium import webdriver
from selenium.common.exceptions import UnexpectedAlertPresentException

from TBtestProject.case.models.mytestcase import MyTestCase
from TBtestProject.case.pages.loginpage import LoginPage
from TBtestProject.case.pages.mytbpage import MyTbPage
from TBtestProject.data.excel_utils import ExcelUtil
from TBtestProject.case.models.HTMLTestRunner import _previou_case_result

test_datas = ExcelUtil(sheetName='login').dict_data()

@ddt.ddt
class Login(MyTestCase):
    """登录功能测试"""
    # username = 'xxxxxxxxxx'
    # password = 'xxxxxxxxxx'

    @classmethod
    def setUpClass(cls):
        pass

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.logindriver = LoginPage(self.driver)
        self.mytbdriver = MyTbPage(self.driver)
        self.logindriver.open('https://login.taobao.com')

    @ddt.data(*test_datas)
    def test_00_login_error(self, data):
        self.logindriver.login(data['username'], data['psw'])
        self.assertEqual(data['msg'], self.logindriver.get_error_hint(), msg=data['hint'])

    def test_01_login_user_psw_null(self):
        '用户名、密码为空，登录'
        print('========status=========')
        print(_previou_case_result[0])
        if _previou_case_result[0] == 0:
            raise unittest.SkipTest('已经测试通过')
        self.logindriver.login('', '')
        a = self.assertEqual('请输入账户名和密码',
                             self.logindriver.get_error_hint(),
                             msg=self._testMethodName)
        print(a)

    def test_02_login_psw_null(self):
        '密码为空,登录'
        print('========status=========')
        print(_previou_case_result[0])
        if _previou_case_result[0] == 0:
            raise unittest.SkipTest('已经测试通过')
        self.logindriver.login('18000000000', '')
        self.assertEqual('请输入密码',
                         self.logindriver.get_error_hint(),
                         msg=self._testMethodName)

    def test_03_login_user_null(self):
        '用户名为空，登录'
        print('========status=========')
        print(_previou_case_result[0])
        if _previou_case_result[0] == 0:
            raise unittest.SkipTest('已经测试通过')
        self.logindriver.login('', 'qazwsxedcrfv180000')
        self.assertEqual('请填写账户名',
                         self.logindriver.get_error_hint(),
                         msg=self._testMethodName)

    def test_04_login_fail(self):
        '用户名和密码不匹配'
        self.logindriver.login('18000000000', 'qazwsxedcrfv180000')
        self.assertEqual('你输入的密码和账户名不匹配，是否忘记密码或忘记会员名',
                         self.logindriver.get_error_hint(),
                         msg=self._testMethodName)

    def test_05_login_success(self):
        '正确的账号密码，登录'
        username = 'xxxxxxxx'
        password = 'xxxxxxx'
        self.logindriver.login(username, password)
        self.assertTrue(self.mytbdriver.islogin(),
                        msg=self._testMethodName)

    def tearDown(self):
        self.driver.quit()

    @classmethod
    def tearDownClass(cls):
        #cls.driver.quit()
        pass


if __name__ == '__main__':
    unittest.main()