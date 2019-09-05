# # -*- encoding=utf8 -*-
# __author__ = "Jmelody"
# from lib.MySQLHelper import MySQLHelper
# from airtest.core.api import *
# auto_setup(__file__)
# from selenium.webdriver.common.keys import Keys
#
# """注意以下airtest转来的脚本由于无法直接找到chrome_driver，按照chrome版本安装chrome_driver后，按以下方式配置后生效
#     保证chrome_driver支持版本和chrome一致，参考：
#     https://blog.csdn.net/qq_26200629/article/details/86141131
# """
# from selenium import webdriver
# chrome_driver='C:/Program Files (x86)/Google/Chrome/Application/chromedriver_76.exe'
# driver=webdriver.Chrome(executable_path=chrome_driver)
# # driver = WebChrome()
# driver.implicitly_wait(20)
# from lib.log import logger
#
#
# def DemoWebUi(tel_num):
#     str=''
#     driver.find_element_by_xpath("//input[@data-parsley-length='[0, 100]']").send_keys(str(str[0]['xw_id']), Keys.ENTER)
#     logger.info(str(tel_num)+"——————someLog——————")
