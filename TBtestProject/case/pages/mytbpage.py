import time
from selenium.common.exceptions import TimeoutException
from case.models.navigationbar import NavigationBar
from selenium import webdriver


class MyTbPage(NavigationBar):
    """
       我的淘宝页面
    """
    logo = ('xpath', "//a[@title='我的淘宝']")         # 导航栏下的"我的淘宝"图片
    myCart = ('link text', '我的购物车')        # 我的购物车
    bought_item = ('link text', '已买到的宝贝')     # 已买到的宝贝
    bought_shop = ('link text', '购买过的商铺')         # 购买过的商铺
    myInvoice = ('link text', '我的发票')             # 我的发票
    myCollection = ('link text', '我的收藏')          # 我的收藏
    myScores = ('link text', '我的积分')              # 我的积分
    DiscountInfo = ('link text', '我的优惠信息')       # 我的优惠信息
    Evaluation = ('link text', '评价管理')            # 评价管理
    Refund = ('link text', '退款维权')                # 退款维权
    myFoot = ('link text', '我的足迹')                # 我的足迹
    FlowPurse = ('link text', '流量钱包')             # 流量钱包
    searchBox = ('id', 'q')                          # 搜索框，输入搜索文本
    searchBtn = ('class name', 'btn-search')         # 搜索按钮

    # 名字下方的五个订单状态
    waitpay = ('xpath', '//span[text()="待付款"]')
    waitsend = ('xpath', '//span[text()="待发货"]')
    waitconfirm = ('xpath', '//span[text()="待收货"]')
    waitrate = ('xpath', '//span[text()="待评价"]')
    refund = ('xpath', '//span[text()="退款"]')

    alls = ('xpath', '//span[text()="所有订单"]')     # 所有订单


    def islogin(self):
        # 判断是否登录成功
        try:
            self.find_element(MyTbPage.logo)
        except TimeoutException:
            return False
        else:
            return True

if __name__ == '__main__':
    '页面自测'
    driver = webdriver.Firefox()
    tbdriver = MyTbPage(driver)
    tbdriver.open('https://login.taobao.com')
    tbdriver.switch_to_mytaobao()
    time.sleep(2)
    current_handle = tbdriver.curr_window_handle()
    print('curr==', current_handle)
    tbdriver.click(MyTbPage.waitpay)
    time.sleep(2)
    handles = tbdriver.get_window_handles()
    print('handles=', handles)

    for handle in handles:
        if handle != current_handle:
            tbdriver.switch_to_window(handle)
            time.sleep(2)

    tbdriver.click(MyTbPage.alls)
    time.sleep(1)
    tbdriver.close_tap()
    time.sleep(1)
    tbdriver.switch_to_window(current_handle)
    tbdriver.click(MyTbPage.waitpay)




