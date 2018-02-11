from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage(object):

    '''基于selenium二次封装'''

    MAXTIMEOUT = 10      #设置最大超时时间为10s
    MINTIMEOUT = 3       #设置最小超时时间为10s
    INTERVAL = 0.8    #设置每隔8秒查找一次元素

    def __init__(self, driver):
        self.driver = driver

    def open(self, url):
        self.driver.get(url)
        self.driver.maximize_window()

    def find_element(self, locator):
        element = WebDriverWait(self.driver, BasePage.MAXTIMEOUT, BasePage.INTERVAL)\
            .until(EC.presence_of_element_located(locator))
        return element

    def find_elements(self, locator):
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
        element = WebDriverWait(self.driver, BasePage.MINTIMEOUT, BasePage.INTERVAL)\
            .until(EC.visibility_of_element_located(locator))
        if element:
            return True
        else:
            return False

if __name__ == "__main__":
    driver = webdriver.Chrome()
    baseDriver = BasePage(driver)
    baseDriver.open('http://www.baidu.com')
    input_box = ('id', 'kw')
    searh = ('id', 'su')
    baseDriver.sendKeys(input_box,'hello')
    baseDriver.click(searh)
