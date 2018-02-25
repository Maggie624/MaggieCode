from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage(object):

    '''基于selenium二次封装'''

    MAXTIMEOUT = 8      # 设置最大超时时间为10s
    MINTIMEOUT = 3       # 设置最小超时时间为10s
    INTERVAL = 0.5    # 设置每隔8秒查找一次元素

    def __init__(self, driver):
        self.driver = driver

    def open(self, url):
        # 打开链接，浏览器最大化
        self.driver.get(url)
        self.driver.maximize_window()

    def find_element(self, locator):
        # 设置查找元素的超时时间为 6 秒，每隔 0.5 秒搜索一次
        element = WebDriverWait(self.driver, BasePage.MAXTIMEOUT, BasePage.INTERVAL)\
            .until(EC.presence_of_element_located(locator))
        return element

    def find_elements(self, locator):
        # 设置查找一组元素的超时时间为 6 秒，每隔 0.5 秒搜索一次
        elements = WebDriverWait(self.driver, BasePage.MAXTIMEOUT, BasePage.INTERVAL)\
            .until(EC.presence_of_all_elements_located(locator))
        return elements

    def click(self, locator):
        element = self.find_element(locator)
        element.click()

    def sendKeys(self, locator, msg, is_clear=True):
        element = self.find_element(locator)
        if is_clear == True:
            element.clear()
        element.send_keys(msg)

    def is_visible(self, locator):
        # 判断元素是否可见
        # 设置查找元素的超时时间为 3 秒，每隔 0.5 秒搜索一次
        # 返回 Boolean 值
        element = WebDriverWait(self.driver, BasePage.MINTIMEOUT, BasePage.INTERVAL)\
            .until(EC.visibility_of_element_located(locator))
        if element:
            return True
        else:
            return False
    def get_screenshot(self, filename):
        self.driver.get_screenshot_as_file(filename)

if __name__ == "__main__":
    driver = webdriver.Chrome()
    baseDriver = BasePage(driver)
    baseDriver.open('http://www.baidu.com')
    input_box = ('id', 'kw')
    searh = ('id', 'su')
    baseDriver.sendKeys(input_box, 'hello')
    baseDriver.click(searh)
