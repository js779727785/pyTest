
import unittest
import random
import datetime
from config.demoUrl import base_url
import requests
from lib.mysql.userQuery import queryOldPossessionInfo
def testgo():
    """二者之间的随机数"""
    # str(random.randrange(10000000, 99999999))
    r = random.randrange(10,200)
    print(r)
    return r
def randomInt():
    a= random.randint(0,100)
    print(a)
    return a
def nowtime():
    # 获取当前时间 格式为 20170101000000
    currentTime = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    print(currentTime)
    return  currentTime
def demomanysql(param):
    possessionInfo=queryOldPossessionInfo(param)
    print(possessionInfo)
    possLen = possessionInfo.__len__()
    print(possLen)

demomanysql('ad45f833-748c-4fa2-9695-c41514ab6d0a')