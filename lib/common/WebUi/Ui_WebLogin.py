## -*- encoding=utf8 -*-
__author__ = "Jmelody"
from lib.MySQLHelper import MySQLHelper
from airtest.core.api import *
auto_setup(__file__)
from selenium.webdriver.common.keys import Keys

"""注意以下airtest转来的脚本由于无法直接找到chrome_driver，按照chrome版本安装chrome_driver后，按以下方式配置后生效
    保证chrome_driver支持版本和chrome一致，参考：
    https://blog.csdn.net/qq_26200629/article/details/86141131
"""
from selenium import webdriver
chrome_driver='C:/Program Files (x86)/Google/Chrome/Application/chromedriver_76.exe'
driver=webdriver.Chrome(executable_path=chrome_driver)
# driver = WebChrome()
driver.implicitly_wait(20)
from lib.log import logger


def Login(tel_num,password):
    driver.get("https://azure-www.qingyidai.com/member/login.shtml")
    driver.find_element_by_xpath("//*[@id=\"name\"]").send_keys(tel_num)
    driver.find_element_by_xpath("//*[@id=\"pwd\"]").send_keys(password, Keys.ENTER)
    time.sleep(2)
    """todo_加一个弹窗判断"""

    # driver.find_element_by_xpath("//*[@id=\"msgBtn\"]").click()
    # driver.find_element_by_xpath("//*[@id=\"phoneCode\"]").send_keys('0000', Keys.ENTER)
    logger.info(str(tel_num)+"登录成功！！！")

Login('16803585780','js123456')


