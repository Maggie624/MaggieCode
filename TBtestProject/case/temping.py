"""
测试代码
"""

from case.models.base import BasePage
from selenium import webdriver

SEARCH_INPUT = ['input', ('id', 'kw')]
SEARCH_BUTTON = ['button', ('id', 'su')]


class Baidu(BasePage):


    def search_item(self):

        default_args = [SEARCH_INPUT, '搜索的内容', SEARCH_BUTTON]
        self.perform_actions(*default_args)


if __name__ == "__main__":

    driver = webdriver.Firefox()
    baidudriver = Baidu(driver)
    baidudriver.open('https://www.baidu.com/')

    baidudriver.search_item()