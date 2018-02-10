from selenium import webdriver
from case.models.BasePage import BasePage

class LoginPage(BasePage):

    switch_login_mode = ('id', 'J_Quick2Static')
    login_btn = ('id', 'J_SubmitStatic')
    username = ('id', 'TPL_username_1')
    psw = ('id', 'TPL_password_1')
    form_item = ('id', 'J_Form')
    img_code =

    SCANLOGINTITLE = '手机扫码，安全登录'
    LOGINFLAG = False              #密码和用户名登陆方式

    def switch_to_psw_login(self):
        print("switch")
        '''进入登陆页面后，切换到用户名密码登陆框'''

        if title == LoginPage.SCANLOGINTITLE:
            self.click(LoginPage.switch_login_way)
            LoginPage.LOGINFLAG = True
        else:
            LoginPage.LOGINFLAG = False
        return LoginPage.LOGINFLAG

    def switch_model(self):
        result = self.switch_to_psw_login()
        if result == False:
            print("未能切换登陆方式为用户名、密码登陆")
            #self.driver.quit()


    def send_name(self, name):
        print('send_name')
        if LoginPage.LOGINFLAG==False: self.switch_model()
        self.sendKeys(LoginPage.username, name)

    def send_psw(self, psw):
        print('send_psw')
        if LoginPage.LOGINFLAG==False: self.switch_model()
        self.sendKeys(LoginPage.psw, psw)

    def login(self):
        self.find_element(LoginPage.form_item).subimt()

if __name__ == "__main__":
    driver = webdriver.Chrome()
    Logindriver = LoginPage(driver)
    Logindriver.open("https://login.taobao.com")
    Logindriver.send_name("")
    Logindriver.send_psw("")

