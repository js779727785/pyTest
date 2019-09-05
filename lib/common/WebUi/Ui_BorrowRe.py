## -*- encoding=utf8 -*-
__author__ = "Jmelody"
from selenium.webdriver.common.keys import Keys
from airtest.core.api import *
auto_setup(__file__)
from selenium import webdriver
chrome_driver='C:/Program Files (x86)/Google/Chrome/Application/chromedriver_76.exe'
driver=webdriver.Chrome(executable_path=chrome_driver)
# driver = WebChrome()
driver.implicitly_wait(20)
from lib.log import logger
# from lib.common.WebUi import Ui_WebLogin

def UiBorrowRe(tel_num,password):
    driver.get("https://azure-www.qingyidai.com/member/login.shtml")
    driver.find_element_by_xpath("//*[@id=\"name\"]").send_keys(tel_num)
    driver.find_element_by_xpath("//*[@id=\"pwd\"]").send_keys(password, Keys.ENTER)
    driver.find_element_by_xpath("//*[@id=\"msgBtn\"]").click()
    driver.find_element_by_xpath("//*[@id=\"phoneCode\"]").send_keys('0000', Keys.ENTER)
    time.sleep(10)
    driver.find_element_by_xpath("//*[@id=\"left-nav\"]/ul/li[11]/a").click()
    time.sleep(2)
    # 多刷新一次，防止页面信息加载不出来
    driver.find_element_by_xpath("//*[@id=\"left-nav\"]/ul/li[11]/a").click()
    time.sleep(3)
    # 点击开通借款人按钮
    driver.find_element_by_xpath("//*[@id=\"borrowerDeposContainer\"]/span[3]/a").click()
    # 跳转到新网填写表单页
    # 点击发送验证码
    driver.find_element_by_xpath("//*[@id=\"sendSmsVerify\"]").click()
    # 点击我知道了弹窗
    driver.find_element_by_xpath("//*[@id=\"alertLayer-2\"]/div[2]/a").click()
    # 填写表单内容
    driver.find_element_by_xpath("//*[@id=\"smsCode\"]").send_keys("0000")
    driver.find_element_by_xpath("//*[@id=\"password\"]").send_keys("js12345678")
    driver.find_element_by_xpath("//*[@id=\"nextButton\"]").click()
    logger.info(str(tel_num)+"开通借款人成功!!!")
UiBorrowRe('16803586924','js123456')


