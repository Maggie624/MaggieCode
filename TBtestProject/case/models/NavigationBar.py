import random

from selenium import webdriver
from selenium.webdriver import ActionChains
import time
from TBtestProject.case.models.BasePage import BasePage

class NavigationBar(BasePage):
    """ 封装导航栏元素及其方法 """
    region = ('xpath', '//li[@data-name="region"]')     # 归属区域，默认中国大陆
    login = ('link text', '亲，请登录')                  # 登录，点击后，跳转到登录页面
    register = ('link text', '免费注册')                 # 免费注册，点击后，跳转到注册页面
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

    region_dicts = {0: '全球', 1: '中国大陆', 2: '香港', 3: '台湾', 4: '澳门',
                    5: '韩国', 6: '马来西亚', 7: '澳大利亚', 8: '新加坡',
                    9: '新西兰', 10: '加拿大', 11: '美国', 12: '日本'}

    def SWITCH_ACTION(self, num):
        js_find_region_item = 'var ul_item = document.getElementById("J_SiteNavRegionList"); ' \
                              'var lists = ul_item.getElementsByTagName("li");' \
                              'for(var i=0; i<lists.length; i++){lists['+str(num)+'].click();}'
        self.driver.execute_script(js_find_region_item)

    @staticmethod
    def get_keys(value):
        return [k for k, v in NavigationBar.region_dicts.items() if v == value]

    def switch_language(self, languange):
        region_select = self.find_element(NavigationBar.region)
        self.moveToele(driver, region_select)
        num = NavigationBar.get_keys(languange)
        self.SWITCH_ACTION(num)




if __name__ == "__main__":
    """ 模块自测 """
    driver = webdriver.Chrome()
    barDriver = NavigationBar(driver)
    #barDriver.open('http://127.0.0.1:49776/TBhomepage.html')
    barDriver.open('https://www.taobao.com/')

    # barDriver.click(NavigationBar.login)
    # driver.back()
    # barDriver.click(NavigationBar.surfBymobile)
    # driver.back()
    # barDriver.click(NavigationBar.myTaobao)
    # driver.back()
    # barDriver.click(NavigationBar.cart)
    # driver.back()

    #barDriver.switch_language("美国")

    ele = barDriver.find_element(NavigationBar.mytaobao)
    driver.moveToele(ele)
    time.sleep(1)






