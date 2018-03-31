from selenium import webdriver

from TBtestProject.case.pages.loginpage import LoginPage

class Login():
    """
    Usage: 封装登录页面需要调用的方法
    """

    DEFAULT_NAME = 'xxxxxxxxxxx'
    DEFAULT_PSW = 'xxxxxxxxxxxx'
    cookies = []

    AUTO_IN = False          # 是否可以实现Cookies登录的标识位

    # 登 录(常规流程)
    @classmethod
    def login(cls, driver, username=DEFAULT_NAME, password=DEFAULT_PSW):
        mydriver = LoginPage(driver)
        mydriver.open("https://login.taobao.com")
        mydriver.send_name(username)
        mydriver.send_psw(password)
        mydriver.login()

    @classmethod
    def pre_Auto(cls, driver):
        Login.cookies = driver.get_cookies()
        print("===============cookies=================")
        print(Login.cookies)
        print("===============cookies=================")
        Login.AUTO_IN = True

    # Cookies登录
    @classmethod
    def login_auto(cls, driver):

        if not Login.AUTO_IN:
            cls.login(driver)
            return
        for cookie in Login.cookies:
            driver.add_cookie({'name': cookie['name'], 'value': cookie['value']})
        driver.refresh()

    # 退 出
    @classmethod
    def logout(cls):
        pass



