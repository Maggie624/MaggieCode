from TBtestProject.case.pages.loginpage import LoginPage

class Login:
    """
    Usage: 封装登录方法
    """
    DEFAULT_NAME = 'xxxxxxxxxxx'
    DEFAULT_PSW = 'xxxxxxxxxxxx'
    cookies = []

    AUTO_IN = False          # 是否可以实现Cookies登录的标识位

    @staticmethod
    def login_auto(driver):
        """Cookies自动登录"""
        if not Login.AUTO_IN:
            Login.login_normal(driver)
            return
        for cookie in Login.cookies:
            driver.add_cookie({'name': cookie['name'], 'value': cookie['value']})
        driver.refresh()

    @staticmethod
    def login_normal(driver, username=DEFAULT_NAME, password=DEFAULT_PSW):
        """登 录(常规流程)"""
        mydriver = LoginPage(driver)
        mydriver.open("https://login.taobao.com")
        mydriver.send_name(username)
        mydriver.send_psw(password)
        mydriver.login()

    @staticmethod
    def collec_cookies(driver):
        """登录后获取cookies"""
        Login.cookies = driver.get_cookies()
        print("===============cookies=================")
        print(Login.cookies)
        print("===============cookies=================")
        Login.AUTO_IN = True


    # 退 出
    def logout(self):
        pass



