
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
import TBtestProject.case.models.func as Func


class BasePage(object):
    """
    基于selenium二次封装
    """

    def __init__(self, driver):
        self.driver = driver

    def open(self, url):
        """ 打开链接，浏览器最大化 """
        self.driver.get(url)
        self.driver.maximize_window()

    def find_element(self, locator):
        """ 设置查找元素的超时时间为 6 秒，每隔 0.5 秒搜索一次 """
        element = WebDriverWait(self.driver, 6, 0.5)\
            .until(EC.presence_of_element_located(locator))
        return element

    def find_elements(self, locator):
        """ 设置查找一组元素的超时时间为 6 秒，每隔 0.5 秒搜索一次 """
        elements = WebDriverWait(self.driver, 6, 0.5)\
            .until(EC.presence_of_all_elements_located(locator))
        return elements

    def click(self, locator):
        """ 点击元素"""
        element = self.find_element(locator)
        element.click()

    def sendKeys(self, locator, msg, is_clear=True):
        """ 对元素输入文本 """
        element = self.find_element(locator)
        if is_clear == True:
            element.clear()
        element.send_keys(msg)

    def is_visible(self, locator):
        """ 判断元素是否可见 """
        # 判断元素是否可见
        # 设置查找元素的超时时间为 3 秒，每隔 0.5 秒搜索一次
        # 返回 Boolean 值
        element = WebDriverWait(self.driver, 3, 0.5)\
            .until(EC.visibility_of_element_located(locator))
        if element:
            return True
        else:
            return False

    def get_screenshot(self, filename):
        """ 屏幕截图 """
        dir = Func.get_pngs_dir()
        self.driver.get_screenshot_as_file(dir + '/' + filename)

    def get_cookies(self):
        """ 获取cookies """
        return driver.get_cookies()

    def move_to_element(self, driver, element):
        """ 鼠标悬停到某可见元素 """
        ActionChains(driver).move_to_element(element).perform()

    def execute_script(self, js_command):
        self.driver.execute_script(js_command)

    def switch_to_alert_and_confirm(self):
        """切换到弹出框"""
        self.driver.switch_to_alert().accept()

    def go_back(self):
        """后退到上一页"""
        self.driver.back()

    def refresh_(self):
        """刷新"""
        self.driver.refresh()

    def dismiss_alert(self):
        """解散弹出框"""
        self.driver.switch_to_alert().dismiss()

    def accept_alert(self):
        """接受弹出框"""
        self.driver.switch_to_alert().accept()



if __name__ == "__main__":
    driver = webdriver.Chrome()
    baseDriver = BasePage(driver)
    baseDriver.open('http://www.baidu.com')
    input_box = ('id', 'kw')
    searh = ('id', 'su')
    baseDriver.sendKeys(input_box, 'hello')
    baseDriver.click(searh)
