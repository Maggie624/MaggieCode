import unittest
import time
from TBtestProject.case.models.base import BasePage

class MyTestCase(unittest.TestCase, BasePage):
    """封装断言方法"""

    def assertEqual(self, first, second, msg=None):
        """判断相等"""
        msg = str(msg).split('.')[-1]
        try:
            super(MyTestCase, self).assertEqual(first, second)
        except AssertionError as e:
            self.get_screenshot('error_'+msg+'.png')
            raise e
        else:
            print('success_'+msg)

    def assertTrue(self, expr, msg=None):
        """判断是否为True"""
        msg = str(msg).split('.')[-1]
        try:
            super(MyTestCase, self).assertTrue(expr)
        except AssertionError as e:
            self.get_screenshot('error_'+msg+'.png')
            raise e
        else:
            print('success_'+msg)




