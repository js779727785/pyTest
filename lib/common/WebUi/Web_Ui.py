# -*- encoding=utf8 -*-
__author__ = "Jmelody"
from airtest.core.api import *
from airtest_selenium.proxy import WebChrome
chrome_driver='C:/Program Files (x86)/Google/Chrome/Application/chromedriver_78.exe'
driver = WebChrome(executable_path=chrome_driver)
driver.implicitly_wait(20)
from lib.log import logger
def is_element_exist(xpath1):
    """这里注意用find_elements()
    find_element()会返回一个WebElement节点对象,但是没找到会报错,而find_elements()不会,之后返回一个空列表"""
    s=driver.find_elements_by_xpath(xpath1)
    print(s)
    if len(s)==0:
        print("元素未找到")
        return False
    elif len(s)==1:
        print("元素找到")
        return True
    else:
        print("找到%s个元素：%s"%(len(s),xpath1))
def Web_Login(userName,password):
    driver.get("https://azure-www.qingyidai.com/member/login.shtml")
    driver.find_element_by_id("name").send_keys(userName)
    driver.find_element_by_id("pwd").send_keys(password)
    driver.find_element_by_xpath("//input[@type='submit']").click()
    if is_element_exist("//*[@id='msgBtn']"):
        driver.find_element_by_id("msgBtn").click()
        driver.find_element_by_id("phoneCode").send_keys("0000")
        driver.find_element_by_xpath("//input[@value='登录']").click()
    if is_element_exist("/html/body/div[4]/div/h3"):
        driver.find_element_by_xpath("/html/body/div[4]/div/a/i").click()
    driver.assert_exist("mobileStr", "id", "登录成功")
#充值
def Web_Recharge(userName,password,amount):
    Web_Login(userName,password)
    driver.get("https://azure-www.qingyidai.com/usermanagement/account.shtml")
    if is_element_exist("/html/body/div[4]/div/h3"):
        driver.find_element_by_xpath("/html/body/div[4]/div/a/i").click()
    driver.find_element_by_xpath("//a[@href='/fundmanagement/depositfunds.shtml']").click()
    sleep(1.5)
    driver.find_element_by_xpath("//*[@id=\"online\"]/a").click()
    sleep(2)
    driver.find_element_by_xpath("//*[@id=\"bankList\"]/li[2]/a").click()
    driver.find_element_by_xpath("//*[@id=\"bankList\"]/li[2]/a/p").click()
    driver.find_element_by_id("rechargeAmount").send_keys(amount)
    driver.find_element_by_id("onlineRechargeSubmit").click()
#提现
"""
isMaxAmount:1,代表全额提现；
该脚本未做<2W限制
"""
def Web_WithDraw(userName,password,transPassword,amount=0,isMaxAmount=1):
    Web_Login(userName, password)
    driver.get("https://azure-www.qingyidai.com/usermanagement/account.shtml")
    if is_element_exist("/html/body/div[4]/div/h3"):
        driver.find_element_by_xpath("/html/body/div[4]/div/a/i").click()
    driver.find_element_by_xpath("//*[@id='drawBtn\']").click()
    driver.find_element_by_xpath("//*[@id='drawAmountInput'']").send_keys(amount)
    if isMaxAmount==1:
        driver.find_element_by_xpath("//*[@id='maxAmountBtn'").click()
    driver.find_element_by_xpath("//*[@id='drawSubmit']").click()
    sleep(2)
    driver.find_element_by_xpath("//*[@id='sendSmsVerify']").click()
    driver.find_element_by_xpath("//*[@id='alertLayer-2']/div[2]/a").click()
    driver.find_element_by_id("//*[@id='smsCode']").send_keys(password)
    driver.find_element_by_id("//*[@id='password']").send_keys(transPassword)
    driver.find_element_by_xpath("//*[@id='nextButton']").click()
Web_Recharge('16803586328','js123456','5000')
# Web_WithDraw('16803586328','js123456','js12345678')