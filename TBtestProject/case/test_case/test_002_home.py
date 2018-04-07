import unittest
from selenium import webdriver
from unittest.suite import _ErrorHolder

from TBtestProject.case.models.navigationbar import NavigationBar
from TBtestProject.case.pages.homepage import HomePage
from TBtestProject.case.pages.baobeipage import BaobeiPage


class Home(unittest.TestCase):
    """淘宝网主页功能测试"""
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.homedriver = HomePage(self.driver)
        self.homedriver.open("https://www.taobao.com/")
        self.itemdriver = BaobeiPage(self.driver)
        self.navdriver = NavigationBar(self.driver)

    def tearDown(self):
        self.driver.close()

    def test_01_search_item_none(self):
        '不输入文本，搜索默认宝贝'
        default_search_item = self.homedriver.get_default_search_text()
        self.homedriver.item_search(default_search_item)
        self.assertEqual(self.itemdriver.get_search_text(), default_search_item)   # 判断搜索框中内容正确
        self.assertTrue(self.itemdriver.get_logo())       # 通过logo判断界面正确

    def test_02_search_item_not_exist(self):
        '搜索不存在的宝贝,例如:qazxjdoel'
        search_item = 'qazxjdoel'
        self.homedriver.item_search(search_item)
        expect_hint = '\n        <div>没有找到与“<span class="h">'+search_item+'</span>”相关的宝贝</div>\n      '
        self.assertEqual(self.itemdriver.get_not_exist_hint(), expect_hint)

    def test_03_search_item(self):
        '搜索宝贝:羽绒服'
        search_item = '羽绒服'
        self.homedriver.item_search(search_item)
        self.assertEqual(self.itemdriver.get_search_text(), search_item)

    def test_04_change_region(self):
        '切换地区为:澳大利亚'
        target_region = '澳大利亚'
        self.navdriver.switch_region(self.driver, target_region)
        self.assertEqual(self.navdriver.get_current_region(), target_region)

if __name__ == "__main__":
    # discover = unittest.defaultTestLoader.discover('./', pattern='test*.py')
    # runner = unittest.TextTestRunner()
    # runner.run(discover)
    unittest.main()