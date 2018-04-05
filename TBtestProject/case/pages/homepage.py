import selenium
import time
from selenium import webdriver
from selenium.webdriver import ActionChains

from TBtestProject.case.models.basepage import BasePage
from TBtestProject.case.models.navigationbar import NavigationBar

class HomePage(NavigationBar):
    """封装主页元素及其方法"""
    _search_text = ('id', 'q')
    _search_btn = ('xpath', '//button[@type="submit"]')
    search_models = {0: "宝贝", 1: "天猫", 2: "店铺"}
    default_search_text = ('xpath', '//label[@for="q"]/span')

    @staticmethod
    def get_model_id(model):
        """
        Usage：查找切换模式需要点击的元素
        return: 返回元素id
        """
        return BasePage.get_dict_id(HomePage.search_models, model)

    def switch_search_model(self, model):
        """
        Usage: 切换搜索模式
               目前的可选模式为：按宝贝搜索、按天猫搜索、按店铺搜索
        """
        id = self.get_model_id(model)
        print("the search model to be selected is:" + ''.join(HomePage.search_models[id]))
        js_command = 'var ul_item = document.getElementsByClassName("ks-switchable-nav")[0]; ' \
                     'var lists = ul_item.getElementsByTagName("li");' \
                     'lists['+str(id)+'].click();'
        self.execute_script(js_command)
        print("已切换到"+model+"搜索模式")

    def item_search(self, item):
        """搜索宝贝"""
        self.switch_search_model('宝贝')
        self.sendKeys(HomePage._search_text, item)
        self.click(HomePage._search_btn)

    def tianmao_search(self, item):
        """在天猫中搜索"""
        self.switch_search_model('天猫')
        self.sendKeys(HomePage._search_text, item)
        self.click(HomePage._search_btn)

    def shop_search(self, item):
        """搜索店铺"""
        self.switch_search_model('店铺')
        self.sendKeys(HomePage._search_text, item)
        self.click(HomePage._search_btn)

    def get_default_search_text(self):
        """获取搜索框中的默认文字"""
        innerHTML = self.find_element(HomePage.default_search_text).get_attribute('innerHTML')
        return BasePage.filter_to_get_word(innerHTML)

if __name__ == "__main__":
    driver = webdriver.Chrome()
    homedriver = HomePage(driver)
    homedriver.open('https://www.taobao.com/')


    homedriver.switch_region(driver, '韩国')

    homedriver.tianmao_search("羽绒服")
    homedriver.go_back()

    homedriver.shop_search("安安家")
    homedriver.go_back()

    homedriver.item_search("lamer")
    homedriver.go_back()

    e = homedriver.get_default_search_text()
    print("default text==="+e)
