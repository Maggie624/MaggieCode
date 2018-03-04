from TBtestProject.case.models.BasePage import BasePage

'''我的淘宝页面'''
class MyTbPage(BasePage):

    logo = ('xpath', "//a[@title='我的淘宝']")        # 导航栏下的"我的淘宝"图片

    def islogin(self):
        logo = self.find_element(MyTbPage.logo)
        if logo != None:
            return True
        else:
            return False