import time
from selenium import webdriver
from selenium.webdriver import ActionChains

from case.models.BasePage import BasePage

class LoginPage(BasePage):

    switch_login_mode = ('id', 'J_Quick2Static')  #切换登录模式按钮
    login_btn = ('id', 'J_SubmitStatic')
    username = ('id', 'TPL_username_1')
    psw = ('id', 'TPL_password_1')
    form_item = ('id', 'J_Form')
    scan_tip = ('class name', 'ft-gray')        #二维码下方"扫一扫登录"文字
    slider = ('id', 'nc_1_n1z')

    SCANLOGINTITLE = '手机扫码，安全登录'
    LOGINFLAG = False              #密码和用户名登陆方式

    def switch_to_psw_login(self):
        print("switch")
        '''切换到用户名密码登陆框'''
        self.click(LoginPage.switch_login_mode)
        LoginPage.LOGINFLAG = True

    def switch_model(self):
        result = self.find_element(LoginPage.scan_tip)
        print(result)
        '''二维码存在，则需要点击切换登陆方式'''
        if result:
            self.switch_to_psw_login()

    def send_name(self, name):
        print('send_name')
        if LoginPage.LOGINFLAG==False: self.switch_model()
        self.sendKeys(LoginPage.username, name)

    def send_psw(self, psw):
        print('send_psw')
        if LoginPage.LOGINFLAG==False: self.switch_model()
        self.sendKeys(LoginPage.psw, psw)

    def dragSlider(self):
        '''不能触发验证通过的逻辑，但是可以界面演示拖动效果'''
        js1 = 'document.getElementById("nc_1__bg").setAttribute("style","width: 300px;");' \
             'document.getElementById("nc_1_n1z").setAttribute("style","left: 300;");'
        self.driver.execute_script(js1)
        time.sleep(1)
        self.driver.execute_script(js2)
        ActionChains(self.driver).move_to_element(self.find_element(LoginPage.switch_login_mode)).perform()

    def login(self):
        slider = self.find_element(LoginPage.slider)
        if slider:
            self.dragSlider()
        time.sleep(2)
        self.find_element(LoginPage.form_item).submit()



if __name__ == "__main__":

    driver = webdriver.Firefox()
    logindriver = LoginPage(driver)
    logindriver.open("https://login.taobao.com")
    logindriver.send_name("")
    time.sleep(2)
    logindriver.send_psw("")
    time.sleep(2)
    logindriver.login()

