# coding=utf-8
from appium import webdriver
import time

desired_caps = {
    'deviceName': 'VNX9X19B05002805',
    'platformVersion': '9',
    'platformName':'Android',
    'appPackage': 'cn.xckj.talk_junior',
    'appActivity': '',
}
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)