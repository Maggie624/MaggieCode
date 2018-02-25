import time
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains

from case.models.BasePage import BasePage

class LoginPage(BasePage):

    switch_login_mode = ('id', 'J_Quick2Static')  # 切换登录模式按钮
    username = ('id', 'TPL_username_1')           # 用户名输入框
    psw = ('id', 'TPL_password_1')                # 密码输入框
    form_item = ('id', 'J_Form')                  # 表单ID
    scan_tip = ('class name', 'ft-gray')          # 二维码下方"扫一扫登录"文字
    slider = ('id', 'nc_1_n1z')                   # 滑块

    LOGINFLAG = False              # 登陆方式，True为用户名密码登录，False为扫码登录

    def switch_to_psw_login(self):
        # 切换到用户名密码登陆框
        self.click(LoginPage.switch_login_mode)
        LoginPage.LOGINFLAG = True

    def switch_model(self):
        # 查找二维码图片，存在则需要切换登陆方式为用户名、密码登录
        scan_img = self.find_element(LoginPage.scan_tip)
        if scan_img:
            self.switch_to_psw_login()

    def send_name(self, name):
        # 输入用户名
        # 首先判断当前是否为用户名密码登录方式，不是则需要切换登录方式
        if LoginPage.LOGINFLAG == False: self.switch_model()
        self.sendKeys(LoginPage.username, name)
        print('send username sucessfully!!!')

    def send_psw(self, psw):
        # 输入密码
        # 首先判断当前是否为用户名密码登录方式，不是则需要切换登录方式
        if LoginPage.LOGINFLAG == False: self.switch_model()
        self.sendKeys(LoginPage.psw, psw)
        print('send password sucessfully!!!')

    def ACTION_DRAG(self, element):
        # 执行拖动滑动块的动作
        print('action_drag')
        action = ActionChains(driver)
        action.click_and_hold(element).move_by_offset(258, 0).perform()

    def dragSlider(self):
        # 判断滑动条是否存在,存在则需要拖动滑块
        try:
            slider = self.find_element(LoginPage.slider)
            self.ACTION_DRAG(slider)
        except TimeoutException:
            print("没有滑动验证")


    def login(self):
        # 登录
        self.dragSlider()
        time.sleep(0.05)
        self.find_element(LoginPage.form_item).submit()



if __name__ == "__main__":

    driver = webdriver.Firefox()
    logindriver = LoginPage(driver)
    logindriver.open("https://login.taobao.com")
    logindriver.send_name("")
    logindriver.send_psw("")
    logindriver.login()

