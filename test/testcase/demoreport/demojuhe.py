from lib.log import logger
import requests
import unittest
from config.demoUrl import base_url
from lib.common.DemoLogin import qydFrontLogin
from lib.generateTestCases import __generateTestCases
import json

headers = {"Content-type": "application/json"}
class juhe(unittest.TestCase):
    def setUp(self) -> None:
        logger.info("*"*10+"start")

    def getTest(self,tx):
        logger.info("sheet case start")
        gethomeuserinfourl="/nbigfront/nw/entrance/apis/register/gethomeuserinfo/json"
        url=base_url+gethomeuserinfourl
        par1=tx['param']
        # print(par1)
        #从excl里提取出来的par1是str格式，要转换为json
        # p1= json.loads(par1)['imei']
        # print(p1)
        # par2=tx["param"]
        data=par1
        token=qydFrontLogin('16803581610','js12345678')
        logger.info("token:"+token)
        headers['X-Auth-Token']=token
        logger.info(headers['X-Auth-Token'])
        r=requests.post(url=url,json=data,headers=headers)
        o=requests.post(url=url+"old",json=data,headers=headers)
        response=r.json()
        old=o.json()
        logger.info("response:"+str(response))
        logger.info("old:"+str(old))
        self.assertEqual(response['mapData'],old['mapData'])

    @staticmethod
    def getTestFunc(arg1):
        def func(self):
            self.getTest(arg1)
        return func

    def tearDown(self) -> None:
        logger.info("***end***")

__generateTestCases(juhe,"juhe","demo.xlsx","juhe")