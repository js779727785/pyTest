# -*- encoding=utf8 -*-
__author__ = "Jmelody"
from lib.MySQLHelper import MySQLHelper
from airtest.core.api import *
"""注意以下airtest转来的脚本由于无法直接找到chrome_driver，按照chrome版本安装chrome_driver后，重写executable_path，chrome_driver下载地址：
    http://npm.taobao.org/mirrors/chromedriver/
"""
# 没有用selenium的webdriver而是用的airtest_selenium
from selenium.webdriver.common.keys import Keys
# from selenium import webdriver
# driver=webdriver.Chrome(executable_path=chrome_driver)
from airtest_selenium import WebChrome
chrome_driver='C:/Program Files (x86)/Google/Chrome/Application/chromedriver.exe'
driver = WebChrome(executable_path=chrome_driver)
driver.implicitly_wait(20)
from lib.log import logger


def XwCheckUi(tel_num):
    xw_id_sql="select xw_id from xw_user_role WHERE user_id=(SELECT id FROM user WHERE tel_num=%s)ORDER BY create_time desc"
    xw_id = MySQLHelper('qydproduction').get_many(xw_id_sql,tel_num)
    if xw_id is not None:
        logger.info("*******新网审核中,企业用户手机号：" + str(tel_num) + " 新网用户编号：" + str(xw_id[0]['xw_id']))
        xw_url = "http://47.94.123.201:9000/lanmao-boss-app-pt/login"
        driver.get(xw_url)
        username = 'lmservice'
        password = 'lmservice'
        driver.find_element_by_id("name").send_keys(username)
        driver.find_element_by_id("password").send_keys(password, Keys.ENTER)
        driver.find_element_by_xpath("//*[@id=\"portal\"]/div/div/a/span").click()
        driver.find_element_by_xpath("//*[@id=\"menu_toggle\"]/i").click()
        driver.find_element_by_xpath("//*[@id=\"sidebar-menu\"]/div/ul/li/a/i").click()
        driver.find_element_by_xpath("//*[@id=\"sidebar-menu\"]/div/ul/li/ul/li[1]/a").click()
        driver.find_element_by_xpath("//input[@data-parsley-length='[3, 20]']").send_keys("6000003832")
        driver.find_element_by_xpath("//input[@data-parsley-length='[0, 100]']").send_keys(str(xw_id[0]['xw_id']),                                                                                         Keys.ENTER)
        logger.info(str(tel_num) + "——————新网审核成功,去前台登录查看吧！——————")
    else:
        logger.error("———xw_id is None!!!!")

XwCheckUi('16803584422')