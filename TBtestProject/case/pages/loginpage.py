import time
from selenium import webdriver
from selenium.common.exceptions import TimeoutException, ElementNotInteractableException
from selenium.webdriver.common.action_chains import ActionChains

from TBtestProject.case.models.basepage import BasePage

class LoginPage(BasePage):

    """
    封装登录页面的元素及其方法
    """
    switch_login_mode = ('id', 'J_Quick2Static')  # 切换登录模式按钮
    username = ('id', 'TPL_username_1')           # 用户名输入框
    psw = ('id', 'TPL_password_1')                # 密码输入框
    form_item = ('id', 'J_Form')                  # 表单ID
    scan_tip = ('class name', 'ft-gray')          # 二维码下方"扫一扫登录"文字
    slider = ('id', 'nc_1_n1z')                   # 滑块
    error_hint = ('xpath', '//div[@id="J_Message"]/p')          # 登录失败的原因提示

    def switch_to_psw_login(self):
        """Usage: 切换到用户名密码登陆框"""
        self.click(LoginPage.switch_login_mode)
        LoginPage.LOGINFLAG = True

    def switch_model(self):
        """ 切换登录方式，实际的切换操作在 switch_to_psw_login 中执行 """
        try:
            scan_img = self.find_element(LoginPage.scan_tip) # 查找二维码图片，存在则需要切换登陆方式为用户名、密码登录
        except ElementNotInteractableException:
            print("当前在用户名密码登录模式")
        else:
            self.switch_to_psw_login()

    def send_name(self, name):
        """ 输入用户名 """
        # 输入用户名
        # 首先判断当前是否为用户名密码登录方式，不是则需要切换登录方式
        self.switch_model()
        self.sendKeys(LoginPage.username, name)
        time.sleep(0.5)
        print('send username sucessfully!!!')

    def send_psw(self, psw):
        """ 输入密码 """
        self.sendKeys(LoginPage.psw, psw)
        time.sleep(0.5)
        print('send password sucessfully!!!')

    def ACTION_DRAG(self):
        """ 执行拖拉操作 """
        slider = self.find_element(LoginPage.slider)
        action = ActionChains(self.driver)
        action.click_and_hold(slider).perform()
        # time.sleep(0.05)
        action.move_by_offset(258, 0).perform()
        print('drag slider sucessfully!!!')

    def dragSlider(self):
        """ 拖动滑动条，实际的拖拉操作在 ACTION_DRAG 中执行 """
        try:
            a = self.find_element(LoginPage.slider)
            self.ACTION_DRAG()
        except TimeoutException:
            print("不需要滑动验证")


    def login(self):
        """ 登录 """
        self.dragSlider()
        time.sleep(0.1)
        self.click_login_btn()

    def click_login_btn(self):
        """点击登录按钮"""
        self.find_element(LoginPage.form_item).submit()
        time.sleep(1)

    def get_error_hint(self):
        """return：登录失败的提示"""
        return self.find_element(LoginPage.error_hint).get_attribute('innerHTML')

if __name__ == "__main__":

    driver = webdriver.Firefox()
    logindriver = LoginPage(driver)
    logindriver.open("https://login.taobao.com")
    logindriver.send_name("xxxxxxxxx")
    logindriver.send_psw("xxxxxxxx")
    logindriver.login()
    print(logindriver.get_error_hint())

