from ...case.models.navigationbar import NavigationBar
from selenium import webdriver
from ...case.pages.homepage import HomePage


class BaobeiPage(NavigationBar):
    """
    封装按照宝贝搜索的结果页面的元素及方法
    """
    search_text = ('id', 'q')                             # 搜索框
    search_btn = ('xpath', '//button[@type="submit"]')    # 搜索按钮
    logo = ('xpath', '//a[@href="//www.taobao.com"]')     # logo
    not_exist_flag = ('class name', 'item-not-found')     # 搜索内容不存在时的提示

    def get_search_text(self):
        """
        return: 搜索栏中的文字
        """
        return self.find_element(BaobeiPage.search_text).get_attribute('value')

    def get_logo(self):
        """
        usage: 通过搜索结果页面的logo元素，来判断是否跳转到搜索页面
        return: 存在logo返回true，否则返回false
        """

        try:
            self.find_element(BaobeiPage.logo)
            return True
        except TimeoutError as e:
            print("error:%s" % e.args)
            return False

    def get_not_exist_hint(self):
        flag = self.find_element(BaobeiPage.not_exist_flag)
        return flag.get_attribute('innerHTML')


if __name__ == "__main__":
    driver = webdriver.Firefox()
    homedriver = HomePage(driver)
    homedriver.open("https://www.taobao.com/")
    itemdriver = BaobeiPage(driver)

    homedriver.item_search("羽绒服")
    it = itemdriver.get_search_text()
    print(it)
    itemdriver.go_back()

    homedriver.item_search('keijewihr')
    item = itemdriver.find_element(BaobeiPage.not_exist_flag)
    print(item.get_attribute('innerHTML'))
