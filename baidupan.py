import time
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

driver = webdriver.Firefox()
driver.implicitly_wait(4)
driver.get("https://pan.baidu.com/")
time.sleep(2)

driver.find_element_by_xpath("//div[@class='account-title']/a[@href='javascript:;']").click() #跳转到账号密码登陆
driver.find_element_by_id("TANGRAM__PSP_4__userName").send_keys("落幕可荻")
driver.find_element_by_id("TANGRAM__PSP_4__password").send_keys("cmd15fzwakkn")
driver.find_element_by_id("TANGRAM__PSP_4__submit").click()

time.sleep(3)
try:
    driver.find_element_by_xpath("//div[@class='close icon icon-close']").click() #关闭弹出框
    driver.find_element_by_xpath("//span[@class='close icon icon-close']").click() #关闭设置二级验证的弹窗
except NoSuchElementException as e:
    print("没有弹出框"+str(e))