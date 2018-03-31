import random

from selenium import webdriver
from selenium.webdriver import ActionChains
import time
from TBtestProject.case.models.basepage import BasePage

class NavigationBar(BasePage):
    """ 封装导航栏元素及其方法 """
    region = ('xpath', '//li[@data-name="region"]')     # 归属区域，默认中国大陆
    login = ('link text', '亲，请登录')                  # 登录
    register = ('link text', '免费注册')                 # 免费注册
    mobileSurf = ('link text', '手机逛淘宝')             # 手机逛淘宝
    mytaobao = ('link text', '我的淘宝')                 # 我的淘宝
    bought_item_list = ('link text', '已买到的宝贝')     # 已买到的宝贝
    myfoot = ('link text', '我的足迹')             # 我的足迹
    cart = ('id', 'mc-menu-hd')                   # 购物车
    collection = ('xpath', '//li[@id="J_SiteNavFavor"]/div[1]')  # 收藏夹
    item_collect = ('link text', '收藏的宝贝')              # 收藏的宝贝
    shop_collected = ('link text', '收藏的店铺')            # 收藏的店铺
    market_list = ('link text', '商品分类')                 # 商品分类
    seller = ('link text', '卖家中心')                      # 卖家中心
    consumerservice = ('link text', '联系客服')                      # 联系客服
    sitemap = ('xpath', '//li[@id="J_SiteNavSitemap"]/div[1]')      # 网站导航
    region_item = ('class name', 'site-nav-region-item J_RegionItem')   # 可选地区
    homepage = ('link text', '淘宝网首页')                  # 淘宝网首页，出现页面：手机逛淘宝页

    region_dicts = {0: '全球', 1: '中国大陆', 2: '香港', 3: '台湾', 4: '澳门',
                    5: '韩国', 6: '马来西亚', 7: '澳大利亚', 8: '新加坡',
                    9: '新西兰', 10: '加拿大', 11: '美国', 12: '日本'}

    def SWITCH_ACTION(self, num):
        js_find_region_item = 'var ul_item = document.getElementById("J_SiteNavRegionList"); ' \
                              'var lists = ul_item.getElementsByTagName("li");' \
                              'lists'+str(num)+'.click();'
        print("js===", end=' ')
        print(js_find_region_item)
        self.execute_script(js_find_region_item)

    @staticmethod
    def get_language_id(value):
        return BasePage.get_dict_id(NavigationBar.region_dicts, value)
        # return [k for k, v in NavigationBar.region_dicts.items() if v == value]

    def switch_language(self, languange, driver):
        """切换语言"""
        region_select = self.find_element(NavigationBar.region)
        self.moveToele(driver, region_select)
        num = NavigationBar.get_language_id(languange)
        print("num===", end=' ')
        print(num)
        self.SWITCH_ACTION(num)

    def switch_to_login(self):
        """去登录"""
        self.click(NavigationBar.login)

    def switch_to_register(self):
        """去注册"""
        self.click(NavigationBar.register)

    def switch_to_mobile(self):
        """去手机逛淘宝介绍页面"""
        self.click(NavigationBar.mobileSurf)

    def switch_to_mytaobao(self):
        """去我的淘宝"""
        self.click(NavigationBar.mytaobao)

    def switch_to_bought_item(self, driver):
        """跳转至已买到的宝贝"""
        ele = self.find_element(NavigationBar.mytaobao)
        self.moveToele(driver, ele)
        self.click(NavigationBar.bought_item_list)

    def switch_to_myfoot(self):
        """跳转至我的足迹"""
        ele = self.find_element(NavigationBar.mytaobao)
        self.moveToele(driver, ele)
        self.click(NavigationBar.myfoot)

    def switch_to_cart(self):
        """跳转至购物车"""
        self.click(NavigationBar.cart)

    def switch_to_collection(self):
        """跳转至我的收藏"""
        self.click(NavigationBar.collection)

    def switch_to_coll_item(self):
        """跳转至收藏的宝贝"""
        ele = self.find_element(NavigationBar.collection)
        self.moveToele(driver, ele)
        self.click(NavigationBar.item_collect)

    def switch_to_coll_shop(self):
        """跳转至收藏的店铺"""
        ele = self.find_element(NavigationBar.collection)
        self.moveToele(driver, ele)
        self.click(NavigationBar.shop_collected)

    def switch_to_market_list(self):
        """跳转至商品分类"""
        self.click(NavigationBar.market_list)

    def switch_to_seller(self):
        """跳转至卖家中心"""
        self.click(NavigationBar.seller)

    def switch_to_consumer(self):
        """跳转至联系客服"""
        self.click(NavigationBar.consumerservice)

    def switch_to_sitmap(self):
        """跳转至网站导航"""
        self.click(NavigationBar.sitemap)

if __name__ == "__main__":
    """ 模块自测 """
    driver = webdriver.Firefox()
    barDriver = NavigationBar(driver)
    barDriver.open('https://www.taobao.com/')

    # barDriver.click(NavigationBar.login)
    # driver.back()
    # barDriver.click(NavigationBar.surfBymobile)
    # driver.back()
    # barDriver.click(NavigationBar.myTaobao)
    # driver.back()
    # barDriver.click(NavigationBar.cart)
    # driver.back()

    barDriver.switch_language("美国", driver)
    driver.back()
    barDriver.switch_to_bought_item(driver)
    driver.back()
    barDriver.switch_language('加拿大',driver)






