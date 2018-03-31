import unittest
from selenium import webdriver
from TBtestProject.case.pages.homepage import HomePage
from TBtestProject.case.pages.resultitempage import ResultItemPage


class Home(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.homedriver = HomePage(self.driver)
        self.homedriver.open("https://www.taobao.com/")
        self.itemdriver = ResultItemPage(self.driver)

    def tearDown(self):
        self.driver.close()

    def test_01_search_item_none(self):
        '不输入文本，搜索默认宝贝'
        default_search_item = self.homedriver.get_default_search_text()
        self.homedriver.item_search(default_search_item)
        self.assertEqual(self.itemdriver.get_search_text(), default_search_item)   # 判断搜索框中内容正确
        self.assertTrue(self.itemdriver.get_logo())       # 通过logo判断界面正确

    def test_02_search_item_not_exist(self):
        '搜索不存在的宝贝:qazxjdoel'
        search_item = 'qazxjdoel'
        self.homedriver.item_search(search_item)
        expect_hint = '\n        <div>没有找到与“<span class="h">'+search_item+'</span>”相关的宝贝</div>\n      '
        self.assertEqual(self.itemdriver.get_not_exist_hint(), expect_hint)

    def test_03_search_item(self):
        '搜索宝贝:羽绒服'
        search_item = '羽绒服'
        self.homedriver.item_search(search_item)
        self.assertEqual(self.itemdriver.get_search_text(), search_item)



if __name__ == "__main__":
    # discover = unittest.defaultTestLoader.discover('./', pattern='test*.py')
    # runner = unittest.TextTestRunner()
    # runner.run(discover)
    unittest.main()