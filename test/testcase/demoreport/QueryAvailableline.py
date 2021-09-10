    #coding=utf-8
import unittest
import requests
from lib.generateTestCases import __generateTestCases
from lib.log import logger
from config.demoUrl import qyd_url
from lib.mysql.userQuery import queryuser

headers = {"Content-type": "application/json","X-Auth-Token":""}


"""
查询总的可用借款额度
"""


class QueryAvailableline(unittest.TestCase):
    """查询总的可用借款额度---Jmelody"""
    def setUp(self):
        logger.info("****************查  询总的可用借款额度接口开始****************")

    def getTest(self, tx):
        infoUrl = "/nbigfront/loan/queryavailableline"
        caseNum = tx['test_name']
        caseName = tx['test_description']
        """注意excel中数字的单元格设置为文本,提取出时str格式，下方断言中result['code']==10000 为int格式，注意比较时格式转换"""
        code = tx['code']
        phone=tx['phone']
        user_id= queryuser(phone)
        parm = {"userId": user_id}
        if user_id =='':
            parm = {}
        logger.info("*******测试案例名称： TestCase" + caseNum + "_" + caseName + " 执行开始********")
        logger.info("*******测试数据： " + str(parm))
        test_url=qyd_url+infoUrl
        logger.info("*******测试url： " + str(test_url))
        r = requests.post(url=test_url,json=parm, headers=headers)
        result = r.json()
        logger.info("*******返回数据： " + str(result))
        logger.info("*******requests结果code:  "+str(result['code'])+"     ,预期结果： "+code)
        self.assertEqual(code,str(result['code']))
        logger.info("*******测试案例名称： TestCase" + caseNum + "_" + caseName + " 执行完毕********")
        if result['code']==10000:
            print("查询结果:   "+str(result['data']))
            logger.info("查询结果:   "+str(result['data']['availableBorrowLine']))



    @staticmethod
    def getTestFunc(arg1):
        def func(self):
            self.getTest(arg1)
        return func

    def tearDown(self):
        logger.info("****************查询总的可用借款额度接口结束****************")

__generateTestCases(QueryAvailableline, "QueryAvailableline", "demo.xlsx", "查询总的可用借款额度")
