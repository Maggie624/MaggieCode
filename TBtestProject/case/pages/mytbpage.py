from selenium.common.exceptions import TimeoutException

from TBtestProject.case.models.base import BasePage
from TBtestProject.case.models.navigationbar import NavigationBar


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

    def islogin(self):
        # 判断是否登录成功
        try:
            self.find_element(MyTbPage.logo)
        except TimeoutException:
            return False
        else:
            return True

    """
    TODO:
       目前登录功能不稳定，滑块拖动后，验证通过，但偶尔无法进入我的淘宝页面，这部分功能以后写

    """

